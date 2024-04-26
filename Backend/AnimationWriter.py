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

    window: tkinter.Tk = None
    canvas1: Canvas = None
    frames: int = None
    circles: np.ndarray = np.array([])
    x_Starts: np.ndarray = np.array([])
    y_Starts: np.ndarray = np.array([])
    lim: int = None

    # ANimationWriter construktor för integrerad matplot i tkinter fönster dvs window parametern 
    def __init__(self, canvas1: Canvas, window: tkinter.Tk = None):
        self.window = window
        self.canvas1 = canvas1
        self.frames = 1000
        self.lim = 10

    # Sätter postionerna för cirklarna vid en specefik bild
    # Denna metod körs av Funcanimation metoden längre ner
    def generate_Frame(self, i: int):
        for circle in self.circles:
            if isinstance(circle, CircleObj):
                circle.position(self.calc1.data_Multiplier*i)

        return tuple([circle.circle for circle in self.circles if isinstance(circle, CircleObj)])

#AnimationWriter construktor för separat matplot fönster
#    def __init__(self, widow: tkinter.Tk = None,):
#        self.window = widow
#        self.canvas1 = Canvas((6,6), self.fps, "Projectile Motion", self.window)

    # Skapar ett av mina cirkel objekt och förser dem med en start värden för postition hastighet med mer.
    # Används då bara en cirkel ska skapas
    def generate_Circle(self, x_Velocity: float, y_Velocity: float, x: int, y: int):
        circle1 = CircleObj(self.radius,self.mass,x_Velocity,y_Velocity, x, y)
        self.canvas1.ax.add_patch(circle1.circle)
        self.circles = np.append(self.circles, circle1)
        self.x_Starts = np.append(self.x_Starts, x)
        self.y_Starts = np.append(self.y_Starts, y)
    
    # Skapar ett antal cirklar vars värden för hastighet, massa och storlek förhåller sig enligt angivna värden för medel och standardavikelse.
    def generate_normal_distrebuted_Circle(self, quantity: int, avrage_velocity: float = 5, standard_deviation_velocity: float = 5,
                                            avrage_mass: float = 100, standard_deviation_mass: float = 50,
                                            avrage_radius: float = 0.02, standard_deviation_radius: float = 0) -> None:

        random_Number_Generator = np.random.default_rng()

        # Generera värden i arrays för massorna, storlek och hastigheterna som är slupade från normalfördelning. OBS separata x och y hastigheter.
        normal_distrubuted_masses: np.ndarray = random_Number_Generator.normal(avrage_mass, standard_deviation_mass, quantity)
        normal_distrubuted_x_velocities: np.ndarray = random_Number_Generator.normal(avrage_velocity, standard_deviation_velocity, quantity) 
        normal_distrubuted_y_velocities: np.ndarray = random_Number_Generator.normal(avrage_velocity, standard_deviation_velocity, quantity) 
        normal_distrubuted_radius: np.ndarray = random_Number_Generator.normal(avrage_radius, standard_deviation_radius, quantity)

        # Avrundar de framtagna värderna till heltal.
        normal_distrubuted_x_velocities = np.array([np.round(i) for i in normal_distrubuted_x_velocities])
        normal_distrubuted_y_velocities = np.array([np.round(i) for i in normal_distrubuted_y_velocities])
        normal_distrubuted_masses = np.array([np.abs(np.round(i)) for i in normal_distrubuted_masses])
        normal_distrubuted_radius = np.array([np.abs(i) for i in normal_distrubuted_radius])

        # ändrar ett slumpmässigt antal av hastigheter till negtivt
        random_x_indencies = random_Number_Generator.integers(0,len(normal_distrubuted_x_velocities), np.random.randint(0, len(normal_distrubuted_x_velocities)))
        random_y_indencies = random_Number_Generator.integers(0,len(normal_distrubuted_y_velocities), np.random.randint(0, len(normal_distrubuted_y_velocities)))
        normal_distrubuted_x_velocities[random_x_indencies] = -normal_distrubuted_x_velocities[random_x_indencies]  
        normal_distrubuted_y_velocities[random_y_indencies] = -normal_distrubuted_y_velocities[random_y_indencies] 
        
        # sätter radien till minst 0.1 som säkerhetsågärd för att inte få för små radier.
        normal_distrubuted_radius = np.where(normal_distrubuted_radius<0.1, 0.1, normal_distrubuted_radius)
        normal_distrubuted_radius = np.where(normal_distrubuted_radius==0.5, 0.49, normal_distrubuted_radius)
        
        #gamalt inte slumpmässigt
