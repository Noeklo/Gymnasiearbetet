import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.figure import Figure
import matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter

matplotlib.use("tkagg")


import tkinter as tk

class Canvas:
    tkCanvas = None

    def __init__(self, size: tuple, fps: int, title: str):
        self.size = size
        self.fps = fps
        self.fig, self.ax = plt.subplots(figsize=size)

        #self.fig = Figure(figsize=size, dpi=100)
        #self.ax = self.fig.add_subplot()s
        #self.tkCanvas = FigureCanvasTkAgg(fig, master=self.window)
        #self.tkCanvas.get_tk_widget().pack()
        
        self.title = title

        plt.title(title)  
        plt.grid()

    def __init__(self, size: tuple, fps: int, title: str, window: tkinter.Tk = None):
        self.size = size
        self.fps = fps

        self.fig = Figure(figsize=size, dpi=100)
        self.ax = self.fig.add_subplot()
        self.tkCanvas = FigureCanvasTkAgg(self.fig, master=window)
        self.tkCanvas.get_tk_widget().pack()
        
        self.title = title
 

#        plt.title(title)  
#        plt.grid()

        

        