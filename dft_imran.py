import numpy as np
import matplotlib.pyplot as plt

# Define signal parameters
Fa = 10
T = 1 / Fa
t = np.arange(0, T, T / 99)
y = 5 * np.sin(2 * np.pi * Fa * t) + 2 * np.sin(2 * np.pi * 2 * Fa * t) + 2 * np.sin(2 * np.pi * 3 * Fa * t)

# Plot the original signal
plt.figure(1)
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original Signal')
plt.grid(True)

# Define sampling parameters
Fs = 640
Ts = 1 / Fs
N = int(T / Ts)
n = np.arange(N)
yy = 5 * np.sin(2 * np.pi * Fa * n * Ts) + 2 * np.sin(2 * np.pi * 2 * Fa * n * Ts) + 2 * np.sin(2 * np.pi * 3 * Fa * n * Ts)

# Plot the sampled signal
plt.figure(2)
plt.stem(n, yy)
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.title('Sampled Signal')
plt.grid(True)

# Compute and plot the DFT
b = []
for k in range(N):
    h = []
    for n in range(N):
        ff = yy[n] * np.exp(-1j * 2 * np.pi * (k - 1 - (N / 2)) * (n - 1 - (N / 2)) / N)
        h.append(ff)
    p = sum(h)
    b.append(p)

plt.figure(4)
f = Fs * np.arange(-N / 2, N / 2) / N
plt.stem(f, np.abs(b))
plt.axis([-30, 30, 0, 160])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude of DFT')
plt.grid(True)

plt.show()

# python dft_imran.py
