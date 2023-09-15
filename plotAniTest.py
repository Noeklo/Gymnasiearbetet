import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

start = time.monotonic()

fps = 30
v = 20 
theta = np.pi/3
g = 9.82
zero = 2*np.sin(theta)*v/g

fig, ax = plt.subplots()
ball = ax.scatter(0,0)


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
    ax.set_xlim(0,x_distence(v,zero)+10)
    ax.set_ylim(0, x_distence(v,zero)+10)
    ball = ax.scatter(x_distence(v,t),y_distence(v,t))
    return ball 

animation = FuncAnimation(fig, func=animation_frame, frames = np.arange(0, zero, 1/fps), interval = (1/fps)*1000)

end = time.monotonic()
plt.show()
print(end-start)


