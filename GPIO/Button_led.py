from machine import Pin
import utime
led = Pin(16, Pin.OUT)
BUTTON = Pin(18, Pin.IN)

while True:
    val = BUTTON.value()
    if val :
        led.value(1)
    else:
        led.value(0)
    