from machine import UART, Pin, ADC
import utime

leds = [0, 1, 2, 3, 4, 5, 6, 7]
for x in range(len(leds)):
    leds[x] = Pin(x, Pin.OUT)

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart0 = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

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

setting = 0
inv_sensitivity = 256
while True:
    board_led.on()
    utime.sleep(0.05)
    board_led.off()
    prevsetting = setting
    setting = pot0.read_u16()
    if abs(setting - prevsetting) > inv_sensitivity / 4:
        BinaryDisplay(round(setting / inv_sensitivity), 0)
    
    txData = bytes(str(round(setting / inv_sensitivity)), 'utf-8')
    uart0.write(txData + b'\n')
    uart1.write(txData + b'\n')