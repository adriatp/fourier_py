
from math import *
from wav_utils import *

wav_in_filepath = f"{os.getcwd()}/in/audio_test.wav"
audio_data = get_audio_data_from_wav_file(wav_in_filepath)

img_out_basepath = f"{os.getcwd()}/out/images/"
print_audio_data(audio_data, img_out_basepath)

audio_data_2 = {
  'num_channels': 2,
  'sample_width': audio_data['sample_width'],
  'frame_rate': audio_data['frame_rate'],
  'num_frames': audio_data['num_frames'],
  'int_frames_by_channel': [audio_data['int_frames_by_channel'][0], [0]*audio_data['num_frames']]
}

set_byte_data_from_int_data(audio_data_2)

print_audio_data(audio_data_2, img_out_basepath)
wav_out_filepath = f"{os.getcwd()}/out/audios/audio_out.wav"
create_wav_file(audio_data_2, wav_out_filepath) 