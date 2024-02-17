import numpy as np
from typing import List
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.colors import Normalize 

class CircleObj:

    #cmap = plt.get_cmap("bwr")
    cmap = plt.get_cmap("coolwarm")
    norm = Normalize(vmin= 1, vmax=100)

    radius: float = None
    mass: float = None
    y_Velocity: float = None
    x_Velocity: float = None
    x: float = None
    y: float = None
    circle: Circle = None

    def __init__(self, radius: float, mass: float, x_Velocity: float, y_Velocity: float, x: float,y: float):
        self.radius = radius  
        self.mass = mass
        self.y_Velocity = y_Velocity
        self.x_Velocity = x_Velocity
        self.x = x
        self.y = y
        self.color = self.cmap(self.norm(self.mass))
        self.circle = Circle((x,y),self.radius, color = self.color)
        self.y_Cords: List[float] = np.empty(int(1e6))
        self.x_Cords: List[float] = np.empty(int(1e6)) 
    
    def __add__(self, other):
        return self.radius + other.radius
    
    def __sub__(self, other):
        #om det andra föremålet är en cirkel
        if isinstance(other, CircleObj):
            return np.sqrt(np.square(self.x_Cords-other.x_Cords)+np.square(self.y_Cords-other.y_Cords))
            #return np.linalg.norm(np.array([self.x_Cords, self.y_Cords]) - np.array([other.x_Cords, other.y_Cords]), ord=2)
        #om det andra föremålet är en linje dvs en gräns
        else:
            if other.x_Cords[1] == other.x_Cords[2]:
                diff = np.abs(self.x_Cords - other.x_Cords[0])
            else:
                diff = np.abs(self.y_Cords - other.y_Cords[0])
            return diff

    def get_distance(self, other, i):
        if isinstance(other, CircleObj):
            return np.sqrt(np.square(self.x_Cords[i]-other.x_Cords[i])+np.square(self.y_Cords[i]-other.y_Cords[i]))
            #return np.linalg.norm(np.array([self.x_Cords, self.y_Cords]) - np.array([other.x_Cords, other.y_Cords]), ord=2)
        #om det andra föremålet är en linje dvs en gräns
        else:
            if other.x_Cords[1] == other.x_Cords[2]:
                diff = np.abs(other.x_Cords[0] - self.x_Cords[i])
            else:
                diff = np.abs(other.y_Cords[0] - self.y_Cords[i])
            return diff


    def get_kinetic_energy(self):
        velocity = np.sqrt(self.x_Velocity**2 + self.y_Velocity**2)
        kinetic_energy = self.mass*velocity**2/2
        return kinetic_energy
        
    def position(self, i):
        self.circle.set_center((self.x_Cords[i], self.y_Cords[i])) 
    
class LineObj:

    mass: float = 10.0**100 
    radius: float = 0
    y_Velocity: float = 0 
    x_Velocity: float = 0 

    def __init__(self, x_Cords: np.ndarray, y_Cords: np.ndarray):
        self.y_Cords: np.ndarray = np.array(y_Cords)
        self.x_Cords: np.ndarray = np.array(x_Cords)
        #print(f"{x_Cords}\n{y_Cords}\n")         
        
    def get_distance(self, other, i):
        #om andra föremålet är en cirkel
        if isinstance(other, Circle):
            if self.x_Cords[1] == self.x_Cords[2]:
                diff = np.abs(self.x_Cords[0] - other.x_Cords[i])
            else:
                diff = np.abs(self.y_Cords[0] - other.y_Cords[i])
            return diff
        else: 
            return 10**6


    def get_kinetic_energy(self):
        velocity = np.sqrt(self.x_Velocity**2 + self.y_Velocity**2)
        kinetic_energy = self.mass*velocity**2/2
        return kinetic_energy

    def position(self, i):
        pass
    
    def __add__(self, other):
        return self.radius + other.radius
    