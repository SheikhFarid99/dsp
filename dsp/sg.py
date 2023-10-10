import numpy as np
import matplotlib.pyplot as plt

amplitude = 2 
frequency = 1
signal_lenght = 2
points = np.linspace(0, signal_lenght, num= signal_lenght * 2000)
signal = amplitude * np.sin(2*np.pi*points*frequency)

plt.plot(points, signal)
plt.axhline(y=0, color='blue')
plt.title('Sine wave')
plt.xlabel('Time')
plt.ylabel('Amplitude = sin(time)')
plt.grid(True, which='both')

plt.show()

# python sg.py