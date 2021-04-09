# Studiolab Soldering Demo Project

##  How to run everthing on your own board
- Download OS.py, programs.txt, Count_Demo.py to raspberry pi pico
- On powerup, twist pot 1 until the board displays  1 in binary.
- Press the leftmost button to choose program 1 to run (in this case Count_Demo.py)
- This should initiate the binary counting.  Twist pot 0 to change speed.  Press leftmost button to reset count.

## Changes to be made for the second board:
- Remove-up resistors from pushbuttons.
- Fix potentiometer config
- Change RGB LED to common cathode (?)
- Move side connectors so boards can be flush - female-female only
- Photosensor
- Rubber feet at each corner - silkscreen circles on back

## Program 1: bTest.py
Original test program

## Program 1: Binary Counter (Count_Demo.py)
Twist pot 0 to change speed.  Press leftmost button to reset count.

## Program 2: RGB Color Selector (RGBcolors.py)
Use pot 0 to select the brightnesses of red, green, and blue components.  Press leftmost button to select the setting for each color.  After the three magnitudes are selected, the RGB LED will disply the resultant color.  Press leftmost button to select another color.

## Program 3: UART sending demo
Sends the value of the potentiometer binary setting from both connections.

## Program 4: UART receiving demo
Receives data on UART0 (right hand connector) and displays on LEDs.
