import sounddevice as sd

#config
duration = 30
fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2

#record
recordmyvoice=sd.rec(int(duration * fs))
sd.wait() #check if finished