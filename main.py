import time, pyo
from audio import Audio

def init():
	# initiate the audio controller class, and play a test sound.
    s = Audio()
    s.play_test_sound()

    # Start a counter in the main thread, to demonstrate that the audio happens in a separate thread and does not block the main thread.
    counter = 0
    while counter < 6:
        print counter
        counter += 1
        time.sleep(1)

    s.kill()

init()
