#Teste da biblitoeca do Micropython para utilizar o DHT11(Azul)
import dht
import machine
from time import sleep_ms
class DTH22:
        def __init__(self):
            SENSOR_PIN = 28
            self.sensor = dht.DHT22(machine.Pin(SENSOR_PIN, machine.Pin.IN, machine.Pin.PULL_UP))

        def medirTemp(self):
            self.sensor.measure()
            sleep_ms(100)
            temperatura = "Temp: " + str(self.sensor.temperature()) + "C"
            return temperatura
        
        def medirUmidade(self):
            self.sensor.measure()
            umidade = "Umidade: " + str(self.sensor.humidity()) + "%"
            return umidade
