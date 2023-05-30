import numpy as np

# Ejemplo de datos de una onda
# Aquí debes reemplazar `t` por tu secuencia temporal y `y` por los valores de la onda registrada
t = np.linspace(0, 1, 1000)  # Secuencia temporal
# Frequencia 50 y frequencia 120
y = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)  # Ejemplo de onda con dos frecuencias

# Aplicar la Transformada Rápida de Fourier (FFT)
fft_result = np.fft.fft(y)

# Obtener el espectro de frecuencia y las frecuencias correspondientes
frequencies = np.fft.fftfreq(len(t), t[1] - t[0])
amplitudes = np.abs(fft_result)

# Imprimir las frecuencias y amplitudes correspondientes
for freq, amp in zip(frequencies, amplitudes):
    print(f"Frecuencia: {freq:.2f} Hz, Amplitud: {amp:.2f}")

