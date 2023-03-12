from machine import ADC, Pin
from utime import sleep

ROTARY_ANGLE_SENSOR = ADC(0)
led = Pin("LED",Pin.OUT)

while True :
    print(ROTARY_ANGLE_SENSOR.read_u16())
    if ROTARY_ANGLE_SENSOR.read_u16() > 30000 :
        led.value(1)
        sleep(1)
        print("test")
    else:
        led.value(0)
        sleep(1)