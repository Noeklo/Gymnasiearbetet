import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.animation import FFMpegWriter
import time

start = time.monotonic()

fps = 60
v = 30
r=0.2
theta = np.pi/4
g = 9.82
timeIncrement = 1/fps
#zero = 2*np.sin(theta)*v/g
#timeValue = np.arange(0, zero, 1/fps)

def y_distence(v,t):
    s = np.sin(theta)*v*t - (g*t**2)/2
    return s

def x_distence(v,t):
    s = np.cos(theta)*v*t
    return s

def generate_Data(v):
    t = 0
    i = 0
    data = np.empty((1000,2))
    print(data)
    while y_distence(v,t) >= 0:
        data[i] = np.array([x_distence(v,t), y_distence(v,t)])
        t += timeIncrement
        i += 1
    data = data[:(i)]
    return data

fig, ax = plt.subplots(figsize=(6, 6))
circle = Circle((0,0),r)
ax.add_patch(circle)

def generate_Frame(cord):
    circle.set_center((cord[0],cord[1]))

    return circle,

data = generate_Data(v)
lastCord = data[-1]

plt.title("Projectile Motion")  
plt.grid()
ax.set_xlim(0, lastCord[0]+5)
ax.set_ylim(0, lastCord[0]+5)

print(data, len(data), "hej2")

writer = FFMpegWriter(fps=fps)

ani = FuncAnimation(fig, func=generate_Frame, frames = data, interval = 1/(fps)*1000 , blit = True)

ani.save("Animate1.mp4", writer=writer, dpi=100)

end = time.monotonic()
print(end-start)