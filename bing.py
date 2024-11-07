import pyautogui as py
import time
time.sleep(2)
for i in range(34):
    py.hotkey('ctrl','e')
    py.write(str(i))
    py.press('enter')
    time.sleep(3)