import numpy as np
import matplotlib as plt

x_value = 0
y_value = 100

for i in range(0, 10):
    y_value = y_value - 10
    print(y_value)
    plt.scatter(x_value, y_value)
    plt.pause()

plt.show()