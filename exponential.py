import numpy as np
import matplotlib.pyplot as plt

frequency = 2000
signal_lenght = 2
t = np.linspace(0, signal_lenght, num= signal_lenght * frequency)

Vr_plus = 1500*np.exp(-25*t)*np.sin(t)
Vr_minus = -1500*np.exp(-25*t)*np.sin(t)

plt.plot(t, Vr_plus)
plt.plot(t, Vr_minus)
plt.title('Exponential wave')
plt.xlabel('Time')
plt.grid(True, which='both')
plt.show()

# python exponential.py