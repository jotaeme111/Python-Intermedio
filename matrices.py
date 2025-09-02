import numpy as np

#matriz_uno = [[1, 2, 3], [4, 5, 6]]
#print(matriz_uno[0][1])
#print(matriz_uno)

matriz_2 = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz_2)
print(type(matriz_2))

ceros = np.zeros((3, 4)) 
print('\nMatriz de ceros:\n', '\n',ceros, '\n')

#Hacer una matriz de 1 dimensiones de 2x2
unos = np.ones((2, 2))
print('Matriz de unos:\n', '\n', unos, '\n')

#Hacer una matriz identidad
identidad = np.eye(5)
print('Matriz identidad:\n', '\n', identidad, '\n')

#Hacer un arreglo en un rango:
rango = np.arange(10)
print('Arreglo en un rango:\n', '\n', rango, '\n')

#Hacer una matriz consecutiva del 0 al 8 en una matriz de 3x3
matriz_consecutiva = np.arange(9).reshape(3, 3)
print('Matriz consecutiva:\n', '\n', matriz_consecutiva, '\n')

#Hacer una matriz de valores aleatorios:
aleatorios = np.random.rand(2, 3)
print('Matriz de valores aleatorios:\n', '\n', aleatorios, '\n')

aleatorios_normal = np.random.randn(2, 3)
print('Matriz de valores aleatorios con distribución normal:\n', '\n', aleatorios_normal, '\n')

print('Dimensiones: ', matriz_2.shape)
print('Número de dimensiones: ', matriz_2.ndim)
print('Tipos de datos que contiene la matriz: ', matriz_2.dtype)
print('Tamaño de la matriz: ', matriz_2.size)

#operaciones con matrices
matriz_3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Accediendo al segundo de la segunda fila:', matriz_3[1, 1])
print('Accediendo al ultimo elemento de la matriz:', matriz_3[2, 2])
print('Accediendo al ultimo elemento de la matriz: ', matriz_3[-1, -1])

print('Accediendo a todos los elementos de una fila:', matriz_3[0, :])
print('Accediendo a todos los elementos de una columna:', matriz_3[1, :])
print('Accediendo a todos los elementos de una columna:', matriz_3[2])

print('Accediendo a una columna completa de una matriz: ', matriz_3[:, 0])

print('Accediendo filas 0 y 1 con las columnas 1 y 2: ')
sub_matriz = matriz_3[0:2, 1:3]
print(sub_matriz)

data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
mask = data > 50
print('Imprimiendo solo valores mayores a 50:\n')
print(data[mask])