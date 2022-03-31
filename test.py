import pyautogui
import time
import random
time.sleep(3)
a=random.randint(60,80)
b=random.randint(930,1000)
c= random.uniform(0.2,0.5)
d= random.randint(825,855)
i=random.randint(0,1440)
j=random.randint(0,900)
while(1):
    for i in range(2):
        time.sleep(a)
        pyautogui.moveTo(i, j, duration=c)
        pyautogui.scroll(-300)
    pyautogui.scroll(-3300)
    pyautogui.moveTo(b, d, duration=c)
    pyautogui.click(button='left')
