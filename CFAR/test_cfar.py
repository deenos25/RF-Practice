import numpy as np
from custom_plots import GeneratePlots
from frequency_analysis import fft
from CFAR import CFAR
from scipy import signal
import matplotlib.pyplot as plt

# Setup time interval
fs = 1000 # Hz
time_interval = 10 # sec
N = int(fs * time_interval)
t = np.arange(N) / fs

# Add main signals
signal_1 = (7/8) * np.sin(2 * np.pi * 10 * t) # @ 10 Hz
signal_2 = (2/3) * np.sin(2 * np.pi * 20 * t) # @ 20 Hz
signal_3 = (3/8) * np.sin(2 * np.pi * 30 * t) # @ 30 Hz

# Add noise
noise = np.random.normal(0, 1, N)

# Combine signals
combined_signal = signal_1 + signal_2 + signal_3 + noise

blackman_window = signal.windows.blackman(N)
combined_signal = combined_signal * blackman_window

# Plot
plotting_obj = GeneratePlots(t, combined_signal)
plotting_obj.time_plot(), plotting_obj.freq_plot(freq_range=[5, 35])

# Deploy CFAR frequency domain signal
freq, amp = fft(combined_signal, fs)
cfar_values = CFAR(amp, gap_size=2, ref_size=12, bias=2.5).calc_cfar_avg()
l = int(len(freq) / 2)
freq, amp, cfar_values = freq[:l], amp[:l], cfar_values[:l]
plt.plot(freq, 20 * np.log10(amp))
plt.plot(freq, 20 * np.log10(cfar_values))
plt.xlim([5, 35]), plt.ylim([0, 75]), plt.grid()
plt.legend(['Original Signal', 'CFAR Values']), plt.show()

# source .venv/Scripts/activate
