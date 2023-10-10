import numpy as np
import matplotlib.pyplot as plt
# signal 
t1 = [-3,-2,-1,0,1]
a1 = [1,3,0,2,-2]

# time shifting
st = -3
t = np.zeros(len(t1)+abs(st))
a = np.zeros(len(t1)+abs(st))
if st < 0:
    t[:len(t1)] = t1
    for x in range(len(t1), len(t), 1):
        t[x] = t[x-1] + 1
    a[-len(t1):] = a1
else:
    t[-len(t1):] = t1
    for x in range(len(t)-len(t1)-1, -1, -1):
        t[x] = t[x+1] -1
    a[:len(t1)] = a1
plt.figure(figsize=(5,10))
plt.subplot(2,1,1).stem(t1, a1)
plt.title("signal")
plt.subplot(2,1,2).stem(t, a)
plt.title(f"shifting signal t={st}")

plt.show()

# python shifting.py