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

#python floting.py