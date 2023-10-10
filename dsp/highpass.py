import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
fs = 1000  # Sampling frequency (Hz)
nyquist = 0.5 * fs  # Nyquist frequency
cutoff_frequency = 40  # Cutoff frequency (Hz)
filter_order = 64  # Filter order (number of taps)

# Create a high-pass FIR filter kernel
taps = filter_order + 1
half_taps = taps // 2

# Calculate the ideal high-pass filter frequency response
ideal_response = np.zeros(taps)
for i in range(-half_taps, half_taps + 1):
    if i == 0:
        ideal_response[i + half_taps] = 1 - (2 * cutoff_frequency / fs)
    else:
        ideal_response[i + half_taps] = (
            -np.sin(2 * np.pi * cutoff_frequency * i / fs) / (np.pi * i)
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
    0.5 * np.sin(2 * np.pi * 20 * t)  # A 20 Hz sine wave
    + 0.3 * np.sin(2 * np.pi * 80 * t)  # An 80 Hz sine wave
    + 0.2 * np.random.normal(size=len(t))  # Gaussian noise
)

# Apply the high-pass filter to the input signal using convolution
output_signal = np.convolve(input_signal, filter_kernel, mode='same')

# Plot the input and output signals
plt.figure(figsize=(10, 6))
plt.plot(t, input_signal, label='Input Signal')
plt.plot(t, output_signal, label='Filtered Signal', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('FIR High-Pass Filter Example')
plt.grid(True)
plt.show()


#python highpass.py