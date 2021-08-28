import matplotlib.pyplot as plt
import numpy as np
datos_lins = np.array([1, 2, 3, 4, 5, 6, 7, 8])
datos_cuads = datos_lins**2
LinearSegmentedColormap
plt.ion()
plt.figure()
xvals = range(len(datos_lins))
plt.bar(xvals, datos_lins, width = 0.3)
new_xvals = []

for item in xvals:
    new_xvals.append(item+0.3)

plt.bar(new_xvals, datos_cuads, width = 0.3 ,color='red')
plt.figure()
xvals = range(len(datos_lins))
plt.barh(xvals, datos_lins, height = 0.3, color='b')
plt.barh(xvals, datos_cuads, height = 0.3,
left=datos_lins, color='r')

plt.show()