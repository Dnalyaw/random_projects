from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con



def click(x, y):#not using pyautogui because I think it's too slow
    win32api.SetCursorPos((x, y))#move cursor to position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)#push down
    time.sleep(0.01)#wait
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)#let go

#Color of center: (255, 255, 255)
shot_count = 0
time.sleep(3)
click(933, 660)
while not keyboard.is_pressed('q') or shot_count >= 30:
    pic = pyautogui.screenshot(region=(132, 327, 1820, 965))#takes screenshot of region
    width, height = pic.size#saves the width and height
    shot_count += 1
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x,y))#getting color for every 5 pixels

            if b == 255:
                click(x+132, y+327)
                time.sleep(0.05)
                break#so it doesnt click the same places multiple times