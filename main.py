import wave

wav_basepath = '/mnt/c/Users/adria/Documents/Enregistraments de so/'
wav_filename = 'Enregistrament.wav'

# Abrir el archivo .wav en modo lectura
with wave.open(wav_basepath + wav_filename, 'rb') as wav_file:

    # Obtener información del archivo .wav
    num_channels = wav_file.getnchannels()
    sample_width = wav_file.getsampwidth()
    frame_rate = wav_file.getframerate()
    num_frames = wav_file.getnframes()

    # Leer los datos del archivo .wav
    wav_data = wav_file.readframes(num_frames)

# Hacer algo con los datos...
print(wav_data)