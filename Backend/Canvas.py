import numpy as np
from typing import List
from Classes import LineObj 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.figure import Figure
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.colors import Normalize 

# I
# matplotlib.use("qtagg")

import tkinter as tk

class Canvas:

    size: tuple = None
    fps: int  = None
    title: str  = None
    window: tkinter.Tk = None
    fig: mpl.figure.Figure = None
#    ax: mpl.axes._subplots.AxesSubplot = None
    #tkCanvas: mpl.backends.backend_tkagg.FigureCanvasTkAgg = None

    # construktor för canvas objektet
    def __init__(self, size: tuple, fps: int, title: str, window: tkinter.Tk = None) -> None:
        self.size = size
        self.fps = fps
        self.title = title
        self.window = window
        

        if window is not None:
            # Använd Matplotlib i Tkinter window
            self.fig = Figure(figsize=size, dpi=100)
            self.ax = self.fig.add_subplot()
            self.tkCanvas = FigureCanvasTkAgg(self.fig, master=self.window)
            self.tkCanvas.get_tk_widget().pack()

            #färgbar som representerar massan 
            #fråm https://stackoverflow.com/questions/61084381/create-gradient-legend-matplotlib
            cmap = plt.get_cmap("RdYlBu_r")
            norm = Normalize(vmin= 1, vmax=200)
            axins1 = inset_axes(self.ax, width='20%', height='3%', loc = "upper right")
            self.fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), cax=axins1, orientation='horizontal', ticks =[1,200])
        else:
            # använd matplotlib i separat fönster
            self.fig, self.ax = plt.subplots(figsize=size)
            plt.title(title)
            plt.grid()
    
    # Skapar värden för gränserna
    def set_Limets(self, x_Limet: int, y_Limet: int) -> None:
        self.ax.set_xlim(0, x_Limet)
        self.ax.set_ylim(0, y_Limet)

    # Skapar linjer som placeras vid gränserna angivna ovan
    def set_Boarders(self, lim) -> None:
        length = np.linspace(0,lim,lim*1000)

        x_Boarder1: LineObj = LineObj(length, np.zeros(1000))
        x_Boarder2: LineObj = LineObj(length, np.array([lim for _ in range(1000)]))
        y_Boarder1: LineObj = LineObj(np.zeros(1000), length)
        y_Boarder2: LineObj = LineObj(np.array([lim for _ in range(1000)]), length)

        self.boarders = np.array([x_Boarder1,x_Boarder2,y_Boarder1,y_Boarder2])

#        plt.title(title)  
#        plt.grid()

        

        