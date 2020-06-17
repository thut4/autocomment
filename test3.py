import pyautogui                    #pip install pyautogui
import time
#comment=["hi","hello","helooo","nooob","aaa"]  #also can be used by this line
comment="i love you"
time.sleep(3)
for i in range(15):             #you can loop whatever you like
    #pytogui.typewrite(comment[i%7])
    pyautogui.typewrite(comment)
    pyautogui.typewrite("\n")
    time.sleep(1)

