import numpy as np
from matplotlib.patches import Circle

class CircleObj:

    def __init__(self, radius, mass,x_Velocity, y_Velocity, x,y):
        self.radius = radius  
        self.mass = mass
        self.y_Velocity = y_Velocity
        self.x_Velocity = x_Velocity
        self.x = x
        self.y = y
        self.circle = Circle((x,y),self.radius)
        
    def position(self, x,y):
        self.circle.set_center((x,y)) 
