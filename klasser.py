import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Calc:

    def NsolveODE(self, y_prime: str, point: tuple, end: int, step: float):

        x_Values = np.arange(point[0], end, step) 
        y_Values = np.zeros(len(x_Values))

        y_Values[0] = point[1]

        for count, x in enumerate(x_Values):
            y = y_Values[count]
            slope: float = eval(y_prime)
            if count < len(x_Values)-1:
                y_Values[count+1] = slope*step + y_Values[count] 

        print(y_Values)
        print(x_Values)

        return x_Values, y_Values

class Animation_Writer:

    fig, ax = plt.subplots()

    x = []
    y = []
    ln, = plt.plot([], [], marker = "o", color = "black")

    def __init__(self, x_Values, y_Values):
        self.x_Values = x_Values
        self.y_Values = y_Values

    def generate_Frame(self,i):
        #print(i)
        self.x.append(self.x_Values[i]) 
        self.y.append(self.y_Values[i])
        self.ln.set_data(self.x, self.y)

        return self.ln,

    def generate_Animation(self):

        print(len(self.x_Values))

        self.ax.set_xlim(-(self.x_Values[-1]+5),self.x_Values[-1]+5)
        self.ax.set_ylim(-(self.x_Values[-1]+5),self.x_Values[-1]+5)
        ani = FuncAnimation(self.fig, func = self.generate_Frame, frames = list(range(len(self.x_Values))), interval = 100, blit = True, repeat = False) 
        plt.grid()
        plt.show()

        
calc = Calc()
x,y = calc.NsolveODE("x**2-y", (0,1),10,0.5)
ani = Animation_Writer(x,y)
ani.generate_Animation()
    
