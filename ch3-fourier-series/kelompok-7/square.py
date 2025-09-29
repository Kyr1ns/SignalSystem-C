import numpy as np
import matplotlib.pyplot as plt
# Import modul signal dari scipy untuk fungsi square
from scipy import signal 


def run_square(A, F, S):
    """
    Menghasilkan, memplot, dan menampilkan gelombang kotak.

    Parameters:
    - A (float): Amplitudo gelombang.
    - F (float): Frekuensi gelombang dalam Hz.
    - S (float): Durasi gelombang dalam detik.
    """
    # Define the parameters of the square wave
    amplitude = A  # Amplitudo gelombang
    frequency = F  # Frekuensi gelombang dalam Hz
    duration = S   # Durasi gelombang dalam detik

    # Generate the time values for the x-axis
    sampling_rate = 1000  # Number of samples per second
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples, endpoint=False) # endpoint=False disarankan untuk sinyal periodik

    # Generate the y-values for the square wave
    # Catatan: Fungsi signal.square menghasilkan gelombang dari -1 hingga 1.
    # Kita mengalikannya dengan 'amplitude' untuk mendapatkan amplitudo yang diinginkan.
    # Default duty cycle (siklus kerja) adalah 0.5 (simetris).
    square_wave = amplitude * signal.square(2 * np.pi * frequency * time)

    # Plot the square wave
    plt.plot(time, square_wave)

    # Set the plot title and labels for the x and y axes
    plt.title('Square Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.ylim(-(amplitude + 0.1), (amplitude + 0.1)) # Mengatur batas y agar terlihat jelas

    # Show the plot
    plt.show()


def run_square_analyze(A, F, S):
    """
    Menghasilkan gelombang kotak dan mengembalikan array waktu dan amplitudo.
    Berguna untuk analisis (misalnya, Deret Fourier).

    Parameters:
    - A (float): Amplitudo gelombang.
    - F (float): Frekuensi gelombang dalam Hz.
    - S (float): Durasi gelombang dalam detik.

    Returns:
    - list: [array waktu (x), array gelombang kotak (y)]
    """
    # Define the parameters of the square wave
    amplitude = A  # Amplitudo gelombang
    frequency = F  # Frekuensi gelombang dalam Hz
    duration = S   # Durasi gelombang dalam detik

    # Generate the time values for the x-axis
    sampling_rate = 1000  # Number of samples per second
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples, endpoint=False)

    # Generate the y-values for the square wave
    square_wave = amplitude * signal.square(2 * np.pi * frequency * time)

    return [time, square_wave]

# Contoh Penggunaan:
# run_square(A=1.5, F=5, S=2) 
# data = run_square_analyze(A=1.0, F=1, S=4)
# print(data[0]) # Array waktu
