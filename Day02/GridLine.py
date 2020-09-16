import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

plt.plot(x1,y1,'r--', label='Students')
plt.title('Demo Title')
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.legend(loc='best')
plt.grid(ls='-', color='black')
plt.grid(which='major', ls='-', color='black')
plt.minorticks_on()
plt.grid(which='minor', ls='--', color='grey')
plt.show()
