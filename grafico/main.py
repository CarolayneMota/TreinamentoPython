"""
É possivel colocar duois graficos um ao lado do outro
np.random.normal() # pega o desvio padrão 

xpoints = np.array([2, 4, 6, 8, 10, 12, 14])
ypoints = np.array([1, 3, 5, 7, 9, 11, 13])

#plt.plot(xpoints, ypoints, "o") # plt.plot(xpoints, ypoints, maker = "o") para colocar linha e o. é possivel usar mais de um marcador 
#plt.xlabel("Eixo x") # depois do plot
#plt.ylabel("Eixo y") # depois do plot
#plt.grid() # coloca grade e deve ser add depois do plot
#plt.show()
x = np.random.normal(100, 10, 45)
print(x)
# plt.savefig("graficos/grafico.pdf ") # para salvar o grafico

1-Crie um gráfico pizza em Python para mostrar por dia da semana o número de frutas que uma pessoa 
comprou:y = np.array([35, 25, 25, 15])
mylabels = ["Segunda", "Terça",...]
...................
import matplotlib.pyplot as plt
import numpy as np


y = np.array([35, 25, 25, 15, 30])
mylabels = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
plt.pie(y, labels = mylabels)

plt.show()

2 - Crie um gráfico linha em Python para mostrar a relação da quantidade de litros de agua ingerido 
por calorias. 
import matplotlib.pyplot as plt
import numpy as np

y = np.array([4,5,6,4,7,8,7])
x = np.array([140,120,122,150, 100, 106, 172])

plt.plot(x, y) # plt.plot(xpoints, ypoints, maker = "o") para colocar linha e o. é possivel usar mais de um marcador 
plt.xlabel("calorias") # depois do plot
plt.ylabel("quantidade de litros de agua") # depois do plot
plt.grid() # coloca grade e deve ser add depois do plot

plt.show()

"""


import matplotlib.pyplot as plt
import numpy as np

y = np.array([4,5,6,4,7,8,7])
x = np.array([140,120,122,150, 100, 106, 172])

plt.plot(x, y) # plt.plot(xpoints, ypoints, maker = "o") para colocar linha e o. é possivel usar mais de um marcador 
plt.xlabel("calorias") # depois do plot
plt.ylabel("quantidade de litros de agua") # depois do plot
plt.grid() # coloca grade e deve ser add depois do plot

plt.show()
