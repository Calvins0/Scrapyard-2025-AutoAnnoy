import pyautogui
import time
import pynput
import random
from pynput.mouse import Listener


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0
image_path = 'Screen Shot 2025-03-16 at 3.23.36 PM.png'
xbounce = 1
ybounce = -1
while (True):
        

        time.sleep (5)
        try:
          center = pyautogui.locateCenterOnScreen (image_path, region=(0,20, 1440, 800))
          if center.y <= 800:
            pyautogui.click(center)
            #print(pyautogui.size())
            print(f"Clicked on {image_path} at {center}")
        except:
          print(f"no worky")
          speed = 100
          p = pyautogui.position()
          x = p.x
          y = p.y
          x += speed
          if (pyautogui.onScreen(x, y) == False):
            xbounce = -1
            print(f"right")
          x -= 2*speed
          if (pyautogui.onScreen(x, y) == False):
            xbounce = 1
            print(f"left")
          x += speed
          y += speed
          if (pyautogui.onScreen(x, y) == False):
            ybounce = -1
            print(f"bottom")
          y -= 2*speed
          if (pyautogui.onScreen(x, y) == False):
            ybounce = 1
            print(f"top")
          y += speed
          print(xbounce,ybounce)
          pyautogui.move(xbounce*speed, ybounce*speed)
        # Get the center of the image
          
    
        # Click on the center of the image

        
