import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Calc:

    def NsolveODE(self, y_prime: str, point: tuple, end: int, step: float) -> tuple:

        x_Values = np.arange(point[0], end+step, step) 
        y_Values = np.zeros(len(x_Values))

        y_Values[0] = point[1]

        for count, x in enumerate(x_Values):
            y = y_Values[count]
            slope: float = eval(y_prime)
            if count < len(x_Values)-1:
                y_Values[count+1] = slope*step + y_Values[count] 
            
        #print(x_Values)
        #print(y_Values)

        return x_Values, y_Values



class Animation_Writer:

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.lines = []
        self.ys = []
        self.xs = []
        self.count = 0

    def set_limets(self):
        x_Padding: float = 0.1 * self.x_Values[-1]
        y_Padding: float = 0.1 * self.y_Values.max() 
        self.ax.set_xlim(self.x_Values[0] - x_Padding, self.x_Values[-1] + x_Padding)
        self.ax.set_ylim(self.y_Values.min() - y_Padding, self.y_Values.max() + y_Padding)
        

    def generate_Frame(self,i):
        if i + 1 <= len(self.xs[self.count]):
            self.lines[self.count].set_data(self.xs[self.count][:i], self.ys[self.count][:i])
        else:
            self.count += 1
            
        return tuple(self.lines)

    def generate_Graf(self, x_Values, y_Values) -> None:
        self.x_Values = x_Values
        self.y_Values = y_Values
        self.xs.append(list(x_Values))
        self.ys.append(list(y_Values))

        #ln, = plt.plot([], [], markersize = 5,marker = "o", color = "black")
        ln, = plt.plot([], [], markersize = 5)
        self.lines.append(ln)

    def run_Animation(self) -> None:
        x_Padding: float = 0.1 * self.x_Values[-1]
        y_Padding: float = 0.1 * self.y_Values.max() 

        self.ax.set_xlim(self.x_Values[0] - x_Padding, self.x_Values[-1] + x_Padding)
        self.ax.set_ylim(self.y_Values.min() - y_Padding, self.y_Values.max() + y_Padding)

        ani = FuncAnimation(self.fig, func = self.generate_Frame, frames = list(range(len(self.x_Values))), interval = 0, blit = True, repeat = False) 

        plt.title("Graf")
        plt.xlabel("x Axis")
        plt.ylabel("y Axis")
        plt.grid()
        plt.show()

    def generate_Axis(self) -> None:
        lineWidth: float = 1 

        x_Axis = np.array([-1000,1000])
        y_Axis = np.array([-1*10**12,1*10**12])
        
        plt.plot(x_Axis, np.zeros(len(x_Axis)), color = "black", linewidth = lineWidth)
        plt.plot(np.zeros(len(y_Axis)), y_Axis, color = "black", linewidth = lineWidth)

    def generate_Plot(self):
        self.set_limets()
        for index, line in enumerate(self.lines):
            plt.plot(self.xs[index], self.ys[index]) 
            plt.show()