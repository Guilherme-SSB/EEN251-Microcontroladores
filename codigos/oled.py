from time import sleep

import framebuf
from machine import SPI, Pin
from utime import sleep_ms

from ssd1306 import SSD1306_SPI


class OLED:
    def __init__(self):
        """
        Inicializa o SPI e o display OLED
        """
        spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
        self.oled = SSD1306_SPI(128, 64, spi, Pin(17), Pin(20), Pin(16))

    def exibir(self, value, posx, posy) -> None:
        """
        Exibe o valor da variável "value" na posição (posx, posy) na tela
        
        :param value: O texto a ser exibido
        :param posx: Posição x
        :param posy: Posição y
        """
        self.oled.text(value, posx, posy)
        self.oled.show()
        sleep_ms(100)

    def limpar(self) -> None:
        """
        Limpa a tela
        """
        self.oled.fill(0)
        self.oled.show()
