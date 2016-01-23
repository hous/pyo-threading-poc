import pyo, time, threading


class Audio(object):
    def __init__(self):
        self.background_thread = None
        self.server = pyo.Server(sr=44100, nchnls=2, buffersize=256, duplex=0).boot()
        self.server.start()

    def play_test_sound(self):
        def sound():
            # blatant plaigarism from jmdumas' jm_Kraut.py from https://github.com/tiagovaz/radiopyo
            krautbeat = pyo.Seq(time=0.3,seq=[2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,3,2,2,2,2,2,1,1,1,6],poly=1)
            krauttable = pyo.LinTable([(0,0.0000),(6,0.8325),(236,0.0000),(1417,0.0000),(8192,0.0000)])
            krautenv = pyo.TrigEnv(krautbeat, table=krauttable, dur=1.5, mul=0.7).mix(1)
            krautgen = pyo.PinkNoise()
            krautfiltfreq = pyo.LFO(freq=1,type=6, mul=0.3, add=3500.7)
            krautfilt = pyo.Biquad(krautgen, freq=krautfiltfreq, q=5, type=0, mul=krautenv)
            krautfiltpan = pyo.SPan(krautfilt, pan=0.3)
            krautdelmul = pyo.LFO(freq=2,type=6, mul=1)
            krautdel = pyo.Delay(krautfilt,delay=0.751,feedback=0.5, mul=krautdelmul)
            krautdelpan = pyo.SPan(krautdel, pan=0.7)
            krautrevinput = krautdelpan+krautfiltpan
            krautrev = pyo.WGVerb(krautrevinput, feedback=0.9, bal=0.03)
            krautbeat.play()
            krautrev.out()
            time.sleep(5)
            # TODO: is there a syntax to play the beat indefinitely using PYO? Without having to do time.sleep?

        self.background_thread = threading.Thread(target=sound)
        self.background_thread.start()

    def kill(self):
        self.server.stop()

        # Give portmidi a second to shut down.
        time.sleep(1)

        self.server.shutdown()
