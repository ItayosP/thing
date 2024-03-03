import os
import time
import pyautogui

path = "" #path

pw = input("password: ")

while pw != "סיסמה":
    pw = input("password: ")
        
else:
    if pw == "סיסמה":
        os.startfile(path)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(3)
        pyautogui.click(600, 600)
        
        time.sleep(20)
        pyautogui.click(25, 15)

