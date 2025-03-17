import pyautogui
import time
import pynput
import math
from pynput.mouse import Listener
pyautogui.PAUSE = 0

time.sleep(5)
p = pyautogui.position()
x = p.x
y = p.y
i = 0
for i in range(0, 360, 2):
    xf = x + (200 * math.cos(math.radians(i)))
    yf = y + (200 * math.sin(math.radians(i)))
    pyautogui.moveTo(xf, yf, 0)
    pyautogui.mouseDown(button='left')
pyautogui.mouseUp(button='left')
