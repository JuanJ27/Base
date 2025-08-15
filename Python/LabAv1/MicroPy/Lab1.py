import network
import socket
import time
from machine import Pin, I2C
import dht


#Configurar sensores
dht_sensor = dht.DHT22(Pin(4))
i2c = I2C(0, scl = Pin(22), sda = Pin(21))

# Conexion wifi
ssid = 'jjRedmi'
password = '12345678'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print('Conectado a wifi:', station.ifconfig())

