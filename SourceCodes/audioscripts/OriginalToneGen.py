from pygame import mixer # Load the required library
import winsound
import keyboard
def volumeup():
    for i in range(50):
        keyboard.press_and_release('volume up')
mixer.init()
#sound = mixer.Sound("tone2.wav")
#mixer.music.load('D:\tone2.wav')
while True:
    volumeup()
    winsound.Beep(17500, 30)
