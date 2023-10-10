# import numpy as np

# x = np.array([1, 2, 3])
# h = np.array([0.5, 0.25])
# conv_result = np.convolve(x, h, mode='full')
# print("Convolution Result:", conv_result)

import numpy as np
import matplotlib.pyplot as plt

# Define two example signals
x = np.array([1, 2, 3])
h = np.array([0.5, 0.25])

# Perform convolution using NumPy
conv_result = np.convolve(x, h, mode='full')

# Create time indices for the signals
n_x = np.arange(0, len(x))
n_h = np.arange(0, len(h))
n_conv = np.arange(0, len(conv_result))

# Plot the input signals
plt.figure(figsize=(10, 4))
plt.subplot(311)
plt.stem(n_x, x, basefmt=" ", markerfmt="bo", linefmt="b-", label='x[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Input Signal x[n]')
plt.grid(True)
plt.legend()

plt.subplot(312)
plt.stem(n_h, h, basefmt=" ", markerfmt="ro", linefmt="r-", label='h[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Impulse Response h[n]')
plt.grid(True)
plt.legend()

# Plot the convolution result
plt.subplot(313)
plt.stem(n_conv, conv_result, basefmt=" ", markerfmt="go", linefmt="g-", label='(x * h)[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Convolution Result (x * h)[n]')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()



#python conv.py