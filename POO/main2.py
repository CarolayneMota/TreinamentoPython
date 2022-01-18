from cmath import pi
import numpy as np

"""
salarios = np.array((1, 2, 3, 4, 5))

linha1 = [1, 2, 3]
linha2 = [1, 2, 3]
linha3 = [1, 2, 3]

dados = [linha1, linha2, linha3]

matriz = np.array(dados)
print(f'Saphe: {matriz.shape}')
print(f'Matriz:\n', matriz)
print(matriz.ndim) # ndim diz a dimenção

np.dot(A,B) -> para multiplicar matrizes
np.tranpose OU T-> para obter a matriz transposta
A @ B -> multiplicação de matriz
# multiplicar matrizes por escalar
x * a
np.multiply(x,a)
"""


# Crie uma matriz com 5 dimensões e verifique se ela possui 5 dimensões:
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
