from math import *
from wav_utils import *
import os

channel=0
audio_path = f"{os.getcwd()}/in/audio_test.wav"
sample_rate, audio_data = wavfile.read(audio_path)
audio_data = [i[channel] for i in audio_data]
print(audio_data)

take = 256
start = 160050
audio_data = audio_data[start:start+take]

out_folder = f"{os.getcwd()}/out/images"
out_file = f"{out_folder}/test.png"

freq_spectrum(audio_data, sample_rate, out_file)