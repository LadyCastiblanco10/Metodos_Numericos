import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


#Formula 
def function(x):
    y = x**3+2*x**2+10*x-20  
    return y

print("METODO SECANTE")

x0 = float(input('Por favor, Introduce el valor de x0 '))
x1 = float(input('Introduce el valor de x1 '))
Nerror = float((input('Introduce el error '))) 

Secante_table = []  
raiz = []
Iter = []
raiz.insert(0, 0)
Iter.insert(0, 0)

i = 0
error = 100

while abs(error) > Nerror:
    Iter.append(i)
    x2 = x1 - (function(x1) * (x1 - x0)) / (function(x1) - function(x0))
    raiz.append(x2)
    x0 = x1
    x1 = x2
    i = i + 1
    error = (raiz[i] - raiz[i - 1])
    Secante_table.append([i,x2,abs(error),function(raiz[i]) ])
# Tabla de de datos
print("Tabla de Datos ")

print(tabulate(Secante_table, headers=["i", "xi", "(xi-1)-xi", "e%"]))
print("La raíz  es: ", x2)

#Grafica
plt.title("Metodo Secante")
plt.ylabel("Eje X")
plt.xlabel("Eje y")

a = -3
b=20
n=100
xn = np.linspace(a, b, n)     
yn = function(xn)
plt.plot(xn, yn)
plt.grid(True)
plt.axhline(0,color="#ff0000")
plt.axvline(0,color="#ff0000")
plt.plot(x2,0, 'ko') 
plt.show()