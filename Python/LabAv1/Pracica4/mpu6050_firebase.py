"""
Medición de la Aceleración Gravitacional usando un Sensor MPU6050
y ESP32 con Envío de Datos a Firebase

Conexiones MPU6050:
VIN → VIN (3.3V)
GND → GND
SCL → IO18
SDA → IO5
"""

from machine import Pin, I2C
import network
import urequests
import ujson
import time
import gc

# ========== CONFIGURACIÓN WIFI ==========
WIFI_SSID = "jjRedmi"  # CAMBIAR: Pon aquí el nombre de tu red WiFi
WIFI_PASSWORD = "12345678"  # CAMBIAR: Pon aquí la contraseña de tu WiFi

# ========== CONFIGURACIÓN FIREBASE ==========
FIREBASE_URL = "https://esp32-b6f1c-default-rtdb.firebaseio.com"
FIREBASE_SECRET = "TFmu701vTWgTXUic1laAhJtzYeh3gAzxwhWg1RnU"

# ========== CONFIGURACIÓN MPU6050 ==========
i2c = I2C(0, scl=Pin(18), sda=Pin(5), freq=400000)
MPU6050_ADDR = 0x68

# Registros del MPU6050
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43
WHO_AM_I = 0x75

# Variables globales
wifi_connected = False

