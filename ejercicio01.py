import numpy as np
import matplotlib.pyplot as plt

def matriz_numpy():
    plt.style.use('dark_background') 
    
    matriz = np.random.randint(1, 100, size=(4, 4))
    print("\nMatriz: \n", '\n', matriz)

    sub_matriz = matriz[0:2, -2:]
    print("\nSub-matriz: \n", '\n', sub_matriz, "\n")

    eje_x = np.arange(matriz.shape[1])
    eje_y = matriz[0]

    # Gráfico de líneas:
    plt.figure(figsize = (8, 5))
    plt.plot(eje_x, eje_y, marker = 'o', linestyle = '-', color = 'blue', label = 'Valores de la primera fila')
    plt.title('Gráfico de líneas: ')
    plt.xlabel('Índice de la columna: ')
    plt.ylabel('Valores: ')
    plt.legend()
    plt.grid(True, alpha = 0.3)
    plt.xticks(eje_x)
    plt.show()

    # Histograma: 
    plt.figure(figsize = (7, 5))
    plt.hist(matriz.flatten(), bins = 10, color = 'blue', edgecolor = 'white')
    plt.title('Histograma: ')
    plt.xlabel('Valores: ')
    plt.ylabel('Frecuencia: ')
    plt.grid(axis = 'y', alpha = 0.3)
    plt.show()

matriz_numpy()
