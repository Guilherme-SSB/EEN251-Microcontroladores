import dht
import machine
from time import sleep_ms

class DTH22:
    def __init__(self):
        SENSOR_PIN = 28
        self.sensor = dht.DHT22(machine.Pin(SENSOR_PIN, machine.Pin.IN, machine.Pin.PULL_UP))

    def medirTemp(self) -> str:
        self.sensor.measure()
        sleep_ms(100)
        # temperatura = "Temp: " + str(self.sensor.temperature()) + "C"
        temperatura = str(self.sensor.temperature())
        
        return temperatura
    
    def medirUmidade(self) -> str:
        self.sensor.measure()
        # umidade = "Umidade: " + str(self.sensor.humidity()) + "%"
        umidade = self.sensor.humidity()
        return umidade

#dht = DTH22()
#temp = dht.medirUmidade()
#print(temp)
