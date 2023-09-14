import matplotlib.pyplot as plt
import numpy as np

input("Teniendo en cuenta que la función es e^(x^2)")

# Solicita al usuario los valores de a, b y la cantidad de trapecios
a = float(input("Ingresa el límite inferior (a): "))
b = float(input("Ingresa el límite superior (b): "))
trapecios = int(input("Ingresa la cantidad de trapecios: "))

# Función que representa e^(x^2)
fx = lambda x: np.exp(x**2)

h = (b - a) / trapecios
muestras = trapecios + 1
areaTotal = 0
xi = a

# Cálculo del área utilizando el método del trapecio
for i in range(0, trapecios):
    areaTrapecio = h * (fx(xi) + fx(xi + h)) / 2
    areaTotal += areaTrapecio
    xi += h

# Crear una distribución de puntos equidistantes
xi = np.linspace(a, b, muestras)

# Evaluamos cada punto xi en la función original
fi = fx(xi)

# Salidas
print('Cantidad de trapecios:', trapecios)
print('El resultado de la integral es:', areaTotal)

# Gráfica de puntos de muestra incluyendo los trapecios
plt.plot(xi, fi, 'bo')

# Dibujamos líneas para dividir los trapecios
for i in range(0, muestras):
    plt.axvline(xi[i], color='w')

# Rellenamos los trapecios
plt.fill_between(xi, 0, fi, color='blue')
plt.show()