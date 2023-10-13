import numpy as np
from matplotlib.patches import Circle

class CircleObj:

    def __init__(self, radius, mass,V_x, V_y, x,y):
        self.radius = radius  
        self.mass = mass
        self.V_y = V_y
        self.V_x = V_x
        self.x = x
        self.y = y
        self.circle = Circle((x,y),self.radius)
        
    def position(self, x,y):
        self.circle.set_center((x,y)) 