import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg


plt.figure()
plt.plot(3,3, '.')
plt.plot(3,2, 'o')

ax = plt.gca()
ax.axis([0,10,0,10])#Determinar los ejes de los graficos

x = [0,1,2,3,4,5,6,7,8,9,10]
y = x

colors = ['yellow'] * (len(x)-1)
colors.append('red')

colors2 = ['green'] * (len(x)-1)
colors2.append('blue')

plt.scatter(x, y,s=100,c=colors)
plt.scatter(x, y,s=10,c=colors2)
plt.scatter(x, y,s=1,c=colors)


plt.show()