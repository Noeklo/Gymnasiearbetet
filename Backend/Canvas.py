import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.figure import Figure
import matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter

# matplotlib.use("qtagg")


import tkinter as tk

class Canvas:

    def __init__(self, size: tuple, fps: int, title: str, window: tkinter.Tk = None):
        self.size = size
        self.fps = fps
        self.title = title
        self.window = window

        if window is not None:
            # Use Matplotlib in a Tkinter window
            self.fig = Figure(figsize=size, dpi=100)
            self.ax = self.fig.add_subplot()
            self.tkCanvas = FigureCanvasTkAgg(self.fig, master=self.window)
            self.tkCanvas.get_tk_widget().pack()
        else:
            # Use Matplotlib in a standalone window
            self.fig, self.ax = plt.subplots(figsize=size)
            plt.title(title)
            plt.grid()

    def set_Limets(self, x_Limet: int, y_Limet: int):
        self.ax.set_xlim(0, x_Limet)
        self.ax.set_ylim(0, y_Limet)
 

#        plt.title(title)  
#        plt.grid()

        

        