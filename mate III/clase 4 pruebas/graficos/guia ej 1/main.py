import matplotlib.pyplot as plt
import numpy as np

poblacion = [440769.2,29702.8,2364409.9,286013.8,394571.1,88554.7,4780.6,1309880.9,37260.6,210881.6,4678.2,50532.1,116067.8]
pais = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia','Ecuador','Guyana','México','Paraguay','Perú','Surinam','Uruguay','Venezuela']

plt.figure()
plt.bar(pais,poblacion)
plt.show()
