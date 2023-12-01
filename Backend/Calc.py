import numpy as np
from itertools import combinations
from typing import List
from Canvas import Canvas
from Classes import CircleObj, LineObj


#gammal
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

    def __init__(self, canvas: Canvas, frames: int, lim: int):
        self.timeIncrement: float = 1/canvas.fps
        self.g: float = 9.82
        self.frames = frames
        self.lim = lim

    def getZero(self, Obj: CircleObj):
        zero = 2*Obj.y_Velocity/self.g 
        return zero

#    def linear_Distence(self, Velocity: float, timeSeconds: float):
#        distance = Velocity*timeSeconds
#        return distance

    def linear_Distence(self, Velocity: float):
        distance = Velocity*self.timeIncrement
        return distance

    def get_Difference(self, obj_Pair, i):
        diff: float = None
        if isinstance(obj_Pair[0], CircleObj) and isinstance(obj_Pair[1], CircleObj):
            diff = np.sqrt( (obj_Pair[0].x_Cords[i] - obj_Pair[1].x_Cords[i])**2 + (obj_Pair[0].y_Cords[i] - obj_Pair[1].y_Cords[i])**2 ) 
        elif isinstance(obj_Pair[0], LineObj) and isinstance(obj_Pair[1], CircleObj): 
            diff = np.sqrt( (obj_Pair[0].x_Cords[0] - obj_Pair[1].x_Cords[i])**2 + (obj_Pair[0].y_Cords[0] - obj_Pair[1].y_Cords[i])**2 ) 
        elif isinstance(obj_Pair[0], CircleObj) and isinstance(obj_Pair[1], LineObj): 
            diff = np.sqrt( (obj_Pair[0].x_Cords[i] - obj_Pair[1].x_Cords[0])**2 + (obj_Pair[0].y_Cords[i] - obj_Pair[1].y_Cords[0])**2 ) 
        elif isinstance(obj_Pair[0], LineObj) and isinstance(obj_Pair[1], LineObj): 
            diff = 10**10
        return diff

    def get_Coliding_Pairs(self, Objs: List[CircleObj], index, i):

        obj_Pairs = np.asarray(list(combinations(Objs, 2))) 
        diffs = np.asarray([self.get_Difference(obj_Pair, i) for obj_Pair in obj_Pairs])

        for index, diff in enumerate(diffs):
            if 0 < diff < (obj_Pairs[index][0].radius + obj_Pairs[index][1].radius):
                return obj_Pairs[index]

        return []

    def check_Dif_From_Walls(self, Objs: List[CircleObj], i):
        for obj in Objs:
            if obj.x_Cords[i] >= self.lim:
                pass
            elif obj.y_Cords[i] >= self.lim:
                pass

    def change_Velocity(self, coliding_Pairs: [[CircleObj]]):
        coliding_Pairs[0].x_Velocity = -coliding_Pairs[0].x_Velocity 
        coliding_Pairs[0].y_Velocity = -coliding_Pairs[0].y_Velocity 
        
        coliding_Pairs[1].x_Velocity = -coliding_Pairs[1].x_Velocity 
        coliding_Pairs[1].y_Velocity = -coliding_Pairs[1].y_Velocity 
        #unit_Normal_Angle: float = np.arctan((coliding_Objs[1].y_Cords[i] - coliding_Objs[2].y_Cords[i]) / (coliding_Objs[1].x_Cords[i] - coliding_Objs[2]))
        #unit_Tangent_Angle: float = unit_Tangent_Angle + (np.pi / 2) 
        #print("collision")#


    def generate_Data(self, Objs: List[CircleObj], x_Starts: List[float], y_Starts: List[float]):
        timeSeconds: float = 0
        i: int = 0

        while i < 1000:
            #print(f"frame {i}")

            for index, Obj in enumerate(Objs):
                print(type(Obj))
                if isinstance(Obj, CircleObj):
                    if i == 0 :
                        Obj.y_Cords[0] = y_Starts[index]                
                        Obj.x_Cords[0] = x_Starts[index]                
                    else:
                        Obj.y_Cords[i] = self.linear_Distence(Obj.y_Velocity) + Obj.y_Cords[i-1]
                        Obj.x_Cords[i] = self.linear_Distence(Obj.x_Velocity) + Obj.x_Cords[i-1]

            coliding_Pairs: List[CircleObj] = self.get_Coliding_Pairs(Objs, index, i)
            if len(coliding_Pairs) > 0: 
                
                self.change_Velocity(coliding_Pairs)

            timeSeconds += self.timeIncrement
            i += 1

        #Tar bort oanvända element i arrayen
        for Obj in Objs:
            Obj.y_Cords = Obj.y_Cords[:(i)]
            Obj.x_Cords = Obj.x_Cords[:(i)]
#            print(f"x cord 1{Obj.x_Cords}")
#            print(f"x cord 2{Obj.y_Cords}")

        