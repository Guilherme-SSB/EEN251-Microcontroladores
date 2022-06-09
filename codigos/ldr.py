import time

import machine


class LDR:
    def __init__(self):
        """
        Seta o pino do LDR
        """
        self.ldr = machine.ADC(27)

    def read(self) -> float:
        """
        Faz a leitura do sensor LDR e retorna o valor como float
        :return: O valor do sensor LDR como float.
        """
        return float(self.ldr.read_u16())
