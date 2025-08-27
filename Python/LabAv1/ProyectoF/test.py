from machine import Pin, ADC
import time
import os

# Configura el ADC en los pines correspondientes
azul = ADC(Pin(39))
verde = ADC(Pin(36))
amarillo = ADC(Pin(34))
naranja = ADC(Pin(35))
rojo = ADC(Pin(04))
5
# Intenta configurar la atenuación para 0-3.3V
try:
    azul.atten(ADC.ATTN_11DB)  # Para rango completo (0-3.3V)
    verde.atten(ADC.ATTN_11DB)
    amarillo.atten(ADC.ATTN_11DB)
    naranja.atten(ADC.ATTN_11DB)
    rojo.atten(ADC.ATTN_11DB)
except ValueError:
    azul.atten(3)  # Valor numérico para 11 dB
    verde.atten(3)
    amarillo.atten(3)
    naranja.atten(3)
    rojo.atten(3)

# Nombre del archivo CSV
filename = "linea.csv"

# Crear archivo CSV con encabezados si no existe
if filename not in os.listdir():
    with open(filename, "w") as f:
        f.write("tiempo,azul,verde,amarillo,naranja,rojo\n")

# Contador para muestras
contador = 0
tiempo_inicio = time.time()

try:
    while True:
        valor_azul = azul.read()
        valor_verde = verde.read()
        valor_amarillo = amarillo.read()
        valor_naranja = naranja.read()
        valor_rojo = rojo.read()

        # Obtener tiempo transcurrido
        tiempo_actual = time.time() - tiempo_inicio
        
        # Mostrar en consola
        print(f"""
              naranja: {valor_naranja}, azul: {valor_azul}
                    amarillo: {valor_amarillo}
              rojo: {valor_rojo}, verde: {valor_verde}
              """)
        
        # Guardar en archivo CSV (abrir en modo append)
        with open(filename, "a") as f:
            f.write(f"{tiempo_actual:.2f},{valor_azul},{valor_verde},{valor_amarillo},{valor_naranja},{valor_rojo}\n")
        
        contador += 1
        
        # Cada 100 muestras, sincronizar el archivo (opcional)
        if contador % 100 == 0:
            print(f"Guardadas {contador} muestras en {filename}")
            
        time.sleep(0.1)  # Espera 0.1 segundos
        
except KeyboardInterrupt:
    print(f"Programa terminado. Datos guardados en {filename}")
