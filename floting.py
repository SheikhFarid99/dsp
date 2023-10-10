import numpy as np
import matplotlib.pyplot as plt
# signal 
t1 = [-3,-2,-1,0,1]
a1 = [1,3,0,2,-2]

# folding
t = [-x for x in t1]
t = t[::-1]
a = a1[::-1]
plt.figure(figsize=(5,10))
plt.subplot(2,1,1).stem(t1, a1)
plt.title("signal")
plt.subplot(2,1,2).stem(t, a)
plt.title(f"Folding signal")
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# # Generate some example floating-point data
# x = np.linspace(0, 2 * np.pi, 100)  # Generate 100 points between 0 and 2*pi
# y = np.sin(x)                       # Calculate the sine values for x

# # Create a plot
# plt.figure(figsize=(8, 6))  # Optional: Set the figure size
# plt.plot(x, y, label='sin(x)')  # Plot the data with a label
# plt.title('Floating-Point Plot Example')  # Set the title
# plt.xlabel('x')  # Set the x-axis label
# plt.ylabel('y')  # Set the y-axis label
# plt.legend()  # Display the legend

# # Show the plot (you may need to use plt.show() in a script, not in Jupyter Notebook)
# plt.show()


#python floting.py