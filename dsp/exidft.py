import numpy as np
import matplotlib.pyplot as plt

Xk = np.array([1, 2, 3])
N = len(Xk)

xn = np.zeros(N, dtype=np.complex128(1))
k = np.arange(0, N)
for n in range(0, N):
    xn[n] = np.sum(np.exp(1j * 2 * np.pi * k * n / N) * Xk)

xn /= N

print("x(n) = ")
print(xn)

plt.figure()
plt.stem(k, np.abs(xn))
plt.xlabel('n')
plt.ylabel('Magnitude')
plt.title('IDFT OF A SEQUENCE')
plt.grid(True)
plt.show()