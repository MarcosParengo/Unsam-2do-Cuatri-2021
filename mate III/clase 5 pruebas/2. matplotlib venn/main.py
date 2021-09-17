from matplotlib import pyplot as plt
from matplotlib_venn import venn2,venn2_circles

"""
el subconjunto 10 (Ab) es el de la izquierda (el que pertenece a A pero no a
B); el 01 (aB) , el de la derecha (el que pertenece a B pero no a A); y el 11 (AB),
el del medio (la intersección).
Teniendo esto en cuenta, como primer argumento , también podemos pasarle
como parámetro un diccionario indicando el tamaño de cada uno de
los subconjuntos:
from matplotlib import pyplot 
"""
plt.title ("diagrama de Venn!");

set1 = set(['A','B','C','D'])
set2 = set(['B','C','D','E','F'])

inter=set1&set2
A=set1-(set1&set2)
B=set2-(set1&set2)

diagram=venn2(({"10": len(A), "01": len(inter), "11": len(B)}), set_labels=('Grupo A', 'Grupo B'),set_colors=("red","blue"), alpha=0.6) #set_colors, set_labels y alpha

#Cambiar atributos puntuales de cada conjunto, label texto, patch area
diagram.get_label_by_id("11").set_text("Intersección")
diagram.get_label_by_id("11").set_color("black")

diagram.get_patch_by_id("11").set_alpha(1)
diagram.get_patch_by_id("11").set_color("Yellow")

diagram.get_label_by_id('10').set_text(A)
diagram.get_label_by_id('01').set_text(B)

diagram.get_label_by_id('11').set_text(inter)


#creo circulos, no estan ligados a el grafico de venn, solamente estan superpuestos
c=venn2_circles(subsets=(len(A), len(inter),len(B)), color="#000000", alpha=1, linestyle="-.", linewidth=3)
#cambiar atributos puntuales
c[0].set_lw(3.0)
c[1].set_ls('dotted')
c[1].set_lw(5.0)

plt.show()