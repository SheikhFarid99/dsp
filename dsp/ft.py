import numpy as np
import matplotlib.pyplot as plt

N = 250
ts = 0.0002
t = np.arange(0, N) * ts
x = np.cos(2 * np.pi * 100 * t) + np.cos(2 * np.pi * 500 * t) + np.cos(2 * np.pi * 800 * t)

plt.subplot(2, 1, 1)
plt.plot(t, x)

k = 0
X = np.zeros(801, dtype=complex)

for f in range(801):
    k += 1
    X[k - 1] = np.trapz(x * np.exp(-1j * 2 * np.pi * f * t), t)

frequencies = np.arange(801)
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(X))
plt.show()

# python ft.py
