from math import *
from wav_utils import *
import os

channel=0
take = 24000
start = 160050

filename = "audio_test"
audio_path = f"{os.getcwd()}/in/{filename}.wav"
out_folder = f"{os.getcwd()}/out/images"
out_file = f"{out_folder}/{filename}.png"

sample_rate, audio_data = wavfile.read(audio_path)
audio_data = [i[channel] for i in audio_data]
audio_data = audio_data[start:start+take]

freq_spectrum(audio_data, sample_rate, out_file)

filename = "note_a"
audio_path = f"{os.getcwd()}/in/{filename}.wav"
out_folder = f"{os.getcwd()}/out/images"
out_file = f"{out_folder}/{filename}.png"

sample_rate, audio_data = wavfile.read(audio_path)
audio_data = [i[channel] for i in audio_data]
audio_data = audio_data[start:start+take]

freq_spectrum(audio_data, sample_rate, out_file)

filename = "note_a_violin"
audio_path = f"{os.getcwd()}/in/{filename}.wav"
out_folder = f"{os.getcwd()}/out/images"
out_file = f"{out_folder}/{filename}.png"

sample_rate, audio_data = wavfile.read(audio_path)
audio_data = [i[channel] for i in audio_data]
audio_data = audio_data[start:start+take]

freq_spectrum(audio_data, sample_rate, out_file)


filename = "a_test"
audio_path = f"{os.getcwd()}/in/{filename}.wav"
out_folder = f"{os.getcwd()}/out/images"
out_file = f"{out_folder}/{filename}.png"

sample_rate, audio_data = wavfile.read(audio_path)
audio_data = [i[channel] for i in audio_data]
audio_data = audio_data[start:]

freq_spectrum(audio_data, sample_rate, out_file)

# Pillar els pics! :3