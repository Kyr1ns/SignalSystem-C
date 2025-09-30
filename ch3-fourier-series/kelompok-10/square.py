import numpy as np
import matplotlib.pyplot as plt

# Define the Fourier series function
def fourier_series(t, n_terms):
    result = 2.5  # The constant term
    for n in range(1, n_terms + 1, 2):
        result += (10 / np.pi) * (1 / n) * np.sin(n * np.pi * t / 4)
    return result

# Define the time variable
t = np.linspace(-4 * np.pi, 4 * np.pi, 1000)

# Plot for 20 terms
n_terms = 20
y = fourier_series(t, n_terms)

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(t, y, label=f'Fourier Series with {n_terms} terms', color='blue')
plt.title(f"Fourier Series Approximation with {n_terms} Terms")
plt.xlabel('t')
plt.ylabel('f(t)')
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True)
plt.legend()
plt.show()
