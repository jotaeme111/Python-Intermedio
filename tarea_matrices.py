#Con NumPy: 
import numpy as np

def suma_matrices(m1, m2):
    matriz1 = np.array(m1)
    matriz2 = np.array(m2)
    return matriz1 + matriz2

matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    [0, -1, -2]
]

resultado = suma_matrices(matriz_a, matriz_b)
print("\nCon NumPy: \n", "\n", resultado, "\n")

#Sin NumPy:
def suma_matrices(m1, m2):
    resultado = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[i])):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)
    return resultado

matriz_c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_d = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = suma_matrices(matriz_c, matriz_d)
print("\nSin NumPy:\n", "\n", resultado, "\n")
