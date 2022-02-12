import cv2
import pyautogui
import numpy as np
from time import sleep
from pynput.mouse import Listener
import os
import logging
#fix lag
i = 0
folderint = 0
print("Collecting data...")
def on_move(x, y):
    global i
    return i
def on_click(x, y, button, pressed):
    if pressed:
        global folderint
        folderint = folderint + 1
        return folderint

def on_scroll(x, y, dx, dy):
    global i
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
    cv2.COLOR_RGB2BGR)
    dirname = str(folderint)
    if os.path.isdir(dirname) == False:
        os.mkdir(dirname)
    cv2.imwrite(str(folderint) + "\\frame" + str(i) +".png", image)
    i = i + 1
    return i
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()