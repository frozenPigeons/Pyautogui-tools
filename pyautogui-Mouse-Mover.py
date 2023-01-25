import pyautogui
import time
from time import sleep
import os
import sys
import random

print(pyautogui.size()[0])

print('Press Ctrl-C to quit.')
try:
    while True:
        pyautogui.moveTo(random.randint(1, pyautogui.size()[1]), random.randint(1, pyautogui.size()[1]))
        time.sleep(1)
except KeyboardInterrupt:
    print('\n')