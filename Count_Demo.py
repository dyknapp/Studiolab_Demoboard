"""
4/6
Basic demo for the board: binary counting with variable
    speed using pot 0
"""

#### IMPORT ############################################

from machine import Pin, ADC
from random import randint
import utime


#### VARIABLES AND FUNCTIONS ###########################

leds = [0, 1, 2, 3, 4, 5, 6, 7]
for x in range(len(leds)):
    leds[x] = Pin(x, Pin.OUT)

rgbs = [18, 19, 20]
for x in range(len(rgbs)):
    rgbs[x] = Pin(rgbs[x], Pin.OUT)
    
buttons = [12, 13, 14, 15]
for x in range(len(buttons)):
    buttons[x] = Pin(buttons[x], Pin.IN, Pin.PULL_UP)

pot0 = ADC(26)
pot1 = ADC(27)


# -------------------------------------------
    
def BinaryDisplay(num, its):
    #clear
    for x in range(8):
        leds[x].off()
    if num >= 1:
        BinaryDisplay(num // 2, its + 1)
    if num % 2 == 1:
        leds[7 - its].on()
    else:
        leds[7 - its].off()
             
        
##### LOOP #############################################        

while True:

# LED Test ----------------------------    
    for step in range(255):
        BinaryDisplay(step,0)
        speedFactor = 1 - (pot0.read_u16() / 65535)
        utime.sleep(0.5 * (speedFactor + 0.1))
        print(step)
        
        if not buttons[0].value():
            break
                  
    
# Button Test -------------------------
#     for x in range(len(buttons)):
#         print(buttons[x].value())
#     utime.sleep(.25)
                  

# RGB Test ----------------------------
#     rgbs[randint(0, 2)].toggle()
#     utime.sleep(1)
                  

# Pots Test ---------------------------
#     print(pot0.read_u16())
#     print(pot1.read_u16())
#     utime.sleep(0.2)


#######################################################
