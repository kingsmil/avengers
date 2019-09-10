import pyautogui
import random
import time
import os
from PIL import ImageGrab
#run in python3 
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1
x, y = pyautogui.position()
#mouse position debugger
while True:
  a_mp = input("get mouse position?")
  if(a_mp == "n"):
   break
  x, y = pyautogui.position()
  print(x,y)
#color debugger
im = pyautogui.screenshot()
while True:
  a_clr = input("what is this color?")
  if (a_clr == "n"):
    break
  x, y = pyautogui.position()
  r,g,b = im.getpixel((x,y))
  print(r,g,b)

   
#cytec padometer
# pyautogui.moveTo(0,200)
# pyautogui.click()
# while True:
 # pyautogui.dragRel(2,0)
 # pyautogui.dragRel(0,random.randrange(-10,10))
 # print("help la")
 # time.sleep(5)

#cytec ghost summoning ritual
# while True:
# pyautogui.moveTo(random.randrange(1600), random.randrange(900), duration=0.25)
# pyautogui.moveTo(random.randrange(1600), random.randrange(900), duration=0.25)
# pyautogui.moveTo(random.randrange(1600), random.randrange(900), duration=0.25)
# pyautogui.moveTo(random.randrange(1600), random.randrange(900), duration=0.25)
# pyautogui.position()
# pyautogui.moveRel(0, -100, duration=0.25)