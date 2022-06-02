from machine import Pin, SPI
from ssd1306 import SSD1306_SPI
import framebuf
from time import sleep
from utime import sleep_ms

class OLED:
    def __init__(self):
        spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
        self.oled = SSD1306_SPI(128, 64, spi, Pin(17),Pin(20), Pin(16))
    def exibir(self,value,posx,posy):
        #oled = SSD1306_SPI(WIDTH, HEIGHT, spi, dc,rst, cs) use GPIO PIN NUMBERS
        
        #sleep(1)
        self.oled.text(value,posx,posy)
        self.oled.show()
        sleep_ms(100)
    def limpar(self):
        self.oled.fill(0)
        self.oled.show()
            
