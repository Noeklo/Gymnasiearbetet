import numpy as np
from typing import List
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.colors import Normalize 

class TwoDObj:
    radius: float = None
    mass: float = None
    y_Velocity: float = None
    x_Velocity: float = None

    #overwrite som adderar radierna för objekt då de adderas
    def __add__(self, other) -> float:
        return self.radius + other.radius
    
    #retunerar rörelseengergi
    def get_Kinetic_Energy(self) -> float:
        velocity = np.sqrt(self.x_Velocity**2 + self.y_Velocity**2)
        kinetic_energy = self.mass*velocity**2/2
        return kinetic_energy

#En cirkel klass som ärver från klassen ovan
class CircleObj(TwoDObj):

    #Skapar en färgskala
    cmap = plt.get_cmap("RdYlBu_r")
    #Anpassar skalan till värdena för massan
    norm = Normalize(vmin= 1, vmax=200)

    x: float = None
    y: float = None
    circle: Circle = None

    #Construktor
    def __init__(self, radius: float, mass: float, x_Velocity: float, y_Velocity: float, x: float,y: float) -> None:
        self.radius = radius  
        self.mass = mass
        self.y_Velocity = y_Velocity
        self.x_Velocity = x_Velocity
        self.x = x
        self.y = y
        self.color = self.cmap(self.norm(self.mass))
        self.circle = Circle((x,y),self.radius, color = self.color)

        #Skapar tomma listor som sedan kan uppdateras med de olika positionerna för specefika tidpunkter 
        self.y_Cords: List[float] = np.empty(int(1e6))
        self.x_Cords: List[float] = np.empty(int(1e6)) 
        
    #uppdaterar positionen på matlotfönstret
    def position(self, i) -> None:
        self.circle.set_center((self.x_Cords[i], self.y_Cords[i])) 

#En linje klass som ärver från den översta   
class LineObj(TwoDObj):

    def __init__(self, x_Cords: np.ndarray, y_Cords: np.ndarray) -> None:
        self.y_Cords: np.ndarray = np.array(y_Cords)
        self.x_Cords: np.ndarray = np.array(x_Cords)
        self.mass: float = 10.0**100 
        self.radius: float = 0
        self.y_Velocity: float = 0 
        self.x_Velocity: float = 0 
        #print(f"{x_Cords}\n{y_Cords}\n")         

    def position(self, i) -> None:
        pass
    
    