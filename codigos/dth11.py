from time import sleep_ms

import dht
import machine


class DTH22:
    def __init__(self):
        """
        Seta o pino do DTH22
        """
        SENSOR_PIN = 28
        self.sensor = dht.DHT22(machine.Pin(
            SENSOR_PIN, machine.Pin.IN, machine.Pin.PULL_UP))

    def medirTemp(self) -> str:
        """
        Lê a temperatura do sensor e retorna uma string com a temperatura
        :return: The temperature in Celsius.
        """
        self.sensor.measure()
        sleep_ms(100)
        temperatura = "Temp: " + str(self.sensor.temperature()) + "C"
        return temperatura

    def medirUmidade(self) -> str:
        """
        Lê a umidade do sensor e retorna uma string com o valor
        """
        self.sensor.measure()
        umidade = "Umidade: " + str(self.sensor.humidity()) + "%"
        return umidade
