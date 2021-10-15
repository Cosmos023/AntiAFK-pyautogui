import pyautogui
import time

keys = ('left','down','right','up')

time.sleep(3) #go to game window within 3 seconds

while True:
    for key in keys:
        pyautogui.keyDown(key)
        time.sleep(0.5)
        pyautogui.keyUp(key)
        