# import argparse
# import tempfile
# import queue
# import sys

# import sounddevice as sd
# import soundfile as sf
# import numpy  # Make sure NumPy is loaded before it is used in the callback

# import os
# q = queue.Queue()


# def callback(indata, frames, time, status):
#     """This is called (from a separate thread) for each audio block."""
#     q.put(indata.copy())



# print(sd.query_devices())


# try:
#     os.remove("a.wav")
# except:
#     pass


# for dev in range(40):
#     t = 0
#     file_name = f'dev_{dev}.wav'
#     with sf.SoundFile(file_name, mode='x', samplerate=48000,
#                         channels=2, subtype="PCM_24") as file:
#             with sd.InputStream(samplerate=48000, device=dev,
#                                 channels=2, callback=callback):
#                 while t < 100:
#                     t += 1
#                     file.write(q.get())


import pyaudio
import wave


p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if ( dev['hostApi'] == 0):
        dev_index = dev['index'];
        print('dev_index', dev_index)


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"


dev_index = 1

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                input_device_index = dev_index,
                frames_per_buffer = CHUNK)

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)


print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()


wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()