import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Generate a noisy signal
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Time vector
signal_freq = int(input('Frequency of the signal : '))  # Frequency of the signal (in Hz)
signal = np.sin(2 * np.pi * signal_freq * t)  # A simple sine wave

# Add noise to the signal
noise_amplitude = 0.5
noise = noise_amplitude * np.random.normal(size=len(t))
noisy_signal = signal + noise

# Design the low-pass filter
cutoff_freq = 20  # Cutoff frequency (in Hz)
b, a = butter(N=4, Wn=cutoff_freq / (0.5 * fs), btype='low')  # Create a Butterworth low-pass filter

# Apply the filter to the noisy signal
filtered_signal = lfilter(b, a, noisy_signal)

# Plot the original, noisy, and filtered signals
plt.figure(figsize=(10, 6))

plt.plot(t, signal, 'b', label='Original Signal')
plt.plot(t, noisy_signal, 'g', label='Noisy Signal')
plt.plot(t, filtered_signal, 'r', label='Filtered Signal')

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Low-Pass Filter')
plt.grid(True)
plt.show()

plt.plot(t, noisy_signal, 'g', label='Noisy Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Low-Pass Filter')
plt.grid(True)
plt.show()

plt.plot(t, filtered_signal, 'r', label='Filtered Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Low-Pass Filter')
plt.grid(True)
plt.show()
