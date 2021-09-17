from matplotlib import pyplot as plt
from matplotlib_venn import venn2
#venn2((1, 0, 1)) no unidos
venn2((1, 1, 1)) #Unidos
"""
El argumento (1,1,1) indica el tamaño relativo de los
tres subconjuntos en este
orden: Ab (izquierda), aB (derecha), AB (intersección). 
Ab = contenido en el grupo A, pero no B
aB = Contenido en el grupo B, pero no A
AB = contenido en los grupos A y B
"""


plt.show()