import numpy as np
import matplotlib.pyplot as plt
from sawtooth import generate_sawtooth

def fourier_series_sawtooth(freq=1, duration=1, sample_rate=1000, terms=10):
    # Ambil sinyal asli
    t, x, freq = generate_sawtooth(freq, duration, sample_rate)

    # Fourier series approximation
    y_fs = np.zeros_like(t)
    for n in range(1, terms+1):
        # Fourier series sawtooth sinkron dengan scipy.signal.sawtooth
        y_fs += (1/n) * np.sin(2 * np.pi * n * freq * t)

    y_fs = - (2/np.pi) * y_fs  # scaling + tanda minus biar fase sama

    # Plot hasil
    plt.figure(figsize=(8,5))
    plt.plot(t, y_fs, label=f"Fourier series (terms={terms})")
    plt.plot(t, x, label="Original sawtooth wave", alpha=0.7)
    plt.xlabel("x")
    plt.ylabel("y = f(x)")
    plt.title(f"Sawtooth wave and Fourier Series with {terms} terms")
    plt.legend()
    plt.grid(True)
    plt.show()
    return t, x, y_fs

if __name__ == "__main__":
    fourier_series_sawtooth(freq=5, duration=1, sample_rate=2000, terms=10)
    fourier_series_sawtooth(freq=5, duration=1, sample_rate=2000, terms=100)
    fourier_series_sawtooth(freq=5, duration=1, sample_rate=2000, terms=1000)
