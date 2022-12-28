import pytesseract
import pyautogui
import time
import keyboard
import win32api, win32con
import pyscreenshot

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\richa\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
#place on left side of the screen
#580, 580
#1300, 700
new_word_button_x, new_word_button_y = 1050, 766
seen_word_button_x, seen_word_button_y = 847, 766
used_words = []

def click(x, y):#not using pyautogui because I think it's too slow
    win32api.SetCursorPos((x, y))#move cursor to position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)#push down
    time.sleep(0.01)#wait
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)#let go


while not keyboard.is_pressed('q'):
    img = pyscreenshot.grab(bbox=(600, 550, 1100, 700))  # with those coordinates, makes a screenshot and saves the image
    txt = pytesseract.image_to_string(img)
    if txt not in used_words:
        used_words.append(txt)
        click(new_word_button_x, new_word_button_y)
    elif txt in used_words:
        click(seen_word_button_x, seen_word_button_y)
    time.sleep(.1)