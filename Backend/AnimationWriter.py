import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
import tkinter
import time

from CircleObj import CircleObj
from Canvas import Canvas
from Calc import Calc
from Calc import Calc2

#class AnimationWriter:
#    
#    radius: float = 0.1
#    mass: float = 1
#    x: float = 0
#    y: float= 0
#
##Sätter postion för cirkeln
#    def generate_Frame(self,i: int):
#        self.circle1.position(self.x_Cords[i],self.y_Cords[i])
#
#        return self.circle1.circle, 
#
##ANimationWriter construktor för integrerad matplot i tkinter fönster dvs window parametern 
#    def __init__(self, canvas1: Canvas, window: tkinter.Tk = None, Velocity: float = 7):
#        self.window = window
#        self.canvas1 = canvas1
#        self.x_Velocity: float = np.cos(np.pi/4)*Velocity
#        self.y_Velocity: float = np.sin(np.pi/4)*Velocity
#
#
##AnimationWriter construktor för separat matplot fönster
##    def __init__(self, widow: tkinter.Tk = None,):
##        self.window = widow
##        self.canvas1 = Canvas((6,6), self.fps, "Projectile Motion", self.window)
#
##Kör animationen
#    def generate_Animation(self,):
#        self.circle1 = CircleObj(self.radius,self.mass,self.x_Velocity,self.y_Velocity,self.x,self.y)
#
#        self.canvas1.ax.add_patch(self.circle1.circle)
#        self.calc1 = Calc(self.canvas1)#s
#        .x_Cords, self.y_Cords = self.calc1.generate_Data(self.circle1)
#
#        self.canvas1.ax.set_xlim(0, self.x_Cords[-1]+5)
#        self.canvas1.ax.set_ylim(0, self.x_Cords[-1]+5)
#        #self.writer = FFMpegWriter(fps=self.canvas1.fps)
#        self.ani = FuncAnimation(self.canvas1.fig,
#                                 func=self.generate_Frame,
#                                 frames = np.arange(0,len(self.x_Cords)-1, 1),
#                                 interval = 1000/self.canvas1.fps,
#                                 blit = True)
#        #self.canvas1.draw()
#        #plt.show(block=False)
#        #self.canvas1.ax.plot()s
#        #plt.plot()
#        
##stoppar animationen
#    def stop_Animation(self,):
#        self.ani.event_source.stop()
#        self.canvas1.ax.clear()    
#         
#
#        print("hej")

class AnimationWriter:
    
    radius: float = 0.1
    mass: float = 1
    x: float = 0
    y: float= 0

#Sätter postion för cirkeln
    def generate_Frame(self,i: int):
        self.circle1.position(i)

        return self.circle1.circle, 

#ANimationWriter construktor för integrerad matplot i tkinter fönster dvs window parametern 
    def __init__(self, canvas1: Canvas, window: tkinter.Tk = None, Velocity: float = 7):
        self.window = window
        self.canvas1 = canvas1
        self.x_Velocity: float = np.cos(np.pi/4)*Velocity
        self.y_Velocity: float = np.sin(np.pi/4)*Velocity


#AnimationWriter construktor för separat matplot fönster
#    def __init__(self, widow: tkinter.Tk = None,):
#        self.window = widow
#        self.canvas1 = Canvas((6,6), self.fps, "Projectile Motion", self.window)

    def set_limets(self):
        self.canvas1.ax.set_xlim(0, 10)
        self.canvas1.ax.set_ylim(0, 10)

#Kör animationen
    def generate_Animation(self,):
        self.circle1 = CircleObj(self.radius,self.mass,self.x_Velocity,self.y_Velocity,self.x,self.y)

        self.canvas1.ax.add_patch(self.circle1.circle)
        self.calc1 = Calc2(self.canvas1)#s
        self.calc1.generate_Data(self.circle1)

        print(self.circle1.x_Cords)

        self.set_limets()

        #self.writer = FFMpegWriter(fps=self.canvas1.fps)
        self.ani = FuncAnimation(self.canvas1.fig,
                                 func=self.generate_Frame,
                                 frames = 1000,
                                 interval = 1000/self.canvas1.fps,
                                 blit = True)
        
        #self.canvas1.draw()
        #plt.show(block=False)
        #self.canvas1.ax.plot()s
        #plt.plot()
        
#stoppar animationen
    def stop_Animation(self,):
        self.ani.event_source.stop()
        self.canvas1.ax.clear()    
         

        print("hej")