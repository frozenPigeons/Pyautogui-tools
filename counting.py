
import pyautogui
import time
#the first time.sleep lets you run the program then get into discord
time.sleep(2)
#the first number (3933) is the number you are starting from.
#the second number (100000) is the number you are ending at.
for i in range(3933, 100000):
#the number in time.sleep which is 9 is how long . Adjust this number based on the chat cooldown. You have none so make it like 2
    time.sleep(3)
    number = str(i)
    pyautogui.typewrite(number)
    pyautogui.press('enter')

