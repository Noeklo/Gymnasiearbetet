import numpy as np
from typing import List
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.colors import Normalize 

class CircleObj:

    #cmap = plt.get_cmap("bwr")
    cmap = plt.get_cmap("coolwarm")
    norm = Normalize(vmin= 1, vmax=6)

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
        
    def position(self, i):
        self.circle.set_center((self.x_Cords[i], self.y_Cords[i])) 
    
class LineObj:

    mass: float = 10.0**100 
    radius: float = 0
    y_Velocity: float = 0 
    x_Velocity: float = 0 

    def __init__(self, x_Cords: [], y_Cords: []):
        self.y_Cords: np.array = np.array(y_Cords)
        self.x_Cords: np.array = np.array(x_Cords)
        #print(f"{x_Cords}\n{y_Cords}\n")         

    def position(self, i):
        pass
    