from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(27))
vol = 1000
def DO(time):
    buzzer.freq(1046)
    buzzer.duty_u16(vol)
    sleep(time)
def RE(time):
    buzzer.freq(1175)
    buzzer.duty_u16(vol)
    sleep(time)
def MI(time):
    buzzer.freq(1318)
    buzzer.duty_u16(vol)
    sleep(time)
def FA(time):
    buzzer.freq(1397)
    buzzer.duty_u16(vol)
    sleep(time)
def SOL(time):
    buzzer.freq(1568)
    buzzer.duty_u16(vol)
    sleep(time)
def LA(time):
    buzzer.freq(1760)
    buzzer.duty_u16(vol)
    sleep(time)
def SI(time):
    buzzer.freq(1967)
    buzzer.duty_u16(vol)
    sleep(time)
def N(time):
    buzzer.duty_u16(0)
    sleep(time)
while True:
    SI(0.5)
    SI(0.5)
    DO(0.5)
    RE(0.5)
    RE(0.5)
    DO(0.5)
    SI(0.5)
    LA(0.5)
    SOL(0.5)
    SOL(0.5)
    LA(0.5)
    SI(0.5)
    SI(0.5)
    LA(0.5)
    LA(0.5)
    SI(0.5)
    SI(0.5)
    DO(0.5)
    RE(0.5)
    RE(0.5)
    DO(0.5)
    SI(0.5)
    LA(0.5)
    SOL(0.5)
    SOL(0.5)
    LA(0.5)
    SI(0.5)
    LA(0.5)
    SOL(0.5)
    SOL(0.5)
    LA(0.5)
    LA(0.5)
    SI(0.5)
    SOL(0.5)
    LA(0.5)
    SI(0.5)
    DO(0.5)
    SI(0.5)
    SOL(0.5)
    LA(0.5)
    SI(0.5)
    DO(0.5)
    SI(0.5)
    LA(0.5)
    SOL(0.5)
    LA(0.5)
    RE(0.5)

    
    

    