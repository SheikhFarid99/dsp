import numpy as np
import matplotlib.pyplot as plt

# Input the length of the sequence
N = int(input('Enter the length of sequence: '))

# Input the sequence
x = np.array(input('Enter the sequence (comma-separated): ').split(','), dtype=float)

# Create arrays for n and k
n = np.arange(N)
k = np.arange(N)

# Calculate wN
wN = np.exp(-1j * 2 * np.pi / N)

# Create a matrix nk for element-wise exponentiation
nk = np.outer(n, k)

# Calculate wNnk
wNnk = np.power(wN, nk)

# Calculate Xk
Xk = np.dot(x, wNnk)

# Print Xk
print('Xk:')
print(Xk)

# Calculate the magnitude of Xk
mag = np.abs(Xk)

# Plot magnitude
plt.subplot(2, 1, 1)
plt.stem(k, mag)
plt.grid(True)
plt.xlabel('k')
plt.title('MAGNITUDE OF FOURIER TRANSFORM')
plt.ylabel('Magnitude')

# Calculate the phase of Xk
phase = np.angle(Xk)

# Plot phase
plt.subplot(2, 1, 2)
plt.stem(k, phase)
plt.grid(True)
plt.xlabel('k')
plt.title('PHASE OF FOURIER TRANSFORM')
plt.ylabel('Phase')

plt.tight_layout()
plt.show()
