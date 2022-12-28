import time

from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *

#Note to me: go to http://www.trex-game.skipser.com/ to test this out, also place this on the left hand of the screen

class Coordinates():
    replayBtn = (961, 680)
    dinosaur = (650, 680)
def restartGame():
    pyautogui.click(Coordinates.replayBtn)#clicks the correct coordinates from replay btn
    pyautogui.keyDown('down')

def pressSpace(jumpCount):
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')#pushes key down
    time.sleep(jumpCount)#waits 0.05 seconds
    pyautogui.keyUp('space')#lets it go
    pyautogui.keyDown('down')
def imageGrab(reaction):
    box = (Coordinates.dinosaur[0] + 130, Coordinates.dinosaur[1], Coordinates.dinosaur[0] + reaction, Coordinates.dinosaur[1] + 30)
    image = ImageGrab.grab(box)#area to see to know when to jump
    grayImage = ImageOps.grayscale(image)#trying to get the colors
    a = array(grayImage.getcolors())
    return a.sum()

def main():
    jumpCount = 0.25
    reaction = 210
    restartGame()
    time.sleep(1)
    while True:
        if imageGrab(reaction) > 3247:
            pressSpace(jumpCount)
            if reaction < 230:
                reaction += 0.5
            else:
                reaction = 230

            if jumpCount > 0.01:
                jumpCount -= .005

main()