import numpy as np

def fft(signal, fs):
    amp = np.abs(np.fft.fft(signal))
    freq = np.fft.fftfreq(len(signal), 1/fs)
    return freq, amp