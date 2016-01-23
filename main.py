import time, pyo
from audio import Audio

def init():
    s = Audio()
    s.play_test_sound()

    counter = 0
    while counter < 6:
        print counter
        counter += 1
        time.sleep(1)

    time.sleep(0.25)
    s.kill()

init()
