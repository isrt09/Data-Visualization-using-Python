import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)

y1 = 0.08*x**2
y2 = 0.03*x**2

plt.fill_between(x,y1,y2, 'r-')
plt.plot(x,y1, 'r-')
plt.plot(x,y2, 'b-')
plt.show()