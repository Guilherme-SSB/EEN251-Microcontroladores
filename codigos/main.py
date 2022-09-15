from oled import OLED
from dth11 import DTH22
from buzzer import BUZZER
from ldr import LDR
from time import sleep_ms
from mq2 import MQ2
import json

def main():
    meu_dth22 = DTH22()
    meu_buzzer = BUZZER()
    meu_ldr = LDR()
    meu_oled = OLED()
    meu_mq2 = MQ2(pinData = 26, baseVoltage = 3.3)
    print("Calibrando")
    meu_mq2.calibrate()
    print("Calibração completa")
    print("Resistência base:{0}".format(meu_mq2._ro))
    
    meu_oled.limpar()
    # song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]
    song_ldr = ["E5","G5","A5"]
    song_mq2 = ["G5","C5","G5","C5"]
    
    while True:
        #meu_oled.exibir(str(meu_dth22.medirTemp()), 2,15)
        #meu_oled.exibir(str(meu_dth22.medirUmidade()), 5, 35)
        
        # try:
        temp = float(meu_dth22.medirTemp())
        sleep_ms(2000)
        umidade = meu_dth22.medirUmidade()
        
        ldr = float(meu_ldr.read())
        fumaca = round(float(meu_mq2.readSmoke()),1)
        #print('Temperatura: ', temp, end=' ')
        #print(' - Umidade: ', umidade, end=' ')
        #print(" - LDR: {:.1f}".format(meu_ldr.read()), end='')
        #print(" - Fumaça: {:.1f}".format(meu_mq2.readSmoke()))
        
        saida = {"Temperatura":temp, "Umidade":umidade, "LDR": ldr, "Fumaca": fumaca}
        saida2 = json.dumps(saida)
        print(saida2)
        
        
        if meu_ldr.read() <= 10000:
           meu_buzzer.playsong(song_ldr)
        
        if meu_mq2.readSmoke() > 25:
            meu_buzzer.playsong(song_mq2)
        
        sleep_ms(50)

if __name__ == "__main__":
    main()
