#Plant Waterer Helper---------------
from machine import Pin, PWM, ADC
import time

ena = PWM(Pin(0))
in1 = Pin(1, Pin.OUT)

adc = ADC(26)

ena.freq(15000)
ena.duty_u16(60000)

motorValue = ""

while True:
    moistMeter = adc.read_u16()
    if(moistMeter > 18000):
        in1.value(1)
        motorValue = "ON"
    elif(moistMeter < 16500):
        in1.value(0)
        motorValue = "OFF"
    print(moistMeter, " ", motorValue)    
    
    # > 20600 Dry in Air
    #16500 good number for moistness??? 
    # < 11650 in water
    time.sleep(0.5)
    
    
    
