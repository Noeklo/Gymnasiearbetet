import numpy as np
from typing import List
from Canvas import Canvas
from CircleObj import CircleObj

class Calc:

    def __init__(self, canvas: Canvas):
        self.canvas: Canvas = canvas
        self.timeIncrement: float = 1/canvas.fps
        self.g: float = 9.82
        self.y_Cords: List[float] = np.empty(1000)
        self.x_Cords: List[float] = np.empty(1000)

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
        while self.y_distence(Obj,timeSeconds) >= 0:
            self.y_Cords[i] = np.array(self.y_distence(Obj,timeSeconds))
            self.x_Cords[i] = np.array(self.x_distence(Obj,timeSeconds))
            timeSeconds += self.timeIncrement
            i += 1
        self.y_Cords = self.y_Cords[:(i)]
        self.x_Cords = self.x_Cords[:(i)]
        return  self.x_Cords, self.y_Cords

class Calc2:

    def __init__(self, canvas: Canvas):
        self.canvas: Canvas = canvas
        self.timeIncrement: float = 1/canvas.fps
        self.g: float = 9.82

    def getZero(self, Obj: CircleObj):
        zero = 2*Obj.y_Velocity/self.g 
        return zero

    def linear_Distence(self, Velocity: float, timeSeconds: float):
        distance = Velocity*timeSeconds
        return distance

    def get_Difference(self, Obj1: CircleObj, Obj2: CircleObj, i):
        diff = np.sqrt( (Obj1.x_Cords[i] - Obj2.x_Cords[i])**2 + (Obj1.y_Cords[i] - Obj2.y_Cords[i])**2 ) 
        return diff

    def check_Dif_Less_Than_Diameter(self, Objs: List[CircleObj], i):
        for Obj1 in Objs:
            for Obj2 in Objs:
                diff = self.get_Difference(Obj1, Obj2, i)
                if  diff < (Obj1.radius + Obj2.radius) and diff > 0:
                    return True
                else: 
                    return False 

    def generate_Data(self, *Objs: List[CircleObj]):
        timeSeconds: float = 0
        i: int = 0

        while i < 1000:

            for Obj in Objs:
                if self.check_Dif_Less_Than_Diameter(Objs, i):
                    print("du")
                    pass
                else:
                    Obj.y_Cords[i] = np.array(self.linear_Distence(Obj.y_Velocity, timeSeconds))
                    Obj.x_Cords[i] = np.array(self.linear_Distence(Obj.x_Velocity, timeSeconds))
            timeSeconds += self.timeIncrement
            i += 1
        
        for Obj in Objs:
            Obj.y_Cords = Obj.y_Cords[:(i)]
            Obj.x_Cords = Obj.x_Cords[:(i)]