import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

class Canvas:

    def __init__(self, size, fps):
        self.size = size
        self.fps = fps
        fig, ax = plt.subplots(figsize=size)
    
        