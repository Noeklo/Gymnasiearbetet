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
        self.circles = np.array([])
        self.x_Starts = np.array([])
        self.y_Starts = np.array([])
        self.lim = 10
        

#AnimationWriter construktor för separat matplot fönster
#    def __init__(self, widow: tkinter.Tk = None,):
#        self.window = widow
#        self.canvas1 = Canvas((6,6), self.fps, "Projectile Motion", self.window)


    def generate_Circle(self, x_Velocity: float, y_Velocity: float, x: int, y: int):
        circle1 = CircleObj(self.radius,self.mass,x_Velocity,y_Velocity, x, y)
        self.canvas1.ax.add_patch(circle1.circle)
        self.circles = np.append(self.circles, circle1)
        self.x_Starts = np.append(self.x_Starts, x)
        self.y_Starts = np.append(self.y_Starts, y)
    
    def generate_normal_distrebuted_Circle(self, quantity: int, avrage_velocity: float = 5, standard_deviation_velocity: float = 5, avrage_mass: float = 100, standard_deviation_mass: float = 50):

        random_Number_Generator = np.random.default_rng()

        #Generera random värden i arrays för massorna och hastigheterna 
        normal_distrubuted_masses: np.ndarray = random_Number_Generator.normal(avrage_mass, standard_deviation_mass, quantity)
        normal_distrubuted_x_velocities: np.ndarray = random_Number_Generator.normal(avrage_velocity, standard_deviation_velocity, quantity) 
        normal_distrubuted_y_velocities: np.ndarray = random_Number_Generator.normal(avrage_velocity, standard_deviation_velocity, quantity) 


        normal_distrubuted_x_velocities = np.array([np.round(i) for i in normal_distrubuted_x_velocities])
        normal_distrubuted_y_velocities = np.array([np.round(i) for i in normal_distrubuted_y_velocities])
        normal_distrubuted_masses =  np.array([np.abs(np.round(i)) for i in normal_distrubuted_masses])

        normal_distrubuted_x_velocities = np.where(normal_distrubuted_x_velocities%2==0,-normal_distrubuted_x_velocities, normal_distrubuted_x_velocities )
        normal_distrubuted_y_velocities = np.where(normal_distrubuted_y_velocities%2==0, -normal_distrubuted_y_velocities, normal_distrubuted_y_velocities )

        print((normal_distrubuted_masses))
        print(normal_distrubuted_x_velocities)
        print(normal_distrubuted_y_velocities)

        #Generera alla möjliga koordinater
        all_coordinates = np.array(list(np.ndindex((self.lim-2, self.lim-2))))+1
        
        #blanda koordinaterna
        np.random.shuffle(all_coordinates)

        # välj ut de första "quantity" koordinaterna
        selected_coordinates = all_coordinates[:quantity-1]

        #separera x och y koordinater
        random_x_Cord = selected_coordinates[:, 0]
        random_y_Cord = selected_coordinates[:, 1]

        for index, x in enumerate(random_x_Cord):
            circle1 = CircleObj(self.radius,
                                normal_distrubuted_masses[index],
                                normal_distrubuted_x_velocities[index],
                                normal_distrubuted_y_velocities[index],
                                random_x_Cord[index],
                                random_y_Cord[index])
        

            self.canvas1.ax.add_patch(circle1.circle)
            self.circles = np.append(self.circles, circle1)

            self.x_Starts = np.append(self.x_Starts, random_x_Cord[index])
            self.y_Starts = np.append(self.y_Starts, random_y_Cord[index])
        
        print(quantity)

    def generate_Random_Circle(self, quantity: int):

        random_Number_Generator = np.random.default_rng()

        #Generera random värden i arrays för massorna och hastigheterna 
        masses: int = random_Number_Generator.integers(low=1, high=6, size=quantity)
        random_x_Velocity: int = random_Number_Generator.integers(low=-20, high=20, size=quantity)
        random_y_Velocity: int = random_Number_Generator.integers(low=-20, high=20, size=quantity)
        
        print(random_x_Velocity)
        print(random_y_Velocity)

        # Generate all possible coordinates
        all_coordinates = np.array(list(np.ndindex((self.lim-2, self.lim-2))))+1
        
        # Shuffle the coordinates
        np.random.shuffle(all_coordinates)

        # Take the first 'quantity' coordinates
        selected_coordinates = all_coordinates[:quantity-1]

        # Extract x and y coordinates
        random_x_Cord = selected_coordinates[:, 0]
        random_y_Cord = selected_coordinates[:, 1]

        for index, x in enumerate(random_x_Cord):
            circle1 = CircleObj(self.radius,
                                masses[index],
                                random_x_Velocity[index],
                                random_y_Velocity[index],
                                random_x_Cord[index],
                                random_y_Cord[index])
        

            self.canvas1.ax.add_patch(circle1.circle)
            self.circles = np.append(self.circles, circle1)

            self.x_Starts = np.append(self.x_Starts, random_x_Cord[index])
            self.y_Starts = np.append(self.y_Starts, random_y_Cord[index])


#genererar animation med random cirklar
    def generate_Spec_Animation(self, vectors: List,  Velocity: float = 8, radius: float = 0.1, mass: float = 1):

        self.radius: float = radius
        self.mass: float = mass 

        self.calc1 = Calc2(self.canvas1, self.frames, self.lim)
        self.canvas1.set_Boarders(self.lim) 
        
        self.x_Velocity: float = np.cos(self.calc1.get_angle(vectors))*Velocity
        self.y_Velocity: float = np.sin(self.calc1.get_angle(vectors))*Velocity
        self.generate_Circle(self.x_Velocity, self.y_Velocity, 5,5) # noll vid 75 bredd 540
        self.generate_Circle(0, 0, 7,7) # noll vid 75 bredd 540

        self.circles = np.concatenate((self.circles, self.canvas1.boarders), axis=0)
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

        #self.generate_Random_Circle(quantity)
        self.generate_normal_distrebuted_Circle(quantity, Velocity, 5, mass)
    
        #self.generate_Circle(1,1)
        self.calc1 = Calc2(self.canvas1, self.frames , self.lim)
        self.canvas1.set_Boarders(self.lim) 

        self.circles = np.concatenate((self.circles, self.canvas1.boarders), axis=0)
    
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
         
