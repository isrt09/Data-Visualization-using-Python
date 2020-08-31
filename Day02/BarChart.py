import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,4,8,16]
colors = ['red','blue','magenta','yellow','blue']
plt.bar(x,y, edgecolor='blue', color=colors)
plt.show()
