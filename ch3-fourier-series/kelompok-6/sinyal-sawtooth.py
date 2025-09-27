import numpy as np
import matplotlib.pyplot as plt

# Parameter sinyal
T = 1          # Periode
f = 1 / T      # Frekuensi
t = np.linspace(0, T, 1000)  # Waktu
terms = 50     # Jumlah suku Fourier

# Fourier series untuk sinyal sawtooth
sawtooth = np.zeros_like(t)
for n in range(1, terms + 1):
    sawtooth += ((-1) ** (n + 1)) * (2 / (n * np.pi)) * np.sin(2 * np.pi * n * f * t)

# Plot hasil
plt.figure(figsize=(8, 4))
plt.plot(t, sawtooth, label=f'Sawtooth Fourier Series ({terms} terms)')
plt.title('Sinyal Sawtooth dengan Fourier Series')
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()