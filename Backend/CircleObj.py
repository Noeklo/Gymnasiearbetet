import numpy as np
from matplotlib.patches import Circle

class CircleObj:

    def __init__(self, radius, mass,V_y, V_x, cord):
        self.radius = radius  
        self.mass = mass
        self.V_y = V_y
        self.V_x = V_x
        self.cord = cord
        self.circle = Circle((cord[0],cord[1]), self.radius)

#   def getCircle(self, ax, cord):
#       circle = Circle(cord, self.radius)
#       return circle
        
    def postition(self, cord):
        self.circle.set_cetner((cord[0],cord[1])) 