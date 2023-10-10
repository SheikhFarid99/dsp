import numpy as np
import matplotlib.pyplot as plt

# signal 1
t1 = [-3,-2,-1,0,1]
a1 = [1,3,0,2,-2]

# signal 2
t2 = [-1,0,1,2,3]
a2 = [-2,1,2,1,-2]

# signal additon
t_min = np.min([np.min(t1), np.min(t2)])
t_max = min = np.max([np.max(t1), np.max(t2)])

# total t length
t_length = abs(t_min)+abs(t_max) + 1

if np.min(t1) > np.min(t2):
    t1, t2 = t2, t1
    a1, a2 = a2, a1

a1_modify = np.zeros(t_length)
a1_modify[:len(a1)] = a1

a2_modify = np.zeros(t_length)
a2_modify[-len(a2):] = a2

a = a1_modify + a2_modify
t = np.arange(t_min, t_max+1)
plt.figure(figsize=(5,10))
plt.subplot(3,1,1).stem(t1, a1)
plt.title("signal 1")
plt.subplot(3,1,2).stem(t2, a2)
plt.title("signal 2")
plt.subplot(3,1,3).stem(t, a)
plt.title("Addition signal")

plt.show()

# python add.py