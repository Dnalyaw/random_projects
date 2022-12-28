import pyautogui
import time
import keyboard
import win32api, win32con
#place on left side of the screen
Pos_x, Pos_y = 1400, 600

def click(x, y):#not using pyautogui because I think it's too slow
    win32api.SetCursorPos((x, y))#move cursor to position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)#push down
    time.sleep(0.01)#wait
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)#let go
    time.sleep(3)#look at the score
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # push down to refresh
    time.sleep(0.01)  # wait
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # let go

while not keyboard.is_pressed('q'):
    #print(pyautogui.pixel(Pos_x, Pos_y))
    if pyautogui.pixel(Pos_x, Pos_y)[0] == 75:#the [0] in the pixel is the r value in the rgb
        click(Pos_x, Pos_y)