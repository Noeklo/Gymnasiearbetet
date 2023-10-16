import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
import time

from CircleObj import CircleObj
from Canvas import Canvas
from Calc import Calc

class AnimationWriter:
    radius = 0.1
    mass = 1
    V_x = 7
    V_y = 7
    x  = 0
    y = 0
    fps = 60

    start = time.monotonic()

    def generate_Frame(self,i):
        self.circle1.position(self.x_Cords[i],self.y_Cords[i])

        return self.circle1.circle, # fps_text 

    canvas1 = None 
    circle1 = None 


    calc1 = None
    x_Cords, y_Cords = None, None

    def __init__(self):
        None
    def generate_Animation(self,):
        self.canvas1 = Canvas((6,6), self.fps, "Projectile Motion")
        self.circle1 = CircleObj(self.radius,self.mass,self.V_x,self.V_y,self.x,self.y)


        self.canvas1.ax.add_patch(self.circle1.circle)
        self.calc1 = Calc(self.canvas1)
        self.x_Cords, self.y_Cords = self.calc1.generate_Data(self.circle1)

        self.canvas1.ax.set_xlim(0, self.x_Cords[-1]+5)
        self.canvas1.ax.set_ylim(0, self.x_Cords[-1]+5)
        #self.writer = FFMpegWriter(fps=self.canvas1.fps)
        self.ani = FuncAnimation(self.canvas1.fig, func=self.generate_Frame, frames = np.arange(0,len(self.x_Cords)-1, 1), interval = 1000/self.canvas1.fps, blit = True)
        self.canvas1.tkCanvas.show(block=False)

    def stop_Animation(self,):
        plt.close(self.canvas1.fig)
#   self.calc1.getZero(self.circle1)*1400/150

        #self.ani.save("Animate1.mp4", writer=self.writer, dpi=100)

    end = time.monotonic()
    print(end-start)