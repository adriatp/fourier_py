import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import pdb

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


def freq_spectrum(values, sample_rate, out_file):
    fft_data = np.fft.fft(values)
    magnitude_spectrum = np.abs(fft_data)
    frequencies = np.fft.fftfreq(len(values), 1/sample_rate)
    pdb.set_trace()
    
    # Plot frequency spectre
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies, magnitude_spectrum)
    plt.title('Espectro de frecuencia')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.xlim(0, sample_rate/2)

    # Save image as png
    plt.savefig(out_file)
    plt.clf()