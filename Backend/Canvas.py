import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.figure import Figure
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTKAgg

matplotlib.use("tkagg")

class Canvas:

    def __init__(self, size: tuple, fps: int, title: str):
        self.size = size
        self.fps = fps
        self.fig, self.ax = plt.subplots(figsize=size)
        self.title = title
        self.tkCanvas = FigureCanvasTKAgg(self.fig, master=root)

        plt.title(title)  
        plt.grid()

        

        