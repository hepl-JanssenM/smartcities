from machine import Pin
import utime 

led = Pin(16, Pin.OUT)
BUTTON = Pin(18, Pin.IN)
val = 0
while True:
    if BUTTON.value() == 1  :
        val = val +1
        utime.sleep(1)
    elif val >= 2 :
        val = 0
        utime.sleep(1)
    led.value(val)