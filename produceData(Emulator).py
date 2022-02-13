import cv2
import pyautogui
import numpy as np
from time import sleep
from pynput import mouse
import os
import logging
import time
from pynput import keyboard
i = 0
folderint = 0
attentionThreshold = 0.01 #seconds
tic = time.process_time()
reset = 0
print("Collecting data...")


def on_press(key):
    global i
    sleep(0.001)
    try:
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
        cv2.COLOR_RGB2BGR)
        dirname = str(key.char)
        if os.path.isdir(key.char) == False:
            os.mkdir(key.char)
            cv2.imwrite(str(key.char) + "\\frame" + str(i) +".png", image)
            i += 1
        if os.path.isdir(key.char) == True:
            cv2.imwrite(str(key.char) + "\\frame" + str(i) +".png", image)
            i += 1
        
    except AttributeError:
        print('error')

def on_release(key):
   print ("key released")
            
    
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()