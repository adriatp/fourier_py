import wave
import numpy as np
import matplotlib.pyplot as plt
import os
import pdb

from wav_utils import *

wav_in_filepath = f"{os.getcwd()}/in/audio_test.wav"
audio_data = get_audio_data_from_wav_file(wav_in_filepath)

img_out_basepath = f"{os.getcwd()}/out/images/"
print_audio_data(audio_data, img_out_basepath)