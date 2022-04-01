# Author: Jiri Svab
# screen resolution needed: width=2560, height=1440
# dependencies: Python3, PyAutogui
# notes: Taking the tasks "Move To" from HOME (alt+h) menu
# notes: Browser zoom level needs to be 100%
# notes: PyAutogui doesnt support dual monitors currently (21/10/19). 
# notes: Nevertheless it is recommended to launch this program in separate screen.

import pyautogui as pg

for x in range(9): # run throught this program x times
	pg.click(x=2340, y=446, clicks=2, interval=1, button="left") # click on country arrow in top right corner
	pg.PAUSE = 1.50 # Make a pause between each instruction
	pg.move(0, 120, 1, pg.easeInOutQuad) # Move mouse down to country
	pg.click(button="left") # Click on country
	pg.hotkey("alt", "v") # select versions
	pg.moveTo(517, 329, 1, pg.easeInOutQuad) # move mouse over Remove arrow
	pg.click(button="left") # Click on Remove arrow
	pg.moveTo(538, 356, 1, pg.easeInOutQuad) # move mouse over "Remove all versions"
	pg.click(button="left") # Click on "Remove all versions"
	pg.moveTo(1412, 939, 1, pg.easeInOutQuad) # Move mouse over "OK" msg
	pg.click(button="left") # Click on OK button
