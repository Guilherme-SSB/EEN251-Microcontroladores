from time import sleep_ms

from buzzer import BUZZER
from dth11 import DTH22
from ldr import LDR
from mq2 import MQ2
from oled import OLED


def main():

    # Instancia todos os sensores utilizados
    meu_dth22 = DTH22()
    meu_buzzer = BUZZER()
    meu_ldr = LDR()
    meu_oled = OLED()
    meu_mq2 = MQ2(pinData = 26, baseVoltage = 3.3)

    # Calibra o sensor de gás
    print("Calibrando")
    meu_mq2.calibrate()
    print("Calibragem finalizada")
    print("Resistência base:{0}".format(meu_mq2._ro))
    
    # Limpa o display OLED
    meu_oled.limpar()

    # Variáveis de som, que serão utilizadas em situações aqui consideradas críticas
    song_ldr = ["E5","G5","A5"]
    song_mq2 = ["G5","C5","G5","C5"]
    
    # Loop infinito
    while True:
        # Leitura da temperatura e da umidade e exibição na tela
        meu_oled.exibir(str(meu_dth22.medirTemp()), 2,15)
        meu_oled.exibir(str(meu_dth22.medirUmidade()), 5, 35)
        
        # Leitura do sensor de luz e de fumaça e print no terminal
        print("LDR: {:.1f}".format(meu_ldr.read())+" - ", end='')
        print("Fumaça: {:.1f} ppm".format(meu_mq2.readSmoke()))
        
        # Se o sensor de luz estiver abaixo do limite (10000), toca o buzzer
        if meu_ldr.read() <= 10000:
           meu_buzzer.playsong(song_ldr)
        
        # Se o sensor de fumaça estiver acima do limite (25), toca o buzzer
        if meu_mq2.readSmoke() > 25:
            meu_buzzer.playsong(song_mq2)
        
        sleep_ms(50)

if __name__ == "__main__":
    main()

