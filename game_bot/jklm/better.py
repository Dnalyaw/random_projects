import cv2
import numpy as np
import time
import pytesseract
from PIL import ImageGrab
import keyboard
from urllib.request import urlopen
import win32api, win32con


filepath_words = urlopen("https://raw.githubusercontent.com/BasilPanda/bombpartysolver/master/dict/dict.txt")
Tile_1_Pos_x, Tile_1_Pos_y = 735, 2049
Tile_2_Pos_x, Tile_2_Pos_y = 350, 1350
input_coords = [735, 2049, 736, 2050]
letter_coords = [683, 1118, 786, 1153]
bomb_coords = [683, 1118, 786, 1153]
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\richa\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
all_words = []



def main():
    used = []
    # temp = 0
    while True:
        cap_input_box = np.array(ImageGrab.grab(bbox=input_coords))
        cap_input_box = cv2.cvtColor(cap_input_box, cv2.COLOR_BGR2GRAY)
        cap_letters = np.array(ImageGrab.grab(bbox=letter_coords))
        cap_letters = cv2.cvtColor(cap_letters, cv2.COLOR_BGR2GRAY)
        cap_bomb = np.array(ImageGrab.grab(bbox=bomb_coords))
        cap_bomb = cv2.cvtColor(cap_bomb, cv2.COLOR_BGR2GRAY)
        # 20 is when it's current turn to input

        if cap_input_box[0][0] == 21:
            time.sleep(1)
            # run function
            text = pytesseract.image_to_string(cap_bomb)
            imagem = cv2.bitwise_not(cap_bomb)
            #thresh = cv2.threshold(cap_bomb, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

            # thresh = cv2.GaussianBlur(thresh, (3, 3), 0)
            data = pytesseract.image_to_string(imagem, lang='eng', config='-c tessedit_char_whitelist'
                                                                          '=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 7 ')
            if "1" in data:
                data.replace("1", "i")
            if len(data) == 1:
                data += "I"
            letters = data.rstrip()
            print(letters)

            # if 20 >= cap_input_box[750 - input_coords[0], 1380 - input_coords[1]]:
                # print(f"Int: {cap_input_box[750 - input_coords[0], 1380 - input_coords[1]]}")
                # temp = cap_input_box[750 - input_coords[0], 1380 - input_coords[1]]
            valid = getValid(letters)

            # Get the best word possible that isn't already used
            best = findLongestUnique(valid, used)

            used.append(best)

            print(best)
            #

            #win32api.SetCursorPos((Tile_2_Pos_x,Tile_2_Pos_y))  # move cursor to position
            click(Tile_2_Pos_x, Tile_2_Pos_y)
            time.sleep(0.01)
            keyboard.write(str(best)[2:len(best)-1], delay=False)
            #slowType(str(best)[2:len(best)-1])
            time.sleep(.1)

            keyboard.press_and_release('enter')
            # text = pytesseract.image_to_string(cap_letters)
            # print(text)

            # Shows the capture of the bomb
            cv2.imshow("imagem", imagem)
            # Wait
            time.sleep(1)

        if cv2.waitKey(1) == 27:
            break
        # 1440p monitor
        # input box
        # x736 y1371
        # x1455 y1414

        # letters on right
        # x2059 y197
        # x2181 y1339

        # words in middle
        # x1057 y759
        # x1123 y803
    cv2.destroyAllWindows()


def loadWords(r):
    for line in r:
        all_words.append(str(line[:len(line) - 1]))


def getValid(letters):
    valid = []
    for word in all_words:
        if letters in word:
            valid.append(word)
    return valid


def findLongestUnique(words, used):
    longest = ""
    for word in words:
        if word in used:
            continue
        if len(set(word)) > len(set(longest)):
            longest = word
            used.append(word)
    return longest
def slowType(word):
    for i in word:  # for every letter in the string
        keyboard.press(i)  # press that letter
        time.sleep(0.05)
        keyboard.release(i)  # release that press
        time.sleep(0.125)  # wait .1 seconds

def click(x, y):#not using pyautogui because I think it's too slow
    win32api.SetCursorPos((x, y))#move cursor to position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)#push down
    time.sleep(0.01)#wait
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)#let go

if __name__ == "__main__":
    loadWords(filepath_words)
    main()