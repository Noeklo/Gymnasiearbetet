import numpy as np
from Backend.Canvas import Canvas
from Backend.CircleObj import CircleObj

class Calc:
    g = 9.82

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.timeIncrement = 1/canvas.fps

    def getZero(self, Obj: CircleObj):
        zero = 2*Obj.V_y/self.g 
        return zero

    def y_distence(self,Obj: CircleObj, t):
        s = Obj.V_y*t - (self.g*t**2)/2
        return s

    def x_distence(self,Obj: CircleObj, t):
        s = Obj.V_x*t
        return s

    def generate_Data(self, Obj: CircleObj):
        t = 0
        i = 0
        y_Cords = np.empty(1000)
        x_Cords = np.empty(1000)
        while self.y_distence(Obj,t) >= 0:
            y_Cords[i] = np.array(self.y_distence(Obj,t))
            x_Cords[i] = np.array(self.x_distence(Obj,t))
            t += self.timeIncrement
            i += 1
        y_cords = y_Cords[:(i)]
        x_Cords = x_Cords[:(i)]
        return  x_Cords, y_Cords