def connect_wifi():
    """Conecta a la red WiFi"""
    global wifi_connected
    
    print("Conectando a WiFi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        
        # Esperar conexión (máximo 20 segundos)
        timeout = 20
        while not wlan.isconnected() and timeout > 0:
            print(".", end="")
            time.sleep(1)
            timeout -= 1
    
    if wlan.isconnected():
        wifi_connected = True
        print(f"\n✅ WiFi conectado!")
        print(f"IP: {wlan.ifconfig()[0]}")
        return True
    else:
        wifi_connected = False
        print("\n❌ Error: No se pudo conectar a WiFi")
        print("Verifica el SSID y contraseña en el código")
        return False

def init_mpu6050():
    """Inicializa el sensor MPU6050"""
    try:
        # Verificar que el sensor esté presente
        devices = i2c.scan()
        if MPU6050_ADDR not in devices:
            print("❌ MPU6050 no encontrado")
            return False
        
        # Leer WHO_AM_I para verificar
        who_am_i = i2c.readfrom_mem(MPU6050_ADDR, WHO_AM_I, 1)[0]
        if who_am_i != 0x68:
            print(f"❌ Sensor incorrecto. WHO_AM_I: {hex(who_am_i)}")
            return False
        
        # Despertar el sensor (salir del modo sleep)
        i2c.writeto_mem(MPU6050_ADDR, PWR_MGMT_1, bytes([0]))
        print("✅ MPU6050 inicializado correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error al inicializar MPU6050: {e}")
        return False

def read_raw_data(addr):
    """Lee datos raw de 16 bits del sensor"""
    try:
        high = i2c.readfrom_mem(MPU6050_ADDR, addr, 1)[0]
        low = i2c.readfrom_mem(MPU6050_ADDR, addr + 1, 1)[0]
        
        # Combinar bytes y convertir a signed int
        value = (high << 8) | low
        if value > 32768:
            value -= 65536
        return value
    except Exception as e:
        print(f"Error leyendo datos: {e}")
        return None

def read_sensor_data():
    """Lee todos los datos del sensor y calcula valores físicos"""
    try:
        # Leer datos raw del acelerómetro
        accel_x_raw = read_raw_data(ACCEL_XOUT_H)
        accel_y_raw = read_raw_data(ACCEL_XOUT_H + 2)
        accel_z_raw = read_raw_data(ACCEL_XOUT_H + 4)
        
        # Leer datos raw del giroscopio
        gyro_x_raw = read_raw_data(GYRO_XOUT_H)
        gyro_y_raw = read_raw_data(GYRO_XOUT_H + 2)
        gyro_z_raw = read_raw_data(GYRO_XOUT_H + 4)
        
        # Leer temperatura
        temp_raw = read_raw_data(0x41)
        
        if None in [accel_x_raw, accel_y_raw, accel_z_raw, gyro_x_raw, gyro_y_raw, gyro_z_raw, temp_raw]:
            return None
        
        # Convertir a valores físicos
        # Acelerómetro: dividir por 16384 para obtener valores en g (±2g range)
        accel_x = accel_x_raw / 16384.0
        accel_y = accel_y_raw / 16384.0
        accel_z = accel_z_raw / 16384.0
        
        # Giroscopio: dividir por 131 para obtener valores en °/s (±250°/s range)
        gyro_x = gyro_x_raw / 131.0
        gyro_y = gyro_y_raw / 131.0
        gyro_z = gyro_z_raw / 131.0
        
        # Temperatura en Celsius
        temp_celsius = (temp_raw / 340.0) + 36.53
        
        # Calcular ángulos de inclinación usando acelerómetro
        import math
        
        # Calcular ángulos (en grados)
        angle_x = math.atan2(accel_y, math.sqrt(accel_x*accel_x + accel_z*accel_z)) * 180 / math.pi
        angle_y = math.atan2(-accel_x, math.sqrt(accel_y*accel_y + accel_z*accel_z)) * 180 / math.pi
        angle_z = math.atan2(accel_z, math.sqrt(accel_x*accel_x + accel_y*accel_y)) * 180 / math.pi
        
        # Magnitud de la aceleración total
        accel_magnitude = math.sqrt(accel_x*accel_x + accel_y*accel_y + accel_z*accel_z)
        
        return {
            'timestamp': time.time(),
            'accel_raw': {'x': accel_x_raw, 'y': accel_y_raw, 'z': accel_z_raw},
            'accel_g': {'x': accel_x, 'y': accel_y, 'z': accel_z},
            'gyro_raw': {'x': gyro_x_raw, 'y': gyro_y_raw, 'z': gyro_z_raw},
            'gyro_dps': {'x': gyro_x, 'y': gyro_y, 'z': gyro_z},
            'angles': {'x': angle_x, 'y': angle_y, 'z': angle_z},
            'accel_magnitude': accel_magnitude,
            'temperature': temp_celsius
        }
        
    except Exception as e:
        print(f"Error leyendo datos del sensor: {e}")
        return None

def send_to_firebase(data):
    """Envía datos a Firebase"""
    global wifi_connected
    
    if not wifi_connected:
        print("❌ WiFi no conectado")
        return False
    
    try:
        # Crear un timestamp único para cada entrada
        timestamp_str = str(int(time.time() * 1000))  # Timestamp en milisegundos
        
        # URL sin autenticación primero (para probar)
        url = f"{FIREBASE_URL}/sensor_data/{timestamp_str}.json"
        
        # Preparar datos para envío (simplificados)
        firebase_data = {
            'timestamp': data['timestamp'],
            'accel_x': round(data['accel_g']['x'], 3),
            'accel_y': round(data['accel_g']['y'], 3),
            'accel_z': round(data['accel_g']['z'], 3),
            'angle_x': round(data['angles']['x'], 1),
            'angle_y': round(data['angles']['y'], 1),
            'angle_z': round(data['angles']['z'], 1),
            'magnitude': round(data['accel_magnitude'], 3),
            'temperature': round(data['temperature'], 1),
            'device': 'ESP32_MPU6050'
        }
        
        # Convertir a JSON
        json_data = ujson.dumps(firebase_data)
        
        print(f"🔄 Enviando a: {url}")
        
        # Enviar datos usando PUT (más confiable para Firebase)
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'ESP32'
        }
        
        response = urequests.put(url, data=json_data, headers=headers)
        
        if response.status_code == 200:
            print("✅ Datos enviados a Firebase")
            response.close()
            return True
        else:
            print(f"❌ Error HTTP: {response.status_code}")
            print(f"Response: {response.text}")
            response.close()
            return False
            
    except OSError as e:
        print(f"❌ Error de conexión: {e}")
        return False
    except Exception as e:
        print(f"❌ Error enviando a Firebase: {e}")
        return False
    finally:
        # Liberar memoria
        gc.collect()

