import sounddevice as sd

duration = 10 # (seconds)
rec_rate = 44100
rec = sd.rec(int(duration * rec_rate), samplerate=rec_rate, channels=1, blocking=True)

import IPython.display as ipd
ipd.Audio(rec[:,0], rate=rec_rate)