# Studiolab Soldering Demo Project

##  How to run everthing on you won board
- Download OS.py, programs.txt, Count_Demo.py to raspberry pi pico
- On powerup, twist pot 1 until the board displays  1 in binary.
- Press the leftmost button to choose program 1 to run (in this case Count_Demo.py)
- This should initiate the binary counting.  Twist pot 0 to change speed.  Press leftmost button to reset count.

## Changes to be made for the second board:
- Remove-up resistors from pushbuttons.
- Fix potentiometer config
- Change RGB LED to common cathode (?)
- Move side connectors so boards can be flush