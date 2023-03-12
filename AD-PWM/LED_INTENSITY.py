from machine import ADC, Pin, PWM
from utime import sleep

ROTARY_ANGLE_SENSOR = ADC(0)
led_PWM = PWM(Pin(18))

led_PWM.freq(500)

while True :
    val = ROTARY_ANGLE_SENSOR.read_u16()
    led_PWM.duty_u16(val)