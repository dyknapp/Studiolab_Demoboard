#### IMPORT ############################################

from machine import Pin, ADC, PWM
from random import randint
import utime


#### VARIABLES AND FUNCTIONS ###########################

leds = [0, 1, 2, 3, 4, 5, 6, 7]
for x in range(len(leds)):
    leds[x] = Pin(x, Pin.OUT)

rgbs = [18, 19, 20]
for x in range(len(rgbs)):
    rgbs[x] = PWM(Pin(rgbs[x]))
    rgbs[x].freq(1760)
    
buttons = [12, 13, 14, 15]
for x in range(len(buttons)):
    buttons[x] = Pin(buttons[x], Pin.IN, Pin.PULL_UP)

pot0 = ADC(26)
pot1 = ADC(27)

board_led = Pin(25, Pin.OUT)

def ClearLEDs():
    for j in range(8):
        leds[j].off()

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

def SelectBinary(inv_sensitivity):
    setting = 0
    while True:
        utime.sleep(0.05)
        prevsetting = setting
        setting = pot0.read_u16()
        if abs(setting - prevsetting) > inv_sensitivity / 4:
            BinaryDisplay(round(setting / inv_sensitivity), 0)
        
        if not buttons[0].value():
            return round(setting / inv_sensitivity)

def GetButtonInput():
    input = (15 - int(buttons[3].value())\
                        - 2 * int(buttons[2].value())\
                        - 4 * int(buttons[1].value())\
                        - 8 * int(buttons[0].value()))
    return input

def CountDownInput(CountTime):
    button_input = 0
    RemainedTheSame = 0
    prev_input = GetButtonInput()
    while True:
        for j in range(8):
            leds[j].off()
        utime.sleep(CountTime/8)
        prev_input = button_input
        while button_input == 0:
            GetButtonInput()
            utime.sleep(CountTime/8)
            
        if button_input == prev_input:
            RemainedTheSame = 1
            for j in range(8):
                leds[j].on()
                utime.sleep(CountTime/8)
                GetButtonInput()
                if button_input != prev_input:
                    RemainedTheSame = 0
                    break
                    
        if RemainedTheSame == 1:
            for j in range(8):
                leds[j].off()
            return button_input

def DisplayRGB(r, g, b):
    for j in range(3):
        rgbs[j].duty_u16(0)
    # RGB 0 to 65025
    rgbs[0].duty_u16(round(65025 * g))
    rgbs[1].duty_u16(round(65025 * b))
    rgbs[2].duty_u16(round(65025 * r))

def WaitNoInput(BufferTime):
    while True:
        utime.sleep(0.05)
        if GetButtonInput() == 0:
            utime.sleep(BufferTime)
            if GetButtonInput() == 0:
                return 0



def SelectColor():
    DisplayRGB(1, 0, 0)
    Red = SelectBinary(256*16)
    WaitNoInput(0.05)
    DisplayRGB(0, 1, 0)
    Green = SelectBinary(256*16)
    WaitNoInput(0.05)
    DisplayRGB(0, 0, 1)
    Blue = SelectBinary(256*16)
    WaitNoInput(0.05)
    ClearLEDs()
    DisplayRGB(Red / 16., Green / 16., Blue / 16.)
    
while True:
    SelectColor()
    while True:
        if GetButtonInput() == 8:
            WaitNoInput(0.05)
            break