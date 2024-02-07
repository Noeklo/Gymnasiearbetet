import numpy as np
from itertools import combinations
from typing import List
from Canvas import Canvas
from Classes import CircleObj, LineObj
import time


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
        self.data_Multiplier = 5 
        self.timeIncrement: float = 1/(self.data_Multiplier *canvas.fps)
#        self.timeIncrement: float = 1/canvas.fps
        self.g: float = 9.82
        self.frames = frames
        self.lim = lim
        
    def get_angle(self, vectors: List):
        angle: float = np.arctan2(-(vectors[1][1] - vectors[0][1]),(vectors[1][0] - vectors[0][0]))
        return angle 

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

      # If both are circles
        if isinstance(obj_Pair[0], CircleObj) and isinstance(obj_Pair[1], CircleObj):
            diff = np.linalg.norm(np.array([obj_Pair[0].x_Cords[i], obj_Pair[0].y_Cords[i]]) - np.array([obj_Pair[1].x_Cords[i], obj_Pair[1].y_Cords[i]]))
        # If one is a line
        elif isinstance(obj_Pair[0], LineObj) and isinstance(obj_Pair[1], CircleObj):
            # If two x cords are the same, then it is a y-axis
            if obj_Pair[0].x_Cords[1] == obj_Pair[0].x_Cords[2]:
                diff = np.abs(obj_Pair[0].x_Cords[0] - obj_Pair[1].x_Cords[i])
            else:
                diff = np.abs(obj_Pair[0].y_Cords[0] - obj_Pair[1].y_Cords[i])
        elif isinstance(obj_Pair[0], CircleObj) and isinstance(obj_Pair[1], LineObj):
            if obj_Pair[1].x_Cords[1] == obj_Pair[1].x_Cords[2]:
                diff = np.abs(obj_Pair[1].x_Cords[0] - obj_Pair[0].x_Cords[i])
            else:
                diff = np.abs(obj_Pair[1].y_Cords[0] - obj_Pair[0].y_Cords[i])
        # If both are lines
        elif isinstance(obj_Pair[0], LineObj) and isinstance(obj_Pair[1], LineObj):
            diff = 1e10  # Some large value
        return diff

    def get_Coliding_Pairs(self, Objs: List[CircleObj], i):
        coliding_Pairs = []
        obj_Pairs = np.asarray(list(combinations(Objs, 2))) 
        diffs = np.asarray([self.get_Difference(obj_Pair, i) for obj_Pair in obj_Pairs])

        for index, diff in enumerate(diffs):
            if 0 < diff <= (obj_Pairs[index][0].radius + obj_Pairs[index][1].radius)*1.1:
                coliding_Pairs.append(obj_Pairs[index])
            
        return np.array(coliding_Pairs)

    #def get_Coliding_Pairs(self, Objs: List[CircleObj], i):

    #    obj_Pairs = np.asarray(list(combinations(Objs, 2)), dtype=object) 
    #    diffs = np.asarray([self.get_Difference(obj_Pair, i) for obj_Pair in obj_Pairs])

    #    # Hitta index för kolliderande par
    #    #colliding_indices = np.where((0 < diffs) & (diffs <= (obj_Pairs[:, 0].radius + obj_Pairs[:, 1].radius) * 1.1))

    #    # Hitta index för kolliderande par
    #    radii_sum = obj_Pairs[:, 0]+ obj_Pairs[:, 1]
    #    colliding_indices = np.where((0 < diffs) & (diffs <= radii_sum * 1.1))

    #    # Returnera de kolliderande paren
    #    if len(colliding_indices) > 0:
    #        return obj_Pairs[colliding_indices]

    #    return []


    def check_Dif_From_Walls(self, Objs: List[CircleObj], i):
        for obj in Objs:
            if obj.x_Cords[i] >= self.lim:
                pass
            elif obj.y_Cords[i] >= self.lim:
                pass



    def change_Velocity(self, i: int, coliding_Pairs: [CircleObj, CircleObj]):

        vel1 = np.array([coliding_Pairs[0].x_Velocity, coliding_Pairs[0].y_Velocity])
        vel2 = np.array([coliding_Pairs[1].x_Velocity, coliding_Pairs[1].y_Velocity]) 

        # Beräkna avståndet mellan cirklarna
        distance = self.get_Difference(coliding_Pairs, i ) 

        # Beräkna normalvektorn

        #If one is a line
        if isinstance(coliding_Pairs[0], LineObj) and isinstance(coliding_Pairs[1], CircleObj): 
            #If two x cords are the same than it is a y axis
            if coliding_Pairs[0].x_Cords[1] == coliding_Pairs[0].x_Cords[2]: 
                #normal_vector = (coliding_Pairs[1].radius/distance,0)
                normal_vector = (1,0)
            else:
                #normal_vector = (0,coliding_Pairs[1].radius/distance)
                normal_vector = (0,1)

            print(normal_vector)

        if isinstance(coliding_Pairs[0], CircleObj) and isinstance(coliding_Pairs[1], LineObj): 

            if coliding_Pairs[1].x_Cords[1] == coliding_Pairs[1].x_Cords[2]: 
                #normal_vector = (coliding_Pairs[0].radius/distance,0)
                normal_vector = (1,0)
            else:
                #normal_vector = (0,coliding_Pairs[0].radius/distance)
                normal_vector = (0,1)


        if isinstance(coliding_Pairs[0], CircleObj) and isinstance(coliding_Pairs[1], CircleObj):
            normal_vector = ((coliding_Pairs[1].x_Cords[i] - coliding_Pairs[0].x_Cords[i]) /
                            distance, (coliding_Pairs[1].y_Cords[i] - coliding_Pairs[0].y_Cords[i]) / distance)

        elif isinstance(coliding_Pairs[0], LineObj) and isinstance(coliding_Pairs[1], LineObj): 
            normal_vector = (0,0)

        #Bräkna Unit Tanget vektorn       
        tangent_vector = (-normal_vector[1], normal_vector[0])
        # Beräkna kollisionens hastighet längs normalvektorn
        v1_normal = vel1[0] * normal_vector[0] + vel1[1] * normal_vector[1]
        v2_normal = vel2[0] * normal_vector[0] + vel2[1] * normal_vector[1]
        v1_tangent = vel1[0] * tangent_vector[0] + vel1[1] * tangent_vector[1]
        v2_tangent = vel2[0] * tangent_vector[0] + vel2[1] * tangent_vector[1]

        #Anpassning för bevarande av rörelsemängd och kenetisk energi
        new_v1_normal = (v1_normal*(coliding_Pairs[0].mass - coliding_Pairs[1].mass) + 2*coliding_Pairs[1].mass*v1_normal) / (coliding_Pairs[0].mass + coliding_Pairs[1].mass)
        new_v2_normal = (v2_normal*(coliding_Pairs[1].mass - coliding_Pairs[0].mass) + 2*coliding_Pairs[0].mass*v2_normal) / (coliding_Pairs[1].mass + coliding_Pairs[0].mass)

        # Anpassning för bevarande av rörelsemängd och kenetisk energi
        new_v1_normal = (v1_normal * (coliding_Pairs[0].mass - coliding_Pairs[1].mass) + 2 * coliding_Pairs[1].mass * v2_normal) / (coliding_Pairs[0].mass + coliding_Pairs[1].mass)
        new_v2_normal = (v2_normal * (coliding_Pairs[1].mass - coliding_Pairs[0].mass) + 2 * coliding_Pairs[0].mass * v1_normal) / (coliding_Pairs[1].mass + coliding_Pairs[0].mass)

        # Uppdatera hastigheterna
        coliding_Pairs[0].x_Velocity = (normal_vector[0] * new_v1_normal + tangent_vector[0] * v1_tangent)
        coliding_Pairs[0].y_Velocity = (normal_vector[1] * new_v1_normal + tangent_vector[1] * v1_tangent)
        coliding_Pairs[1].x_Velocity = (normal_vector[0] * new_v2_normal + tangent_vector[0] * v2_tangent)
        coliding_Pairs[1].y_Velocity = (normal_vector[1] * new_v2_normal + tangent_vector[1] * v2_tangent)
        
        #print(f"Hastighet: {np.sqrt(coliding_Pairs[0].x_Velocity**2+coliding_Pairs[0].y_Velocity**2)}")
        #print(f"Hastighet: {np.sqrt(coliding_Pairs[1].x_Velocity**2+coliding_Pairs[1].y_Velocity**2)}")

    def generate_Data(self, Objs: List[CircleObj], x_Starts: List[float], y_Starts: List[float]):
        timeSeconds: float = 0
        i: int = 0

        while i < self.frames*self.data_Multiplier:
            #print(f"frame {i}")

            for index, Obj in enumerate(Objs):

                if isinstance(Obj, CircleObj):
                    if i == 0 :
                        Obj.y_Cords[:i+1] = y_Starts[index]
                        Obj.x_Cords[:i+1] = x_Starts[index]
                    else:
                        Obj.y_Cords[i] = self.linear_Distence(Obj.y_Velocity) + Obj.y_Cords[i-1]
                        Obj.x_Cords[i] = self.linear_Distence(Obj.x_Velocity) + Obj.x_Cords[i-1]

            coliding_Pairs: [[CircleObj, CircleObj],] = self.get_Coliding_Pairs(Objs, i)
            if len(coliding_Pairs) > 0: 
                for coliding_Pair in coliding_Pairs:
                    self.change_Velocity(i, coliding_Pair)
                #print("collision")s

            timeSeconds += self.timeIncrement
            i += 1
        
        ##Tar bort oanvända element i koordinat arrayerna

        #vec_cut_Cords = np.vectorize(CircleObj.cut_Cords, otypes=[object])
        #vec_cut_Cords(Objs, i)#snabbare variation av for loopen nedan

        for Obj in Objs:
            Obj.y_Cords = Obj.y_Cords[:(i)]
            Obj.x_Cords = Obj.x_Cords[:(i)]

            #print(f"x cord 1{Obj.x_Cords}")
            #print(f"x cord 2{Obj.y_Cords}")

    #def generate_Data(self, Objs: List[CircleObj], x_Starts: List[float], y_Starts: List[float]):
    #    y_cords = np.array([obj.y_Cords for obj in Objs if isinstance(obj, CircleObj)])
    #    x_cords = np.array([obj.x_Cords for obj in Objs if isinstance(obj, CircleObj)])

    #    # Skapa arrayer för startposition
    #    y_starts = np.array(y_Starts)
    #    x_starts = np.array(x_Starts)

    #    i = 0
    #    while i < self.frames * self.data_Multiplier:
    #        # Uppdatera position med vektorisering
    #        y_cords += self.linear_Distence(Obj.y_Velocity)
    #        x_cords += self.linear_Distence(Obj.x_Velocity)


    #        # Sätt startposition vid första iterationen
    #        y_cords[0] = np.where(i == 0, y_starts, y_cords[0])
    #        x_cords[0] = np.where(i == 0, x_starts, x_cords[0])

    #        # Hitta kollisioner med vektorisering
    #        coliding_pairs = np.array(self.get_Coliding_Pairs(Objs, i))

    #        if len(coliding_pairs) > 0:
    #            # Vektoriserad ändring av hastighet vid kollision
    #            self.change_Velocity(i, coliding_pairs)

    #        time_seconds += self.timeIncrement
    #        i += 1

    #    for Obj in Objs:
    #        Obj.y_Cords = Obj.y_Cords[:(i)]
    #        Obj.x_Cords = Obj.x_Cords[:(i)]

        