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

board_led = Pin(25, Pin.OUT)

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

def ClearLEDs():
    for j in range(8):
        leds[j].off()

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

def WaitNoInput(BufferTime):
    while True:
        utime.sleep(0.05)
        if GetButtonInput() == 0:
            utime.sleep(BufferTime)
            if GetButtonInput() == 0:
                return 0


# -------------------------------------------

while True:
    board_led.on()
    inv_sensitivity = 1024
    searchnum = str(SelectBinary(inv_sensitivity))
    WaitNoInput(0.05)
    print(searchnum)

    f = open("programs.txt", "r")
    directory = f.read()

    i = 0
    progname = ""
    prognum = ""
    while i < len(directory):
        if directory[i] == ":":
            i += 1
            while directory[i] != "*" and i < len(directory):
                prognum += directory[i]
                i += 1
            if searchnum == prognum:
                break
            else:
                i += 3
                progname = ""
        prognum = ""
        progname += directory[i]
        i += 1
    
    print(progname)
    
    board_led.off()
    program_to_run = __import__(progname)
