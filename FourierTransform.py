import numpy as np

class FourierTransform:
    def __init__(self, data):
        self.data = data

    def discrete_fourier_transform(self):
        N = len(self.data)
        frequencies = np.fft.fftfreq(N)
        amplitudes = np.fft.fft(self.data)
        return frequencies, amplitudes
