import pyautogui
import time
import keyboard
pyautogui.FAILSAFE = False
x = True
while x:
    time.sleep(3)
    for i in range(0, 100):
        if keyboard.is_pressed('q'):
            x=False
            break
        pyautogui.moveTo(0, i * 5)
    for i in range(0, 3): 
        if keyboard.is_pressed('q'):
            x=False
            break
        pyautogui.press('shift')
    