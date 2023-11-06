import numpy as np
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
        
    def position(self, x,y):
        self.circle.set_center((x,y)) 
