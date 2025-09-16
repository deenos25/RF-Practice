import numpy as np
import matplotlib.pyplot as plt
from frequency_analysis import fft

class GeneratePlots:
    def __init__(self, time, signal):
        self.time = time
        self.signal = signal
    def time_plot(self):
        plt.plot(self.time, self.signal)
        plt.xlabel('Time (s)'), plt.ylabel('Amplitude (V)')
        plt.title('Time Plot'), plt.grid(), plt.show()
    def freq_plot(self, freq_range=[0, 6]):
        fs = 1 / (self.time[1] - self.time[0])
        freq, amp = fft(self.signal, fs)
        l = int(len(freq) / 2)
        freq, amp = freq[:l], amp[:l]
        plt.plot(freq, 20 * np.log10(amp)), plt.xlim(freq_range[0], freq_range[1])
        plt.xlabel('Frequency (Hz)'), plt.ylabel('Amplitude (dB)')
        plt.title('FFT'), plt.grid(), plt.show()

