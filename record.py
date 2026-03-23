import sounddevice as sd
import numpy as np

# This shit DID NOT WORK OH MY GOD IM GOING TO BED FUCKKK

def record_audio(duration=30, fs=16000):
    print("Jarvis is listening...")
    # อัดเสียงและเก็บใน NumPy array (DataType เป็น float32 ตามที่ AI ส่วนใหญ่ต้องการ)
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # รอจนกว่าจะอัดเสร็จ
    print("Recording finished.")
    return recording

# audio_data = record_audio()