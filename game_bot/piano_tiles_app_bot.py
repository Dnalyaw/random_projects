import pyautogui
import time
import keyboard
import win32api, win32con
from numpy import *
from PIL import ImageOps, ImageGrab

Tile_1_Pos_x, Tile_1_Pos_y = 500, 1350
Tile_2_Pos_x, Tile_2_Pos_y = 800, 1350
Tile_3_Pos_x, Tile_3_Pos_y = 1100, 1350
Tile_4_Pos_x, Tile_4_Pos_y = 1400, 1350
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
def imageGrab(x, y):
    image = ImageGrab.grab((x, y, x+1, y+1))
    grayImage = ImageOps.grayscale(image)  # trying to get the colors
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

while not keyboard.is_pressed('q'):
#    print(pyautogui.pixel(Tile_1_Pos_x, Tile_1_Pos_y))
 #   print(pyautogui.pixel(Tile_2_Pos_x, Tile_2_Pos_y))
  #  print(pyautogui.pixel(Tile_3_Pos_x, Tile_3_Pos_y))
   # print(pyautogui.pixel(Tile_4_Pos_x, Tile_4_Pos_y))
    if pyautogui.pixel(Tile_1_Pos_x, Tile_1_Pos_y)[0] <= 200:#the [0] in the pixel is the r value in the rgb
        click(Tile_1_Pos_x, Tile_1_Pos_y)
    if pyautogui.pixel(Tile_2_Pos_x, Tile_2_Pos_y)[0] <= 200:#the [0] in the pixel is the r value in the rgb
        click(Tile_2_Pos_x, Tile_2_Pos_y)
    if pyautogui.pixel(Tile_3_Pos_x, Tile_3_Pos_y)[0] <= 200:#the [0] in the pixel is the r value in the rgb
        click(Tile_3_Pos_x, Tile_3_Pos_y)
    if pyautogui.pixel(Tile_4_Pos_x, Tile_4_Pos_y)[0] <= 200:#the [0] in the pixel is the r value in the rgb
        click(Tile_4_Pos_x, Tile_4_Pos_y)