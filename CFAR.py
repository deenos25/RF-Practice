import numpy as np

class CFAR:
    def __init__(self, signal, gap_size, ref_size, bias):
        self.signal = signal
        self.gap_size = gap_size
        self.ref_size = ref_size
        self.bias = bias
    def calc_cfar_avg(self):
        l = len(self.signal)
        # Loop through center indexes
        cfar_values = np.zeros(np.shape(self.signal))
        for i in range(self.gap_size + self.ref_size,
                       l - (self.gap_size + self.ref_size)):
            # Get min indexes
            min_ref = i - (self.gap_size + self.ref_size)
            min_gap = i - self.gap_size
            # Get max indexes
            max_gap = i + self.gap_size
            max_ref = i + (self.gap_size + self.ref_size)
            # Calc. upper & lower means
            lower_mean = np.mean(self.signal[min_ref:min_gap])
            upper_mean = np.mean(self.signal[max_gap:max_ref])
            ref_mean = (lower_mean + upper_mean) / 2
            # Append CFAR values
            cfar_values[i] = ref_mean * self.bias
        return np.clip(cfar_values, 1e-12, None)


