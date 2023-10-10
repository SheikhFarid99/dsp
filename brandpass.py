import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
fs = 1000  # Sampling frequency (Hz)
nyquist = 0.5 * fs  # Nyquist frequency
low_cutoff = 40  # Low cutoff frequency (Hz)
high_cutoff = 60  # High cutoff frequency (Hz)
filter_order = 64  # Filter order (number of taps)

# Create a bandpass FIR filter kernel
taps = filter_order + 1
half_taps = taps // 2

# Calculate the ideal bandpass filter frequency response
ideal_response = np.zeros(taps)
for i in range(-half_taps, half_taps + 1):
    if i == 0:
        ideal_response[i + half_taps] = 2 * (high_cutoff - low_cutoff) / fs
    else:
        ideal_response[i + half_taps] = (
            np.sin(2 * np.pi * high_cutoff * i / fs) / (np.pi * i)
            - np.sin(2 * np.pi * low_cutoff * i / fs) / (np.pi * i)
        )

# Create the window function (Hamming window)
window = np.hamming(taps)

# Multiply the ideal response by the window
filter_kernel = ideal_response * window

# Normalize the filter kernel
filter_kernel /= np.sum(filter_kernel)

# Generate a noisy input signal
t = np.arange(0, 1, 1/fs)
input_signal = (
    np.sin(2 * np.pi * 50 * t)  # A 50 Hz sine wave
    + 0.5 * np.sin(2 * np.pi * 120 * t)  # A 120 Hz sine wave (interference)
    + 0.2 * np.random.normal(size=len(t))  # Gaussian noise
)

# Apply the bandpass filter to the input signal using convolution
output_signal = np.convolve(input_signal, filter_kernel, mode='same')

# Plot the input and output signals
plt.figure(figsize=(10, 6))
plt.plot(t, input_signal, label='Input Signal')
plt.plot(t, output_signal, label='Filtered Signal', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('FIR Bandpass Filter Example')
plt.grid(True)
plt.show()


#python brandpass.py