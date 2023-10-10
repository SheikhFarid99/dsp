import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the analog signal
sampling_rate = 1000  # Hz
signal_frequency = 5  # Hz
signal_duration = 1.0  # seconds
amplitude = 1.0

# Create a time vector for the analog signal
t_analog = np.linspace(0, signal_duration, int(sampling_rate * signal_duration), endpoint=False)

# Generate the analog signal (a simple sine wave)
analog_signal = amplitude * np.sin(2 * np.pi * signal_frequency * t_analog)

# Simulate analog-to-digital conversion by sampling the analog signal
# You can change the sampling rate to adjust the level of quantization
sampling_rate_digital = 100  # Hz
t_digital = np.arange(0, signal_duration, 1 / sampling_rate_digital)
digital_signal = amplitude * np.sin(2 * np.pi * signal_frequency * t_digital)

# Plot the analog and digital signals
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t_analog, analog_signal, 'b-', label='Analog Signal')
plt.title('Analog Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(t_digital, digital_signal, 'r-', basefmt=' ', linefmt='r-', markerfmt='ro', label='Digital Signal')
plt.title('Digital Signal (After ADC)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()


# python atd.py