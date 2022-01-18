import numpy as np

# ordem de preferencia de dados informada no array, ou seja, tranforma tudo que tem lá se tiver
# pelo menos um elemento sendo desse tipo de dado <-str, float, int
salarios = np.array((1, 2, 3, 4, 5))
print(salarios)
media = np.mean(salarios)
mediana = np.median(salarios)
desvio_padrao = np.std(salarios)

print(f'Média: {media}, Mediana: {mediana}, Desvio padrão: {desvio_padrao}, Maior: {np.max(salarios)}, Menor: {np.min(salarios)}')
for s in salarios:
    print(s)
