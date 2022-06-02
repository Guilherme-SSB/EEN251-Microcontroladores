from oled import OLED
from dth11 import DTH22
from time import sleep_ms
if __name__ == "__main__":
    meu_dth22 = DTH22()
    meu_oled = OLED()
    meu_oled.limpar()
    while True:
        meu_oled.exibir(str(meu_dth22.medirTemp()), 2,15)
        meu_oled.exibir(str(meu_dth22.medirUmidade()), 5, 35)
        sleep_ms(5000)
