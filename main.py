import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui
from time import sleep

while True:
    base_screen = ImageGrab.grab(bbox=(310, 620, 370, 1000))
    base_screen.save('D:/bot/base_screen.png')

    img_rgb = cv2.imread('base_screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('1.png', 0)
    template2 = cv2.imread('2.png', 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res>=0.9)

    for pt in zip(*loc[::-1]):
        pyautogui.moveTo(200,300)
        sleep(0.1)
        pyautogui.leftClick()
        sleep(0.1)
        
        pyautogui.middleClick()
        sleep(0.1)

        pyautogui.moveTo(1480,147) #координаты встать в разгон док
        sleep(0.1)
        pyautogui.leftClick()
        sleep(12)

        pyautogui.moveTo(1545,147) #координаты входа в док
        sleep(0.1)
        pyautogui.leftClick()
        
        sleep(1)

        pyautogui.moveTo(1545,147) #координаты входа в док
        sleep(0.1)
        pyautogui.leftClick()
        exit()
    
    res = cv2.matchTemplate(img_gray, template2, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res>=0.9)

    for pt in zip(*loc[::-1]):
        pyautogui.moveTo(200,300)
        sleep(0.1)
        pyautogui.leftClick()
        sleep(0.1)
        
        pyautogui.middleClick()
        sleep(0.1)

        pyautogui.moveTo(1480,147) #координаты встать в разгон док
        sleep(0.1)
        pyautogui.leftClick()
        sleep(12)

        pyautogui.moveTo(1545,147) #координаты входа в док
        sleep(0.1)
        pyautogui.leftClick()
        
        sleep(1)

        pyautogui.moveTo(1545,147) #координаты входа в док
        sleep(0.1)
        pyautogui.leftClick()
        exit()
    sleep(1)

    
