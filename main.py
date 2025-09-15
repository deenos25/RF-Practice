import numpy as np
from custom_plots import GeneratePlots
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

# Plot
plotting_obj = GeneratePlots(t, combined_signal)
plotting_obj.time_plot(), plotting_obj.freq_plot(freq_range=[0, 10])

# source .venv/Scripts/activate
