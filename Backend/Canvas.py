import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.figure import Figure
import matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

matplotlib.use("tkagg")


import tkinter as tk

class Canvas:

    def __init__(self, size: tuple, fps: int, title: str):
        self.size = size
        self.fps = fps
        #self.fig, self.ax = plt.subplots(figsize=size)
        self.fig = Figure(figsize=size, dpi=100)
        self.ax = self.fig.add_subplot()
        self.title = title
        self.tkCanvas = FigureCanvasTkAgg(self.fig, master=self.window)
 

        plt.title(title)  
        plt.grid()

        

        