import numpy as np

matriz_c = [[1, 2], [3, 4]]
matriz_d = [[5, 6], [7, 8]]

matriz_a = np.array([[[1,2], [3,4]]])
matriz_b = np.array([[[5,6], [7,8]]])

print("Suma: \n", matriz_a + matriz_b)
print("Suma: \n", matriz_c + matriz_d)

#Si no se usa numpy, la suma no funcionaría como se espera porque las matrices no se sumarían elemento a elemento.

def suma_matrices_cuadradas(m1,m2):
    n = len(m1)
    resultado = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)
    return resultado

suma_matrix = suma_matrices_cuadradas(matriz_c,matriz_d)
print(len(matriz_c))
print(suma_matrix)

#TAREA: Hacer una funcion que sume matrices de cualquier tamaño

print('Resta: \n', matriz_a-matriz_b)
print('Multiplicación: \n', matriz_a * matriz_b)

#Funciones de agregación
matriz_e = np.array([[1,2], [3,4], [5,6]])
#De matriz_a
print('Suma total de elemtos: \n', matriz_e.sum())
print('Promedio de todos los elementos: \n, matriz_a.mean())')
print('Valor máximo de la matriz: \n', matriz_e.max())
print('Valor mínimo de la matriz: \n', matriz_e.min())

print("Suma por columna: \n", matriz_e.sum(axis=0))
print('Promedio por fila: \n', matriz_e.mean(axis=1))

arreglo = np.range(12) 
print('Arreglo original: \n', arreglo)

matriz_3x4 = arreglo.reshape(3, 4)
print('Nueva matriz de 3x4: \n', matriz_3x4)

matriz_6x2 = arreglo.reshape(6, 2)
print('Nueva matriz de 6x2: \n', matriz_6x2)