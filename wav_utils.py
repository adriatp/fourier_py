import wave
import math
import numpy as np
import matplotlib.pyplot as plt
import os
import pdb


def get_audio_data_from_wav_file(wav_filepath):

    audio_data = {}
    
    # Open .wav file in readonly mode
    with wave.open(wav_filepath, 'rb') as wav_file:
        
        # Get info from .wav file
        audio_data['num_channels'] = wav_file.getnchannels()
        audio_data['sample_width'] = wav_file.getsampwidth()
        audio_data['frame_rate'] = wav_file.getframerate()
        audio_data['num_frames'] = wav_file.getnframes()

        # Read frames and convert into int16
        audio_data['byte_frames_all'] = wav_file.readframes(audio_data['num_frames'])
        audio_data['int_frames_all'] = np.frombuffer(audio_data['byte_frames_all'], dtype=np.int16)

        # Get int frames for each channel
        audio_data['byte_frames_by_channel'] = []
        audio_data['int_frames_by_channel'] = []
        for i in range(audio_data['num_channels']):
            audio_data['int_frames_by_channel'].append(audio_data['int_frames_all'][i::2])
            audio_data['byte_frames_by_channel'].append(audio_data['byte_frames_all'][i::2])

    return audio_data


def set_byte_data_from_int_data(audio_data):
    # [C1_1,C1_2,C1_3] i [C2_1,C2_2,C2_3] => [[C1_1,C2_1],[C1_2,C2_2],[C1_3,C2_3]...] 
    zip_by_channel = list(zip(*audio_data['int_frames_by_channel']))
    # [[C1_1,C2_1],[C1_2,C2_2],[C1_3,C2_3]...] => [C1_1,C2_1,C1_2,C2_2,C1_3,C2_3,...]
    int_frames_all_list = [x for z in zip_by_channel for x in z]
    # [C1_1,C2_1,C1_2,C2_2,C1_3,C2_3,...] => NP_ARRAY INT16
    audio_data['int_frames_all'] = np.array(int_frames_all_list, dtype=np.int16).astype(f"<i{audio_data['sample_width']}")
    # NP_ARRAY INT16 => NP_BYTES LITTLE_ENDIAN (INT16: CHUNKS OF 2 BYTES)
    audio_data['byte_frames_all'] = audio_data['int_frames_all'].tobytes()


# Audio data must has 'int_frames_by_channel' property
def create_wav_file(audio_data, wav_filepath):

    # Open the WAV file in write mode
    with wave.open(wav_filepath, 'w') as file:
        file.setnchannels(audio_data['num_channels'])
        file.setsampwidth(audio_data['sample_width'])
        file.setframerate(audio_data['frame_rate'])
        file.writeframes(audio_data['byte_frames_all'])



def print_audio_data(audio_data, img_basepath):

    # Print info on screen
    print(f"    num_channels: {audio_data['num_channels']}")
    print(f"    sample_width: {audio_data['sample_width']}")
    print(f"      frame_rate: {audio_data['frame_rate']}")
    print(f"  int_frames_all: {audio_data['int_frames_all']}")
    
    # Print info for each channel
    for i in range(audio_data['num_channels']):
       
        print(f"> plotting channel {i}")

        # Create the time vector for X-axis
        time = np.linspace(0, audio_data['num_frames'] / audio_data['frame_rate'], num=len(audio_data['int_frames_by_channel'][i]))

        # Graph sound wave
        plt.plot(time, audio_data['int_frames_by_channel'][i])
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.title(f"Sound wave for channel {i}")

        # Save image as png
        img_filepath = img_basepath + f"out_ch_{i}.png"
        plt.savefig(img_filepath)
        plt.clf()


def note_frequency(note, octave=0):
    std_freq = {
        'c': 261.63,
        'd': 293.66,
        'e': 329.63,
        'f': 349.23,
        'g': 392.00,
        'a': 440.00,
        'b': 493.88
    }
    return std_freq['note'] * (2**octave)


"""
def create_wav_file_2(file_name, num_channels, samples_per_second, duration_seconds, tone_frequency):
    # Calculate the total number of samples
    num_samples = samples_per_second * duration_seconds

    # Calculate the maximum amplitude
    amplitude = 32767  # maximum amplitude of the sample (16 bits)

    # Open the WAV file in write mode
    with wave.open(file_name, 'w') as file:
        file.setnchannels(num_channels)
        file.setframerate(samples_per_second)
        file.setsampwidth(2)  # 2 bytes for a 16-bit sample

        # Generate the audio samples (simple tone)
        samples = []
        for i in range(num_samples):
            sample_value = int(amplitude * math.sin(2 * math.pi * tone_frequency * i / samples_per_second))
            adjusted_sample_value = sample_value + amplitude  # shift to be positive
            samples.append(adjusted_sample_value.to_bytes(2, 'little'))  # Convert to bytes

        # Write the samples to the WAV file
        file.writeframes(b''.join(samples))

note_frequency = {
    "C0": 16.35,
    "C#0/Db0": 17.32,
    "D0": 18.35,
    "D#0/Eb0": 19.45,
    "E0": 20.60,
    "F0": 21.83,
    "F#0/Gb0": 23.12,
    "G0": 24.50,
    "G#0/Ab0": 25.96,
    "A0": 27.50,
    "A#0/Bb0": 29.14,
    "B0": 30.87,
    "C1": 32.70,
    "C#1/Db1": 34.65,
    "D1": 36.71,
    "D#1/Eb1": 38.89,
    "E1": 41.20,
    "F1": 43.65,
    "F#1/Gb1": 46.25,
    "G1": 49.00,
    "G#1/Ab1": 51.91,
    "A1": 55.00,
    "A#1/Bb1": 58.27,
    "B1": 61.74,
    "C2": 65.41,
    "C#2/Db2": 69.30,
    "D2": 73.42,
    "D#2/Eb2": 77.78,
    "E2": 82.41,
    "F2": 87.31,
    "F#2/Gb2": 92.50,
    "G2": 98.00,
    "G#2/Ab2": 103.83,
    "A2": 110.00,
    "A#2/Bb2": 116.54,
    "B2": 123.47,
    "C3": 130.81,
    "C#3/Db3": 138.59,
    "D3": 146.83,
    "D#3/Eb3": 155.56,
    "E3": 164.81,
    "F3": 174.61,
    "F#3/Gb3": 185.00,
    "G3": 196.00,
    "G#3/Ab3": 207.65,
    "A3": 220.00,
    "A#3/Bb3": 233.08,
    "B3": 246.94,
    "C4": 261.63,
    "C#4/Db4": 277.18,
    "D4": 293.66,
    "D#4/Eb4": 311.13,
    "E4": 329.63,
    "F4": 349.23,
    "F#4/Gb4": 369.99,
    "G4": 392.00
}

# Example usage:
# create_wav_file("out/audio.wav", 2, 44100, 5, note_frequency['G2'])

"""