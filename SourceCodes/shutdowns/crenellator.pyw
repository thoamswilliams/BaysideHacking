import keyboard
import os
import time
import random
while True:
    keyboard.wait('s')
    time.sleep(random.randint(240,600))
    os.system('shutdown -f -p')
