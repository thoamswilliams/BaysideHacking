import winsound
import datetime
import time
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
    time.sleep(1)
    if a:
        winsound.Beep(17500, 600)
