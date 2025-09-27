

import numpy as np
import matplotlib.pyplot as plt

def run_sawtooth(A,F,S):

    # Define the parameters of the sawtooth wave
    # amplitude = 1.0  # Amplitude of the wave
    # frequency = 20.0  # Frequency of the wave in Hz
    # duration = 1.0   # Duration of the wave in seconds
    amplitude = A  # Amplitude of the wave
    frequency = F  # Frequency of the wave in Hz
    duration = S   # Duration of the wave in seconds

    # Generate the time values for the x-axis
    sampling_rate = 1000  # Number of samples per second
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples)

    # Generate the y-values for the sawtooth wave
    cycles = frequency * time
    sawtooth = amplitude * (cycles - np.floor(cycles))

    # Plot the sawtooth wave
    plt.plot(time, sawtooth)

    # Set the plot title and labels for the x and y axes
    plt.title('Sawtooth Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    # Show the plot
    plt.show()


def run_sawtooth_analyze(A,F,S):

        # Define the parameters of the sawtooth wave
    # amplitude = 1.0  # Amplitude of the wave
    # frequency = 20.0  # Frequency of the wave in Hz
    # duration = 1.0   # Duration of the wave in seconds
    amplitude = A  # Amplitude of the wave
    frequency = F  # Frequency of the wave in Hz
    duration = S   # Duration of the wave in seconds

    # Generate the time values for the x-axis
    sampling_rate = 1000  # Number of samples per second
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples)

    # Generate the y-values for the sawtooth wave
    cycles = frequency * time
    sawtooth = amplitude * (cycles - np.floor(cycles))

    # # Plot the sawtooth wave
    # plt.plot(time, sawtooth)

    # # Set the plot title and labels for the x and y axes
    # plt.title('Sawtooth Wave')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Amplitude')

    # # Show the plot
    # plt.show()

    return [time,sawtooth]

