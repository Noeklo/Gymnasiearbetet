import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

class Canvas:

    def __init__(self, size: tuple, fps: int, title: str):
        self.size = size
        self.fps = fps
        self.fig, self.ax = plt.subplots(figsize=size)
        self.title = title

        plt.title(title)  
        plt.grid()

        

        