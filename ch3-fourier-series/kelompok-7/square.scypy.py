import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --- Parameter Gelombang ---
# Durasi waktu (misalnya, dari 0 hingga 1 detik)
duration = 1
# Jumlah sampel (menentukan resolusi plot)
samples = 500
# Frekuensi gelombang (misalnya, 5 Hz)
frequency = 5
# Duty cycle (50% adalah gelombang kotak simetris)
duty_cycle = 0.5 

# --- Pembuatan Gelombang ---
# Membuat array waktu (t)
t = np.linspace(0, duration, samples, endpoint=False)

# Membuat array gelombang kotak (y)
# Argumen untuk signal.square adalah 2 * pi * frekuensi * t
y = signal.square(2 * np.pi * frequency * t, duty=duty_cycle)

# --- Plotting ---
plt.figure(figsize=(10, 4))
plt.plot(t, y, color='blue')
plt.title(f'Gelombang Kotak ({frequency} Hz) dengan SciPy')
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo')
plt.ylim(-1.5, 1.5) # Mengatur batas y agar terlihat jelas
plt.grid(True)
plt.show()
