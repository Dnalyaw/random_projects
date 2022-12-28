import time

from pynput.keyboard import Controller, Key, Listener
from pynput import mouse
import pyscreenshot
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\richa\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
def on_click(x, y, button, pressed):#on mouse click
    if pressed:
        on_click.px = x#records the press of the mouse
        on_click.py = y
    else:
        on_click.rx = x#records the release of the mouse
        on_click.ry = y
    if not pressed:
        return False

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

img = pyscreenshot.grab(bbox=(on_click.px, on_click.py, on_click.rx, on_click.ry))#with those coordinates, makes a screenshot and saves the image
txt = pytesseract.image_to_string(img).replace('|', 'I')#pytesseract converts image to string
txt = ' '.join(txt.splitlines())
print(txt)

keyboard = Controller()

def on_press(key):
    if key == Key.num_lock:#i used number lock as access key
        for i in txt:#for every letter in the string
            keyboard.press(i)#press that letter
            keyboard.release(i)#release that press
            time.sleep(0.01)#wait .1 seconds

with Listener(on_press=on_press) as listener:
    listener.join()