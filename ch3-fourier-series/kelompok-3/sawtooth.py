import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def generate_sawtooth(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=True)
    x = signal.sawtooth(2 * np.pi * freq * t)  
    return t, x, freq

if __name__ == "__main__":
    t, x, freq =generate_sawtooth(5, 1, 1000)
    plt.plot(t, x)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(f"Sawtooth Wave - {freq} Hz")
    plt.grid(True)
    plt.show()
