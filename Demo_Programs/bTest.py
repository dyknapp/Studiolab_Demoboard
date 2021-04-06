"""
3/26
- Pico supports internal pullup/down resistors for digital input reading. Remove resistors.
- "for x in buttons" doesn't work. it should
"""
​
#### IMPORT ############################################
​
from machine import Pin, ADC
from random import randint
import utime
​
​
#### VARIABLES AND FUNCTIONS ###########################
​
# leds = [0, 1, 2, 3, 4, 5, 6, 7]
# for x in range(len(leds)):
#     leds[x] = Pin(x, Pin.OUT)
​
# rgbs = [18, 19, 20]
# for x in range(len(rgbs)):
#     rgbs[x] = Pin(rgbs[x], Pin.OUT)
    
# buttons = [12, 13, 14, 15]
# for x in range(len(buttons)):
#     buttons[x] = Pin(buttons[x], Pin.IN, Pin.PULL_UP)
​
# pot0 = ADC(26)
# pot1 = ADC(27)
​
​
# -------------------------------------------
    
# def binary_count(step):
#     for x in range(8):
#         if (step % 2**(x+1)) >= (2**x)-1:
#             leds[x].on()
#         else:
#             leds[x].off()
             
        
##### LOOP #############################################        
​
while True:
​
# LED Test ----------------------------    
#     for step in range(255):
#         binary_count(step)
#         utime.sleep(0.2)
#         print(step)
                  
    
# Button Test -------------------------
#     for x in range(len(buttons)):
#         print(buttons[x].value())
#     utime.sleep(.25)
                  
​
# RGB Test ----------------------------
#     rgbs[randint(0, 2)].toggle()
#     utime.sleep(1)
                  
​
# Pots Test ---------------------------
#     print(pot0.read_u16())
#     print(pot1.read_u16())
#     utime.sleep(0.2)
​
​
#######################################################