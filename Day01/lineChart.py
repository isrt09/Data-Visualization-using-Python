import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [2,4,6,8]
plt.plot(x,y, 'ro')
#plt.plot([1,2,3,4],[2,4,6,8], 'r-')
plt.axis([0,5,0,10])
plt.title('Your Title')
plt.show()
