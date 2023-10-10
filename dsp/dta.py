import numpy as np
import matplotlib.pyplot as plt

# Define parameters
sampling_rate = 1000  # Hz
signal_frequency = 5  # Hz
signal_duration = 1.0  # seconds
amplitude = 1.0

# Create a time vector for the digital signal
t_digital = np.linspace(0, signal_duration, int(sampling_rate * signal_duration), endpoint=False)

# Generate a digital signal (a simple sine wave)
digital_signal = amplitude * np.sin(2 * np.pi * signal_frequency * t_digital)

# Create a time vector for the analog signal (higher sampling rate for smoother plotting)
t_analog = np.linspace(0, signal_duration, int(10 * sampling_rate * signal_duration), endpoint=False)

# Simulate digital-to-analog conversion (zero-order hold)
analog_signal = np.zeros_like(t_analog)
for i, t in enumerate(t_analog):
    index = int(t * sampling_rate)
    analog_signal[i] = digital_signal[min(index, len(digital_signal) - 1)]

# Plot the digital and analog signals
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t_digital, digital_signal, 'bo-', label='Digital Signal')
plt.title('Digital Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t_analog, analog_signal, 'r-', label='Analog Signal')
plt.title('Analog Signal (After DAC)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()


#python dta.py