def test_firebase_connection():
    """Prueba la conexión a Firebase con datos simples"""
    if not wifi_connected:
        print("❌ WiFi no conectado")
        return False
    
    try:
        print("🔍 Probando conexión a Firebase...")
        
        # Datos de prueba simples
        test_data = {
            'test': 'connection',
            'timestamp': time.time(),
            'value': 123
        }
        
        # URL de prueba
        test_url = f"{FIREBASE_URL}/test.json"
        json_data = ujson.dumps(test_data)
        
        print(f"📡 URL de prueba: {test_url}")
        
        # Probar con PUT
        headers = {'Content-Type': 'application/json'}
        response = urequests.put(test_url, data=json_data, headers=headers)
        
        print(f"📊 Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Conexión a Firebase exitosa!")
            response.close()
            return True
        else:
            print(f"❌ Error en la prueba: {response.text}")
            response.close()
            return False
            
    except Exception as e:
        print(f"❌ Error en prueba de Firebase: {e}")
        return False

def main():
    """Función principal"""
    print("=" * 60)
    print("MEDICIÓN DE ACELERACIÓN GRAVITACIONAL")
    print("ESP32 + MPU6050 + Firebase")
    print("=" * 60)
    
    # 1. Conectar WiFi
    print("\n1. Conectando a WiFi...")
    if not connect_wifi():
        print("⚠️  Continuando sin WiFi (solo lectura local)")
    
    # 2. Inicializar sensor
    print("\n2. Inicializando MPU6050...")
    if not init_mpu6050():
        print("❌ No se puede continuar sin el sensor")
        return
    
    # 3. Probar conexión Firebase
    if wifi_connected:
        print("\n3. Probando conexión a Firebase...")
        if test_firebase_connection():
            print("✅ Firebase listo para recibir datos")
        else:
            print("⚠️  Problemas con Firebase - continuando sin envío de datos")
    
    # 4. Bucle principal de medición
    print("\n4. Iniciando mediciones...")
    print("Presiona Ctrl+C para detener\n")
    
    measurement_count = 0
    
    try:
        while True:
            measurement_count += 1
            
            # Leer datos del sensor
            data = read_sensor_data()
            
            if data:
                # Mostrar datos en consola
                print(f"--- Medición {measurement_count} ---")
                print(f"Aceleración (g): X={data['accel_g']['x']:6.3f}, Y={data['accel_g']['y']:6.3f}, Z={data['accel_g']['z']:6.3f}")
                print(f"Ángulos (°):     X={data['angles']['x']:6.1f}, Y={data['angles']['y']:6.1f}, Z={data['angles']['z']:6.1f}")
                print(f"Magnitud: {data['accel_magnitude']:.3f}g")
                print(f"Temperatura: {data['temperature']:.1f}°C")
                
                # Enviar a Firebase si hay conexión
                if wifi_connected:
                    send_success = send_to_firebase(data)
                    if not send_success:
                        print("⚠️  Error al enviar datos")
                else:
                    print("📡 Sin conexión WiFi - solo lectura local")
                
                print("-" * 50)
                
            else:
                print(f"❌ Error en medición {measurement_count}")
            
            # Esperar antes de la siguiente medición
            time.sleep(2)  # Medición cada 2 segundos
            
    except KeyboardInterrupt:
        print(f"\n⏹️  Mediciones detenidas por el usuario")
        print(f"Total de mediciones: {measurement_count}")
    except Exception as e:
        print(f"\n❌ Error durante las mediciones: {e}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
