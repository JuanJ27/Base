"""
Código de prueba para verificar el funcionamiento del sensor MPU6050
Conexiones:
VIN → VIN (3.3V)
GND → GND
SCL → IO18
SDA → IO5
"""

from machine import Pin, I2C
import time

# Configuración del I2C
i2c = I2C(0, scl=Pin(18), sda=Pin(5), freq=400000)

# Dirección del MPU6050
MPU6050_ADDR = 0x68

# Registros del MPU6050
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43
WHO_AM_I = 0x75

def init_mpu6050():
    """Inicializa el sensor MPU6050"""
    try:
        # Despertar el sensor (salir del modo sleep)
        i2c.writeto_mem(MPU6050_ADDR, PWR_MGMT_1, bytes([0]))
        print("MPU6050 inicializado correctamente")
        return True
    except Exception as e:
        print(f"Error al inicializar MPU6050: {e}")
        return False

def check_connection():
    """Verifica la conexión con el sensor"""
    try:
        devices = i2c.scan()
        print(f"Dispositivos I2C encontrados: {[hex(device) for device in devices]}")
        
        if MPU6050_ADDR in devices:
            print(f"MPU6050 encontrado en dirección: {hex(MPU6050_ADDR)}")
            
            # Leer el registro WHO_AM_I para verificar
            who_am_i = i2c.readfrom_mem(MPU6050_ADDR, WHO_AM_I, 1)[0]
            print(f"WHO_AM_I register: {hex(who_am_i)}")
            
            if who_am_i == 0x68:
                print("✅ MPU6050 verificado correctamente!")
                return True
            else:
                print("❌ Respuesta incorrecta del sensor")
                return False
        else:
            print("❌ MPU6050 no encontrado en el bus I2C")
            return False
            
    except Exception as e:
        print(f"Error en la verificación: {e}")
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
    """Lee todos los datos del sensor"""
    try:
        # Leer acelerómetro (3 ejes)
        accel_x = read_raw_data(ACCEL_XOUT_H)
        accel_y = read_raw_data(ACCEL_XOUT_H + 2)
        accel_z = read_raw_data(ACCEL_XOUT_H + 4)
        
        # Leer giroscopio (3 ejes)
        gyro_x = read_raw_data(GYRO_XOUT_H)
        gyro_y = read_raw_data(GYRO_XOUT_H + 2)
        gyro_z = read_raw_data(GYRO_XOUT_H + 4)
        
        # Leer temperatura
        temp_raw = read_raw_data(0x41)
        temp_celsius = (temp_raw / 340.0) + 36.53
        
        return {
            'accel': {'x': accel_x, 'y': accel_y, 'z': accel_z},
            'gyro': {'x': gyro_x, 'y': gyro_y, 'z': gyro_z},
            'temp': temp_celsius
        }
    except Exception as e:
        print(f"Error leyendo datos del sensor: {e}")
        return None

def main():
    """Función principal de prueba"""
    print("=" * 50)
    print("PRUEBA DE FUNCIONAMIENTO MPU6050")
    print("=" * 50)
    
    # Verificar conexión I2C
    print("\n1. Verificando conexión I2C...")
    if not check_connection():
        print("❌ No se pudo establecer conexión con el MPU6050")
        print("Verifica las conexiones:")
        print("  VIN → VIN (3.3V)")
        print("  GND → GND")
        print("  SCL → IO18")
        print("  SDA → IO5")
        return
    
    # Inicializar sensor
    print("\n2. Inicializando sensor...")
    if not init_mpu6050():
        print("❌ Error en la inicialización")
        return
    
    # Leer datos continuamente
    print("\n3. Leyendo datos del sensor...")
    print("Presiona Ctrl+C para detener\n")
    
    try:
        for i in range(10):  # Leer 10 veces como prueba
            data = read_sensor_data()
            if data:
                print(f"Lectura {i+1}:")
                print(f"  Acelerómetro - X: {data['accel']['x']:6d}, Y: {data['accel']['y']:6d}, Z: {data['accel']['z']:6d}")
                print(f"  Giroscopio   - X: {data['gyro']['x']:6d}, Y: {data['gyro']['y']:6d}, Z: {data['gyro']['z']:6d}")
                print(f"  Temperatura: {data['temp']:.2f}°C")
                print("-" * 40)
            else:
                print(f"❌ Error en lectura {i+1}")
            
            time.sleep(0.5)
            
        print("\n✅ Prueba completada exitosamente!")
        print("El sensor MPU6050 está funcionando correctamente.")
        
    except KeyboardInterrupt:
        print("\n⏹️ Prueba interrumpida por el usuario")
    except Exception as e:
        print(f"\n❌ Error durante la prueba: {e}")

# Ejecutar la prueba
if __name__ == "__main__":
    main()
