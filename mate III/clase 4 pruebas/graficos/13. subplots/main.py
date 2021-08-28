import matplotlib.pyplot as plt
import numpy as np

y = np.random.randn(100).cumsum()
fig,ax=plt.subplots(3,2)
fig.set_size_inches(8,6)
ax[1,0].plot(y)
plt.show()
