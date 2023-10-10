import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from matplotlib.patches import Circle
from matplotlib.animation import FFMpegWriter
import time
from CircleObj import Circle

start = time.monotonic()

circle1 = Circle(0.1, 1, 3.5,3.5, (0,0))
#fps = 30
#v = 7
#r=0.1
theta = np.pi/4
g = 9.82
timeIncrement = 1/fps
zero = 2*np.sin(theta)*v/g

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
    while y_distence(v,t) >= 0:
        data[i] = np.array([x_distence(v,t), y_distence(v,t)])
        t += timeIncrement
        i += 1
    data = data[:(i)]
    return data


def generate_Frame(cord):
    global frame_count, start_time

    circle1.postion(cord)
#    circle.set_center((cord[0],cord[1]))

#    frame_count += 1
#    elapsed_time = time.monotonic() - start_time
#    current_fps = frame_count / elapsed_time
#
#    # Update the title with the current FPS
#    fps_text.set_text(f"FPS: {current_fps:.2f}")

    return circle, # fps_text 

fig, ax = plt.subplots(figsize=(6, 6))
circle = Circle((0,0),r)
ax.add_patch(circle)

#frame_count = 0
#start_time = time.monotonic()
#fps_text = ax.text(0.1, 0.9, '', transform=ax.transAxes)

data = generate_Data(v)
lastCord = data[-1]

plt.title("Projectile Motion")  
plt.grid()
ax.set_xlim(0, lastCord[0]+5)
ax.set_ylim(0, lastCord[0]+5)

#print(data, len(data), "hej2")

#writer = FFMpegWriter(fps=fps)

ani = FuncAnimation(fig, func=generate_Frame, frames = data, interval = 1000/fps-zero*1400/150, blit = True)

plt.show()

#ani.save("Animate1.mp4", writer=writer, dpi=100)

end = time.monotonic()
print(end-start)