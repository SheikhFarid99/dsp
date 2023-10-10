import numpy as np
import matplotlib.pyplot as plt

# sin signal
amplitude = 2 
frequency = 2000
signal_lenght = 2
points = np.linspace(0, signal_lenght, num= signal_lenght * 2000)

t = np.linspace(-1, 1, num= signal_lenght * frequency)
sin_signal = amplitude * np.sin(2*np.pi*points)

# Unit
unit_signal = np.zeros(2*frequency)
unit_signal[frequency:] = 1

# sin * unit
unit_sin_signal = sin_signal * unit_signal
plt.figure(figsize=(10,10))
plt.subplot(3,1,1).plot(t, sin_signal)
plt.title("Sin signal")
plt.subplot(3,1,2).plot(t, unit_signal)
plt.title("Unit")
plt.subplot(3,1,3).plot(t, unit_sin_signal)
plt.title("Sin signal with Unit")
plt.show()

# python unitstep.py