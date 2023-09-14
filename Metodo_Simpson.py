#Caso 1
import matplotlib.pyplot as plt
import numpy as np

def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de subintervalos debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    sum_odd = np.sum(y[1::2])
    sum_even = np.sum(y[2:-1:2])
    
    integral = (h / 3) * (y[0] + 4 * sum_odd + 2 * sum_even + y[-1])
    
    return integral

# Funcion
def funcion(x):
    return np.sqrt(5 + x**3)

# límites de integración
a = 0
b = 1

#  subintervalos (debe ser un número par)
n = 4

resultado = simpson_rule(funcion, a, b, n)
print("Resultado de la integración usando el método de Simpson:", resultado)

# Graficación de la función
x = np.linspace(a, b, 100)
y = funcion(x)

plt.plot(x, y)
plt.fill_between(x, 0, y, where=(x >= a) & (x <= b), alpha=0.2)
plt.grid(True)
plt.title("Método de Simpson para la Integración")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()