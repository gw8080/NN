import cv2
import pyautogui
import numpy as np
from time import sleep
from pynput import mouse
import os
import logging
import time
i = 0
folderint = 0
saveLimit = 42
attentionThreshold = 0.5 #seconds
tic = time.process_time()
reset = 0
print("Collecting data...")
def on_move(x, y):
    global tic
    tic = time.process_time()
    global reset
    reset = 1
    return tic
def on_click(x, y, button, pressed):
    if pressed:
        global folderint
        folderint = folderint + 1
        return folderint

def on_scroll(x, y, dx, dy):
    global tic
    tic = time.process_time()
    global reset
    reset = 1
    return tic
    
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
n = 0
while(True):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
    cv2.COLOR_RGB2BGR)
    dirname = str(folderint)
    if os.path.isdir(dirname) == False:
        os.mkdir(dirname)
    if n < saveLimit:
        cv2.imwrite(str(folderint) + "\\frame" + str(i) +".png", image)
        i = i + 1
        n = n + 1
    toc = time.process_time()
    if toc-tic > attentionThreshold and reset == 1:
        reset = 0
        n = 0
        folderint = folderint + 1