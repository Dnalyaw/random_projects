from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#C:/Users/richa/PycharmProjects/random_projects/game_bot/image_detection/

run = True
while run:
    if pyautogui.locateOnScreen('stickman.png', confidence=0.8) is not None: #if the pyautogui cant find the stickman on the screen, it enters None
        print("I can see it")#confidence is used because the pyautogui wants to find 100%, but the pixels are sometimes off, so 80%
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
