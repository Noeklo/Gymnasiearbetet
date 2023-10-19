import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
import time

from CircleObj import CircleObj
from Canvas import Canvas
from Calc import Calc

class AnimationWriter:
    
    radius: float = 0.1
    mass: float = 1
    x_Velocity: float = 7
    y_Velocity: float = 7
    x = 0
    y = 0
    fps: int = 60

    canvas1: Canvas = None 
    circle1: CircleObj = None 

    calc1: Calc = None
    x_Cords, y_Cords = None, None

    def generate_Frame(self,i):
        self.circle1.position(self.x_Cords[i],self.y_Cords[i])

        return self.circle1.circle, 

    def __init__(self):
        None

    def generate_Animation(self,):
        self.canvas1 = Canvas((6,6), self.fps, "Projectile Motion")
        self.circle1 = CircleObj(self.radius,self.mass,self.x_Velocity,self.y_Velocity,self.x,self.y)

        self.canvas1.ax.add_patch(self.circle1.circle)
        self.calc1 = Calc(self.canvas1)
        self.x_Cords, self.y_Cords = self.calc1.generate_Data(self.circle1)

        self.canvas1.ax.set_xlim(0, self.x_Cords[-1]+5)
        self.canvas1.ax.set_ylim(0, self.x_Cords[-1]+5)
        #self.writer = FFMpegWriter(fps=self.canvas1.fps)
        self.ani = FuncAnimation(self.canvas1.fig,
                                 func=self.generate_Frame,
                                 frames = np.arange(0,len(self.x_Cords)-1, 1),
                                 interval = 1000/self.canvas1.fps,
                                 blit = True)
                                 
        self.canvas1.tkCanvas.show(block=False)

    def stop_Animation(self,):
        plt.close(self.canvas1.fig)

        #self.ani.save("Animate1.mp4", writer=self.writer, dpi=100)
