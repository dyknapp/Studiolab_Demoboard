from machine import UART, Pin
import time

leds = [0, 1, 2, 3, 4, 5, 6, 7]
for x in range(len(leds)):
    leds[x] = Pin(x, Pin.OUT)

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart0 = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

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

rxData = bytes()
while True:
    rxData = uart0.readline()
    print(rxData.decode('utf-8'))
    size = len(rxData)
    result = int(rxData[:size])
    BinaryDisplay(result, 0)
    rxData = bytes()