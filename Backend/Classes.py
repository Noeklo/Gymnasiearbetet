import numpy as np
from typing import List
from matplotlib.patches import Circle

class CircleObj:

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
        self.circle = Circle((x,y),self.radius)
        self.y_Cords: List[float] = np.empty(100000)
        self.x_Cords: List[float] = np.empty(100000) 
        
    def position(self, i):
        self.circle.set_center((self.x_Cords[i], self.y_Cords[i])) 

class LineObj:

    mass: float = 10**100 
    radius: float = 0
    y_Velocity: float = 0 
    x_Velocity: float = 0 

    def __init__(self, x_Cords: [], y_Cords: []):
        self.y_Cords: np.array = np.array(y_Cords)
        self.x_Cords: np.array = np.array(x_Cords)
        #print(f"{x_Cords}\n{y_Cords}\n")        

    def position(self, i):
        pass