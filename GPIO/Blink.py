from machine import Pin
import utime
led = Pin("LED", Pin.OUT)
while True:
    utime.sleep_ms(500)
    led.toggle()
    