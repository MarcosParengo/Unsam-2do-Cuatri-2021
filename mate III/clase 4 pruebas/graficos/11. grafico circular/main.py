import matplotlib.pyplot as plt
popularity = [56, 39, 34, 34, 29]
languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
colores = ["#13EAC9","#FC5A50","#AAFF32","#FFD700","#9A0EEA"]
desfase = (0.1, 0, 0, 0, 0)
plt.pie(popularity, labels=languages, autopct="%0.1f %%", colors=colores, explode=desfase)
plt.show()