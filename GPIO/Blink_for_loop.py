from machine import Pin
import utime
led = Pin("LED", Pin.OUT)

for i in range(10) :
    utime.sleep_ms(500)
    led.toggle()
    