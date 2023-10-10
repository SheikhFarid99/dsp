import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz, zpk2tf

# Define filter specifications
cutoff_frequency = 0.2  # Cutoff frequency as a fraction of Nyquist frequency

# Design a Butterworth low-pass filter
b, a = butter(N=4, Wn=cutoff_frequency, btype='low')

# Convert the filter's poles and zeros to transfer function coefficients
numerator, denominator = zpk2tf(b, a, 1)  # Pass k=1 as the third argument

# Calculate the poles and zeros
poles, zeros = np.roots(a), np.roots(b)

# Frequency response of the filter
w, h = freqz(numerator, denominator)

# Plot the pole-zero diagram
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.title('Pole-Zero Plot')
plt.plot(np.real(poles), np.imag(poles), 'ro', markersize=8, label='Poles')
plt.plot(np.real(zeros), np.imag(zeros), 'bo', markersize=8, label='Zeros')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.legend()

# Plot the frequency response
plt.subplot(122)
plt.title('Frequency Response')
plt.plot(w, 20 * np.log10(abs(h)))
plt.xlabel('Frequency (radians)')
plt.ylabel('Amplitude (dB)')
plt.grid()

plt.tight_layout()
plt.show()


# python pz.py