#        normal_distrubuted_x_velocities = np.where(np.arange(len(normal_distrubuted_x_velocities))%2==0,-normal_distrubuted_x_velocities, normal_distrubuted_x_velocities )
#        normal_distrubuted_y_velocities = np.where(np.arange(len(normal_distrubuted_x_velocities))%2==0, -normal_distrubuted_y_velocities, normal_distrubuted_y_velocities )

        # Generera alla möjliga koordinater
        all_coordinates = np.array(list(np.ndindex((self.lim-2, self.lim-2))))+1
        
        # blanda koordinaterna
        np.random.shuffle(all_coordinates)

        # välj ut de första "quantity" koordinaterna
        selected_coordinates = all_coordinates[:quantity]

        # Separera x och y koordinater
        random_x_Cord = selected_coordinates[:, 0]
        random_y_Cord = selected_coordinates[:, 1]

        # Skapar cikel objekt med värden från arrayerna som togs fram åvan.
        for index, x in enumerate(random_x_Cord):
            circle1 = CircleObj(normal_distrubuted_radius[index],
                                normal_distrubuted_masses[index],
                                normal_distrubuted_x_velocities[index],
                                normal_distrubuted_y_velocities[index],
                                random_x_Cord[index],
                                random_y_Cord[index])

            # Lägger till cirkeln som skapas på canvasen
            self.canvas1.ax.add_patch(circle1.circle)
            self.circles = np.append(self.circles, circle1)

            # Sparar start positionerna till listor.
            self.x_Starts = np.append(self.x_Starts, random_x_Cord[index])
            self.y_Starts = np.append(self.y_Starts, random_y_Cord[index])
        
    # Äldre variation av åvan metod som var helt slumpmässig       
    def generate_Random_Circle(self, quantity: int):

        random_Number_Generator = np.random.default_rng()

        # Generera random värden i arrays för massorna och hastigheterna 
        masses: int = random_Number_Generator.integers(low=1, high=6, size=quantity)
        random_x_Velocity: int = random_Number_Generator.integers(low=-20, high=20, size=quantity)
        random_y_Velocity: int = random_Number_Generator.integers(low=-20, high=20, size=quantity)
        
        print(random_x_Velocity)
        print(random_y_Velocity)

        # Generate alla koordinater
        all_coordinates = np.array(list(np.ndindex((self.lim-2, self.lim-2))))+1
        
        # Blanda koordinaterna
        np.random.shuffle(all_coordinates)

        # Välj ut koordinater 
        selected_coordinates = all_coordinates[:quantity-1]

        # Separera x och y koordinater
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


    # startar vektorstyrd animation.
    def generate_Spec_Animation(self, vectors: List,  Velocity: float = 8, radius: float = 0.1, mass: float = 1, elastic: bool = True):

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
        self.calc1.generate_Data(self.circles, self.x_Starts, self.y_Starts, elastic)
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


    #startar animation med flertal objekt 
    def generate_Rnd_Animation(self, quantity: int, Velocity: float = 8,avrage_radius: float = 0.1,  mass: float = 1,
                                length: float = 1000/60, standard_deviation_velocity: int = 5, standard_deviation_mass = 50, 
                                standard_deviation_radius: float = 0, elastic: bool = True):
        
        #print(avrage_radius)
        #print(standard_deviation_radius)
        self.mass: float = mass 
        self.frames = int(length*60/2)

        #Skapar cirklar med atributer som är normalfördelade
        #self.generate_Random_Circle(quantity)
        self.generate_normal_distrebuted_Circle(quantity, Velocity, standard_deviation_velocity, mass, standard_deviation_mass, avrage_radius, standard_deviation_radius)
    
        #Skapar en calc klass och lägger till gränser på canvas (dvs hur stort område som ska avgränsas)
        #self.generate_Circle(1,1)
        self.calc1 = Calc2(self.canvas1, self.frames , self.lim)
        self.canvas1.set_Boarders(self.lim) 
        
        #Lägger till gränserna (som är linjer) i arrayn med objekt
        self.circles = np.concatenate((self.circles, self.canvas1.boarders), axis=0)
    
        start = time.monotonic_ns()
        self.calc1.generate_Data(self.circles, self.x_Starts, self.y_Starts, elastic)
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
         
