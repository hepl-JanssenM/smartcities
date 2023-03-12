from machine import Pin
import utime
led = Pin(16, Pin.OUT)

while True:
    utime.sleep_ms(500)
    led.toggle()
    