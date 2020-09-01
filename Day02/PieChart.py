import matplotlib.pyplot as plt

x = [50,20,10,15,5]
label = ['HTML','JS','CSS','JQ','PHP']
pieexplode = [0.3,0,0,0,0]
plt.pie(x, labels = label, explode=pieexplode, startangle=90)
plt.show()