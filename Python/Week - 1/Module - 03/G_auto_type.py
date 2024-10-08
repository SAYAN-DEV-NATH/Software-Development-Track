import pyautogui
from time import *

sleep(5)
for i in range(0, 20):
    pyautogui.write("How are you", interval=0)
    pyautogui.press("enter")
