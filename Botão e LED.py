from machine import Pin
import time

led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)

#INSTRUÇÕES:
# Foi utilizado: 1 ESFP32, 1 resistor de 220V para o LED vermelho, um botão, uma miniboard e jumpers para as conexões.
