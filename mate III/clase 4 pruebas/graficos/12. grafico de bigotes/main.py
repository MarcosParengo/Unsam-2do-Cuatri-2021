import matplotlib.pyplot as plt
import numpy as np
jap = np.random.uniform(166, 176, 100)
ale = np.random.uniform(175, 185, 100)
arg = np.random.uniform(170, 180, 100)
plt.boxplot([jap, ale, arg],
notch=True, patch_artist=True,
capprops=dict(color="green"),
medianprops=dict(color="orange"),
whiskerprops=dict(color="yellow"))
plt.xticks([1, 2, 3], ['Japón', 'Alemania', 'Argentina'])
plt.ylabel('Estaturas(cm)')
plt.show()