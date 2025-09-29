mport numpy as np
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
    amplitude = A  # Amplitudo gelom
