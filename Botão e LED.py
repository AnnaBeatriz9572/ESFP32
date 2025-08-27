from machine import Pin
import time

led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)
