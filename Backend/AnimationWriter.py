import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
import time

from Backend.CircleObj import CircleObj
from Backend.Canvas import Canvas
from Backend.Calc import Calc

class AnimationWriter:
    radius = 0.1
    mass = 1
    V_x = 7
    V_y = 7
    x  = 0
    y = 0
    fps = 30

    start = time.monotonic()

    def generate_Frame(self,i):
        self.circle1.position(self.x_Cords[i],self.y_Cords[i])

        return self.circle1.circle, # fps_text 

    canvas1 = Canvas((6,6), fps, "Projectile Motion")
    circle1 = CircleObj(radius,mass,V_x,V_y,x,y)


    canvas1.ax.add_patch(circle1.circle)
    calc1 = Calc(canvas1)
    x_Cords, y_Cords = calc1.generate_Data(circle1)

    canvas1.ax.set_xlim(0, x_Cords[-1]+5)
    canvas1.ax.set_ylim(0, x_Cords[-1]+5)

    def __init__(self):
        None
    #writer = FFMpegWriter(fps=canvas1.fps)
    def generate_Animation(self,):
        ani = FuncAnimation(self.canvas1.fig, func=self.generate_Frame, frames = np.arange(0,len(self.x_Cords)-1, 1), interval = 1000/self.canvas1.fps-self.calc1.getZero(self.circle1)*1400/150, blit = True)
        plt.show()

    #ani.save("Animate1.mp4", writer=writer, dpi=100)

    end = time.monotonic()
    print(end-start)