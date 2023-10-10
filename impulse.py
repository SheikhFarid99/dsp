import numpy as np
import matplotlib.pyplot as plt

# sin signal
amplitude = 2 
frequency = 2000
signal_lenght = 2
points = np.linspace(0, signal_lenght, num= signal_lenght * frequency)
signal = amplitude * np.sin(2*np.pi*points)

# impulse
imp = [200, 500, 700]
impulse_signal = np.zeros(2*frequency)
for x in imp:
    impulse_signal[x] = 1

# sin * impulse
impulse_sin_signla = signal * impulse_signal

plt.figure(figsize=(10,10))
plt.subplot(3,1,1).plot(points, signal)
plt.title("Sin signal")
plt.subplot(3,1,2).plot(points, impulse_signal)
plt.title("Impulse")
plt.subplot(3,1,3).plot(points, impulse_sin_signla)
plt.title("Sin signal with impulse")
plt.show()

#python impulse.py