import numpy as np
import matplotlib.pyplot as plt

# Parameter sinyal
T = 1          # Periode
f = 1 / T      # Frekuensi
t = np.linspace(0, T, 1000)  # Waktu
terms = 50     # Jumlah suku Fourier

# Fourier series untuk sinyal kotak
square = np.zeros_like(t)
for n in range(1, terms * 2, 2):  # hanya ambil harmonik ganjil (1,3,5,...)
    square += (4 / (np.pi * n)) * np.sin(2 * np.pi * n * f * t)

# Plot hasil
plt.figure(figsize=(8, 4))
plt.plot(t, square, label=f'Square Wave Fourier Series ({terms} terms)')
plt.title('Sinyal Kotak dengan Fourier Series')
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
