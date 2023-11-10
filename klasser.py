import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Calc:

    def NsolveODE(self, y_prime: str, point: tuple, end: int, step: float):

        x_Values = np.arange(point[0], end+step, step) 
        y_Values = np.zeros(len(x_Values))

        y_Values[0] = point[1]

        for count, x in enumerate(x_Values):
            y = y_Values[count]
            slope: float = eval(y_prime)
            print(slope)
            if count < len(x_Values)-1:
                y_Values[count+1] = slope*step + y_Values[count] 
                print(y_Values[count+1])
            
        print(x_Values)
        print(y_Values)

        return x_Values, y_Values


class Animation_Writer:

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.lines = []
        self.ys = []
        self.xs = []
        self.count = 0

    def generate_Frame(self,i):
        if i + 1 <= len(self.xs[self.count]):
            self.lines[self.count].set_data(self.xs[self.count][:i], self.ys[self.count][:i])
        else:
            self.count += 1
            
        return tuple(self.lines)


    def generate_Graf(self, x_Values, y_Values):
        self.x_Values = x_Values
        self.y_Values = y_Values
        self.xs.append(list(x_Values))
        self.ys.append(list(y_Values))

        #ln, = plt.plot([], [], markersize = 5,marker = "o", color = "black")
        ln, = plt.plot([], [], markersize = 5, color = "black")
        self.lines.append(ln)
        print(self.lines)

    def run_Animation(self):
        self.ax.set_xlim(-(self.x_Values[-1]+self.padding),self.x_Values[-1]+self.padding)
        self.ax.set_ylim(-(self.x_Values[-1]+self.padding),self.x_Values[-1]+self.padding)
        ani = FuncAnimation(self.fig, func = self.generate_Frame, frames = list(range(len(self.x_Values))), interval = 0, blit = True, repeat = False) 
        plt.grid()
        plt.show()

    padding: int = 30
        
calc = Calc()
ani = Animation_Writer()

# x,y = calc.NsolveODE("x+y", (0,1),10,2/(1+1))
# ani.generate_Graf(x,y)
# x,y = calc.NsolveODE("x+y", (0,1),10,2/(2+1))
# ani.generate_Graf(x,y)

y_prime = "y*(np.cos(x)+4*np.sin(x)*x)"
x,y = calc.NsolveODE(y_prime, (0,1),20,0.01)
ani.generate_Graf(x,y)

# for i in (1,0.5):

#     x,y = calc.NsolveODE(y_prime, (0,1),5,i)
#     ani.generate_Graf(x,y)

ani.run_Animation()
