import numpy as np

# Setup time interval
fs = 100 # Hz
time_interval = 10 # sec
N = int(fs * time_interval)
t = np.arange(N) / fs

# Add main signals
signal_1 = (7/8) * np.sin(2 * np.pi * 1 * t) # @ 1 Hz
signal_2 = (2/3) * np.sin(2 * np.pi * 2 * t) # @ 2 Hz
signal_3 = (3/8) * np.sin(2 * np.pi * 3 * t) # @ 3 Hz

# Add noise
noise = np.random.normal(0, 1, N)

# Combine signals
combined_signal = signal_1 + signal_2 + signal_3 + noise

def fft(signal, fs):
    amp = np.abs(np.fft.fft(signal))
    freq = np.fft.fftfreq(len(signal), 1/fs)
    l = int(len(freq) / 2)
    amp, freq = amp[:l], freq[:l]
    plt.plot(freq, 20*np.log10(amp))
    plt.xlabel('Frequency (Hz)'), plt.ylabel('Amplitude (dB)')
    plt.title('FFT'), plt.grid(), plt.show()

import matplotlib.pyplot as plt
plt.plot(t, combined_signal), plt.show()
fft(combined_signal, fs)