import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import time

start = time.monotonic()

fps = 60 
v = 10
r=0.1
theta = np.pi/4
g = 9.82
zero = 2*np.sin(theta)*v/g

fig, ax = plt.subplots(figsize=(6, 6))
#ball = ax.scatter(0,0)
circle = Circle((0,0),r)


def y_distence(v,t):
    s = np.sin(theta)*v*t - (g*t**2)/2
    return s

def x_distence(v,t):
    s = np.cos(theta)*v*t
    return s

def animation_frame(t):
    ax.cla()
    plt.title("Projectile Motion")  
    plt.grid()
    ax.set_xlim(0,x_distence(v,zero)+5)
    ax.set_ylim(0, x_distence(v,zero)+5)
#    ax.scatter(x_distence(v,t),y_distence(v,t))
    circle = Circle((x_distence(v,t),y_distence(v,t)),r)
    ax.add_patch(circle)


animation = FuncAnimation(fig, func=animation_frame, frames = np.arange(0, zero, 1/fps), interval = 1/fps*1000)

end = time.monotonic()
plt.show()


