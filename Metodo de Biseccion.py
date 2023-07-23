import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

# Función inicial
def function(x):
    y = x**3 - 2*x**2 + x + 2
    return y

print('Metodo de Bisección \n')

xi = -3  # Valor inicial para xi (predeterminado)
xu = 3   # Valor inicial para xu (predeterminado)
raiz = []
biseccion_table = []  # Tabla de datos del método de bisección


while True:
    xr = (xi + xu) / 2.0
    print(xr)
    if function(xi) * function(xr) > 0:
        xi = xr
    else:
        xu = xr
    raiz.append(xr)
    if len(raiz) > 1:
        err = float(abs((raiz[-1] - raiz[-2]) / raiz[-1]) * 100)
        biseccion_table.append([len(raiz), xr, err])
        if err < 1e-5:
            break

# Tabla

print(tabulate(biseccion_table, headers=["i", "xr", "E%"]))

print("\n| La raíz exacta es: ", xr, " |")

# Grafica
plt.title("Metodo de Biseccion")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")

a = -3  # donde empieza el eje x
b = 5   # donde termina el eje x
n = 50  # la densidad de puntos para la grafica
xn = np.linspace(a, b, n)  # Se generan los valores de x para construir la grafica
yn = function(xn)
plt.plot(xn, yn)  # grafica la funcion (establece tamaño plano, traza la grafica)
plt.grid(True)
plt.axhline(0, color="#ff0000")  # establece las lineas de origen en x y el color
plt.axvline(0, color="#ff0000")  # establece las lineas de origen en y y el color
plt.plot(xr, 0, 'ko', label=("Raiz Biseccion"))  # grafica el punto de corte x,y

plt.show()