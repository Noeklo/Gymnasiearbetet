import numpy as np
import matplotlib.pyplot as plt
import time as time


x_value = 0
y_value = 100
fps = 60
totTime = 5
v = 0 
g = 9.82

def y_distence(v,t):
    s = v*t + (g*t**2)/2
    return s

def velocety(v,t):
    v_2 = v + g*t
    return v_2

start = time.time()
for t in np.linspace(0, totTime, fps*totTime):
    plt.clf()
    plt.ylim(-10,110)
    y_value -= y_distence(v,t)
    plt.scatter(x_value, y_value)
    plt.pause(time/(fps*totTime))
    if y_value <= 0:
        end = time.time()
        break

plt.show()

print(y_value)
print(end - start)
#xpoints = np.array([0, 6])
#ypoints = np.array([0, 250])
#
#plt.plot(xpoints, ypoints)
#plt.show()
