from machine import Pin
import time

ledv = Pin(4, Pin.OUT)
leda = Pin(0, Pin.OUT)
ledve = Pin(2, Pin.OUT)

while True:
    #led vermelho
    ledv.value(1)
    time.sleep(1)
    ledv.value(0)

    #led amarelo
    leda.value(1)
    time.sleep(1)
    leda.value(0)

    #led verde
    ledve.value(1)
    time.sleep(1)
    ledve.value(0)
    time.sleep(1)

#INSTRUÇÕES
#Foram utilizados: 3 LEDS(vermelho, verde e amarelo), 1 ESFP32, 3 resistores de 220V e jumpers para as conexões
#Simulação feita no WOWKI
