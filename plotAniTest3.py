import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import time

start = time.monotonic()

fps = 60 
v = 7
r=0.1
theta = np.pi/4
g = 9.82
zero = 2*np.sin(theta)*v/g

def y_distence(v,t):
    s = np.sin(theta)*v*t - (g*t**2)/2
    return s

def x_distence(v,t):
    s = np.cos(theta)*v*t
    return s

fig, ax1 = plt.subplots(figsize=(6, 6))
circle = Circle((0,0),r)
ax1.add_patch(circle)
frame_count = 0
start_time = time.monotonic()
fps_text = ax1.text(0.1, 0.9, '', transform=ax1.transAxes)

def animation_frame(t):
    global frame_count, start_time
    circle.set_center(((x_distence(v,t),y_distence(v,t))))

    frame_count += 1
    elapsed_time = time.monotonic() - start_time
    current_fps = frame_count / elapsed_time

    # Update the title with the current FPS
    fps_text.set_text(f"FPS: {current_fps:.2f}")
                  
    return circle, fps_text
end = time.monotonic()
print(len(np.arange(0, zero, 1/fps)), zero)

animation = FuncAnimation(fig, func=animation_frame, frames = np.arange(0, zero, 1/fps), interval = 1/(2*fps)*1000 , blit = True, repeat = True)

plt.title("Projectile Motion")  
plt.grid()
ax1.set_xlim(0, x_distence(v,zero)+5)
ax1.set_ylim(0, x_distence(v,zero)+5)
plt.show()


