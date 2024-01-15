import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
import tkinter
import time
from typing import List

from Classes import CircleObj, LineObj
from Canvas import Canvas
from Calc import Calc
from Calc import Calc2

class AnimationWriter:

#Sätter postion för cirkeln
    def generate_Frame(self, i: int):
        for circle in self.circles:
            if isinstance(circle, CircleObj):
                circle.position(self.calc1.data_Multiplier*i)

        end2 = time.monotonic_ns()

        #print(f"tid för animationen: {(end2-self.end)/(10**9)}")

        return tuple([circle.circle for circle in self.circles if isinstance(circle, CircleObj)])

#ANimationWriter construktor för integrerad matplot i tkinter fönster dvs window parametern 
    def __init__(self, canvas1: Canvas, window: tkinter.Tk = None):
        self.window = window
        self.canvas1 = canvas1
        self.frames = 1000
        self.circles = []
        self.x_Starts = []
        self.y_Starts = []
        self.lim = 10
        
        self._ = []

#AnimationWriter construktor för separat matplot fönster
#    def __init__(self, widow: tkinter.Tk = None,):
#        self.window = widow
#        self.canvas1 = Canvas((6,6), self.fps, "Projectile Motion", self.window)


    def generate_Circle(self, x, y):
        circle1 = CircleObj(self.radius,self.mass,self.x_Velocity,self.y_Velocity, x, y)
        self.canvas1.ax.add_patch(circle1.circle)
        self.circles.append(circle1)
        self.x_Starts.append(x)
        self.y_Starts.append(y)

    def generate_Random_Circle(self, quantity: int):

        random_Number_Generator = np.random.default_rng()

        masses: int = random_Number_Generator.integers(low=1, high=5, size=quantity)
        random_x_Velocity: int = random_Number_Generator.integers(low=-5, high=5, size=quantity)
        random_y_Velocity: int = random_Number_Generator.integers(low=-5, high=5, size=quantity)

         # Generate all possible coordinates
        all_coordinates = np.array(list(np.ndindex((self.lim-2, self.lim-2))))+1
        
        # Shuffle the coordinates
        np.random.shuffle(all_coordinates)

        # Take the first 'quantity' coordinates
        selected_coordinates = all_coordinates[:quantity]

        # Extract x and y coordinates
        random_x_Cord = selected_coordinates[:, 0]
        random_y_Cord = selected_coordinates[:, 1]

        #Gör en lista med färger 
        colors: List[str] = ["blue", "red"]

        for index, x in enumerate(random_x_Cord):
            random_Color = colors[random_Number_Generator.integers(low=0, high=len(colors), size=1)[0]]
            circle1 = CircleObj(self.radius,
                                masses[index],
                                random_x_Velocity[index],
                                random_y_Velocity[index],
                                random_x_Cord[index],
                                random_y_Cord[index],
                                random_Color)

            self.canvas1.ax.add_patch(circle1.circle)
            self.circles.append(circle1)

            self.x_Starts.append(random_x_Cord[index])
            self.y_Starts.append(random_y_Cord[index])
        

#genererar animation med random cirklar
    def generate_Spec_Animation(self, vectors: List,  Velocity: float = 8, radius: float = 0.1, mass: float = 1):

        self.radius: float = radius
        self.mass: float = mass 

        self.calc1 = Calc2(self.canvas1, self.frames, self.lim)
        self.canvas1.set_Boarders(self.lim) 
        
        self.x_Velocity: float = np.cos(self.calc1.get_angle(vectors))*Velocity
        self.y_Velocity: float = np.sin(self.calc1.get_angle(vectors))*Velocity
        self.generate_Circle(5,5) # noll vid 75 bredd 540

        self.circles += self.canvas1.boarders
   #s 
        start = time.monotonic_ns()
        self.calc1.generate_Data(self.circles, self.x_Starts, self.y_Starts)
        self.end = time.monotonic_ns()

        print(f"{(self.end-start)/(10**9)}")

        self.canvas1.set_Limets(self.lim, self.lim)


        #self.writer = FFMpegWriter(fps=self.canvas1.fps)s
        self.ani = FuncAnimation(self.canvas1.fig,
                                 func=self.generate_Frame,
                                 frames = self.frames,
                                 interval = 1000/self.canvas1.fps,
                                 blit = True,
                                 repeat = False)


#generarar animation med cirklar som har specefik riktning och hastighet 
    def generate_Rnd_Animation(self, quantity: int, Velocity: float = 8, radius: float = 0.1, mass: float = 1, length: float = 1000/60):
        self.radius: float = radius
        self.mass: float = mass 
        self.frames = int(length*60/2)

        self.generate_Random_Circle(quantity)
    
        #self.generate_Circle(1,1)
        self.calc1 = Calc2(self.canvas1, self.frames , self.lim)
        self.canvas1.set_Boarders(self.lim) 

        self.circles += self.canvas1.boarders
        #print(self.circles)
    
        start = time.monotonic_ns()
        self.calc1.generate_Data(self.circles, self.x_Starts, self.y_Starts)
        self.end = time.monotonic_ns()

        print(f"tid för calc: {(self.end-start)/(10**9)}")
        
        self.canvas1.set_Limets(self.lim, self.lim)
    
        #self.writer = FFMpegWriter(fps=self.canvas1.fps)
        self.ani = FuncAnimation(self.canvas1.fig,
                                 func=self.generate_Frame,
                                 frames = self.frames,
                                 interval = 1000/self.canvas1.fps,
                                 blit = True,
                                 repeat = False)

#stoppar animationen
    def stop_Animation(self,):
        self.canvas1.tkCanvas.get_tk_widget().forget()
        #self.ani.event_source.stop()
        self.canvas1.ax.clear()    
        self.circles = []
        self.x_Starts = []
        self.y_Starts = []
         
