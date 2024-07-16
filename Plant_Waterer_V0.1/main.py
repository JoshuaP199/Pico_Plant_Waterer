#Plant Waterer Helper---------------
from machine import Pin, PWM, ADC
import time

ena = PWM(Pin(0))
in1 = Pin(1, Pin.OUT)

adc = ADC(26)

ena.freq(15000)
ena.duty_u16(60000)

motorValue = ""
timer = 0

while True:
    moistMeter = adc.read_u16()
    if(moistMeter > 18000):
        #Timer to prevent overflow
        #if(timer == 2):
        #   in1.value(0)
        #   timer = 0
        #    print("T-OFF")
        #    time.sleep(1)
        in1.value(1)
        motorValue = "ON"
        #timer+= 0.5
    elif(moistMeter < 16500):
        in1.value(0)
        motorValue = "OFF"
    print(moistMeter, " ", motorValue, " ", timer)
    #Get moisture meter
    #Once moisture hits a dry reading
    #Water Plant
    #Have tube pour onto bottom of plant.
    #once moisture hits good reading
    #Stop Watering
    #Since this is Pico W try to look into blutooth for sending reading? Would I need to make an app for that?
    
    
    # >20600 Dry in Air
    #20300 < moist < 20600
    #16500 good number for moistness??? 
    # > 11650 in water
    time.sleep(0.5)
    
    
    