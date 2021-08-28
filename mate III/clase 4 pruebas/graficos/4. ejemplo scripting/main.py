# Importamos matplotlib
import matplotlib.pyplot as plt
# Creamos 2 listas con datos para el gráfico
x = ['Python', 'Java', 'C', 'C++', 'Matlab', 'Octave']
usuarios = [10, 7, 15, 8, 9, 7]
# Uso de la capa de scripting
# No hay necesidad de crear figura y eje antes de trazar
plt.bar(x, usuarios)
plt.title('Usuarios de Lenguajes de Programación')
plt.xlabel('Lenguaje de Programación')
plt.ylabel('Número de usuarios')
plt.show()