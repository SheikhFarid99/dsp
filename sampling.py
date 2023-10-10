import numpy as np
import matplotlib.pyplot as plt

print("\n")
A = float(input("Amplitude of Transmitting signal: "))
print("\n\n")

f = 100
T = 1 / f
t = np.arange(0, 2 * T, T / 100)
y = A * np.sin(2 * np.pi * f * t)
plt.figure(1, figsize=(10, 4))
plt.plot(t, y, linewidth=3)
plt.ylabel('Amplitude (volt)')
plt.xlabel('Time (Sec)')
plt.title('Transmitting Signal')
plt.show()

Ts = T / 20
Fs = 1 / Ts
n = np.arange(1, int(2 * T / Ts) + 1)
y1 = A * np.sin(2 * np.pi * f * n * Ts)
plt.figure(2, figsize=(10, 4))
plt.stem(n, y1)
plt.ylabel('Amplitude (volt)')
plt.xlabel('Discrete time')
plt.title('Discrete Time Signal after Sampling')
plt.show()

y2 = A + y1
plt.figure(3, figsize=(10, 4))
plt.stem(n, y2)
plt.ylabel('Amplitude (volt)')
plt.xlabel('Discrete time')
plt.title('DC Level + Discrete Time Signal')
plt.show()

y3 = np.round(y2)
plt.figure(4, figsize=(10, 4))
plt.stem(n, y3)
plt.ylabel('Amplitude (volt)')
plt.xlabel('Discrete time')
plt.title('Quantized Signal')
plt.show()

y4 = [format(int(val), '04b') for val in y3]
Bi = y4
print(Bi)
