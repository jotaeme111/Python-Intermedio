import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 10, 100) # Genera 100 puntos entre 0 y 10
#print(x)

y = np.sin(x) # Calcula el seno de cada punto
print(y)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Funcion Seno', color='blue', linestyle='-', linewidth=2)
plt.title('Gráfico de la función Seno')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.show()

x = np.arange(0, 5, 0.1)

y1 = x
y2 = x**2
y3 = x**3

plt.figure(figsize=(10,6))
plt.plot(x, y1, label='y = x', color='red', linestyle='-', linewidth=2)
plt.plot(x, y2, label='y = x^2', color='blue', linestyle='-', linewidth=2)
plt.plot(x, y3, label='y = x^3', color='green', linestyle='-', linewidth=2)

plt.title('Multiples Gráficos de Lineas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)

plt.show()

np.random.seed(46)
num_points = 50

x_scatter = np.random.rand(num_points) * 10
y_scatter = 2 * x_scatter + np.random.randn(num_points) * 2

plt.figure(figsize=(7, 5))
plt.scatter(x_scatter, y_scatter, alpha=0.7,s=50, edgecolors='black', label='Datos Aleatorios')
plt.title('Gráfico de Dispersión')
plt.xlabel('Variable independiente')
plt.ylabel('Variable dependiente')
plt.grid(True)

plt.show()


data_hist = np.random.randn(1000) * 15 + 100

plt.figure(figsize=(7,5))
plt.hist(data_hist, bins=30, color='skyblue', edgecolor='black', alpha=0.8)
plt.title('Histograma de datos normales')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75) 
plt.show()

categorias = ['A', 'B', 'C', 'D', 'E']
valores = [23, 45, 56, 12, 39]

plt.figure(figsize=(7,5))
plt.bar(categorias, valores, color='lightgreen', edgecolor='black', alpha=0.8)
plt.title('Gráfico de Barras de Categorías')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.ylim(0, 60)
plt.grid(axis='y', alpha=0.75)
plt.show()
