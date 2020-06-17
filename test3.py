import pyautogui                    #pip install pyautogui
import time
#comment=["hi","hello","helooo","nooob","aaa"] 
comment="i love you"
time.sleep(3)
for i in range(15):
    pyautogui.typewrite(comment)
    pyautogui.typewrite("\n")
    time.sleep(1)

