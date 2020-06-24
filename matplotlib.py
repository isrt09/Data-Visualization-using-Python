from matplotlib import pyplot as plt
import numpy  as np
import pandas as pd

x = [1, 2, 3, 4, 5]
y = [5, 7, 3, 8, 4]
plt.title('Title text here ...')
plt.xlabels('X Axis Label')
plt.ylabels('Y Axis Label')
plt.grid(TRUE)
plt.bar(x,y)
plt.show()
