import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.animation import PillowWriter
from matplotlib.animation import FFMpegWriter
import time

start = time.monotonic()

fps = 30
v = 15
r=0.2
theta = np.pi/4
g = 9.82
timeIncrement = 1/fps
interval = 1/120
#zero = 2*np.sin(theta)*v/g
#timeValue = np.arange(0, zero, 1/fps)

fig, ax = plt.subplots(figsize=(6, 6))
circle = Circle((0,0),r)

def y_distence(v,t):
    s = np.sin(theta)*v*t - (g*t**2)/2
    return s

def x_distence(v,t):
    s = np.cos(theta)*v*t
    return s

#def generate_Data(v):
#    t = 0
#    data = np.empty((2,2))
#    print(data)
#    while y_distence(v,t) >= 0:
#        data = np.append(data, np.array([[x_distence(v,t), y_distence(v,t)]]), axis=0)
#        t += increment
#    return data

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

def generate_Frame(cord, lastCord):
    ax.cla()
    plt.title("Projectile Motion")  
    plt.grid()
    ax.set_xlim(0, lastCord[0]+5)
    ax.set_ylim(0, lastCord[0]+5)
    circle = Circle((cord[0], cord[1]),r)
    ax.add_patch(circle)

#while y_distence(v,t) >= 0:
#    print(t)
#    print(f"{x_distence(v,t)}     {y_distence(v,t)}")
#    t += timeIncrement
data = generate_Data(v)
lastCord = data[-1]
print(data, len(data), "hej2")

#writer = PillowWriter(fps=fps)
writer = FFMpegWriter(fps=fps)

with writer.saving(fig, "nimate1.mp4", 100):
        for cord in data:
            generate_Frame(cord, lastCord)
            writer.grab_frame()

end = time.monotonic()
print(end-start)

