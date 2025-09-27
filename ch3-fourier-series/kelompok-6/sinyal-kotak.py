```python
import numpy as np
import matplotlib.pyplot as plt

def square_wave(t, T=2.0):
    """
    Square wave dengan periode T dan amplitudo ±1.
    """
    y = np.sign(np.sin(2*np.pi*t/T))
    y[y == 0] = 1
    return y

def fourier_square(t, T=2.0, num_terms=5):
    """
    Partial sum deret Fourier dari square wave.
    
    Parameters
    ----------
    t : array
        Waktu.
    T : float
        Periode.
    num_terms : int
        Jumlah suku ganjil yang digunakan (misal num_terms=5 -> k=1,3,5,7,9).
    
    Returns
    -------
    y : array
        Approximation hasil deret Fourier.
    ks : array
        Indeks k (ganjil) yang dipakai.
    """
    result = np.zeros_like(t, dtype=float)
    ks = np.arange(1, num_terms*2, 2)  # hanya k ganjil
    for k in ks:
        result += (4/np.pi) * (1.0/k) * np.sin(2*np.pi*k*t/T)
    return result, ks

def plot_square_vs_fourier(T=2.0, num_terms_list=[1,3,5,25], t_range=(-3,3)):
    """
    Plot square wave dan aproksimasi Fourier untuk berbagai jumlah suku.
    """
    t = np.linspace(t_range[0], t_range[1], 2000)
    sq = square_wave(t, T=T)

    for n in num_terms_list:
        approx, ks = fourier_square(t, T=T, num_terms=n)
        plt.figure(figsize=(8,3.5))
        plt.plot(t, sq, label="Square (ideal)")
        plt.plot(t, approx, linestyle="--", label=f"Fourier approx (n={n}, k sampai {ks[-1]})")
        plt.title(f"Square wave vs Fourier series (n={n} suku ganjil)")
        plt.xlabel("t")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.legend()
        plt.show()
```
