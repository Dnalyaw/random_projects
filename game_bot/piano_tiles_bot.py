import pyautogui
import time
import keyboard
import win32api, win32con
from numpy import *
from PIL import ImageOps, ImageGrab

# go to https://www.agame.com/game/magic-piano-tiles, put at left side of the screen, put at full-screen

Tile_1_Pos_x, Tile_1_Pos_y = 660, 1200
Tile_2_Pos_x, Tile_2_Pos_y = 860, 1200
Tile_3_Pos_x, Tile_3_Pos_y = 1060, 1200
Tile_4_Pos_x, Tile_4_Pos_y = 1260, 1200
def start():
    win32api.SetCursorPos((960, 1160))  # move cursor to position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # push down
    time.sleep(0.01)  # wait
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # let go
def click(x, y):#not using pyautogui because I think it's too slow
    win32api.SetCursorPos((x, y))#move cursor to position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)#push down
    time.sleep(0.01)#wait
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)#let go

start()
while not keyboard.is_pressed('q'):
    if pyautogui.pixel(Tile_1_Pos_x, Tile_1_Pos_y)[0] == 0:#the [0] in the pixel is the r value in the rgb
        click(Tile_1_Pos_x, Tile_1_Pos_y)
    if pyautogui.pixel(Tile_2_Pos_x, Tile_2_Pos_y)[0] == 0:#the [0] in the pixel is the r value in the rgb
        click(Tile_2_Pos_x, Tile_2_Pos_y)
    if pyautogui.pixel(Tile_3_Pos_x, Tile_3_Pos_y)[0] == 0:#the [0] in the pixel is the r value in the rgb
        click(Tile_3_Pos_x, Tile_3_Pos_y)
    if pyautogui.pixel(Tile_4_Pos_x, Tile_4_Pos_y)[0] == 0:#the [0] in the pixel is the r value in the rgb
        click(Tile_4_Pos_x, Tile_4_Pos_y)