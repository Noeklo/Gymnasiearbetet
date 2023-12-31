import numpy as np
from typing import List
from Canvas import Canvas
from CircleObj import CircleObj

class Calc:

    g: float = 9.82

    def __init__(self, canvas: Canvas):
        self.canvas: Canvas = canvas
        self.timeIncrement: float = 1/canvas.fps

    def getZero(self, Obj: CircleObj):
        zero = 2*Obj.y_Velocity/self.g 
        return zero

    def y_distence(self,Obj: CircleObj, timeSeconds: float):
        distance = Obj.y_Velocity*timeSeconds - (self.g*timeSeconds**2)/2
        return distance

    def x_distence(self,Obj: CircleObj, timeSeconds: float):
        distance = Obj.x_Velocity*timeSeconds
        return distance

    def generate_Data(self, Obj: CircleObj):
        timeSeconds: float = 0
        i = 0
        y_Cords: List[float] = np.empty(1000)
        x_Cords: List[float] = np.empty(1000)
        while self.y_distence(Obj,timeSeconds) >= 0:
            y_Cords[i] = np.array(self.y_distence(Obj,timeSeconds))
            x_Cords[i] = np.array(self.x_distence(Obj,timeSeconds))
            timeSeconds += self.timeIncrement
            i += 1
        y_Cords = y_Cords[:(i)]
        x_Cords = x_Cords[:(i)]
        return  x_Cords, y_Cords