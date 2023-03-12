from machine import ADC, Pin, PWM
import utime 

led_PWM = PWM(Pin(18))

led_PWM.freq(500)
val = 0
while True :
    while val < 65535 :
        val = val +50
        utime.sleep_ms(1)
        led_PWM.duty_u16(val)
    while val > 0 :
        val = val - 50
        utime.sleep_ms(1)
        led_PWM.duty_u16(val)