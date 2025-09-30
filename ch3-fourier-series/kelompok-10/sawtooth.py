import numpy as np
import matplotlib.pyplot as plt

# Define the Fourier series function
def fourier_series(t, n_terms):
    result = np.zeros_like(t)
    terms = []  # To store each term for later display
    for n in range(1, n_terms + 1):
        term = ((-1)**(n+1)) * (1 / n) * np.sin(n * t)
        result += term
        terms.append(term)  # Append each term
    return result, terms

# Define the time variable
t = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Plot for 20 terms
n_terms = 20
y, terms = fourier_series(t, n_terms)

# Plot the final Fourier series approximation
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

# Display the individual terms
for i, term in enumerate(terms, 1):
    plt.figure(figsize=(10, 6))
    plt.plot(t, term, label=f'Term {i}')
    plt.title(f"Fourier Series Term {i}")
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.grid(True)
    plt.legend()
    plt.show()
