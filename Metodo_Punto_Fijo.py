import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
#funcion inicial
def FuncionIn(x):
    f_x = 2*(x**2) - x - 5
    return f_x
#funcion despejada
def Function_Des(x):
    g_x = np.sqrt((x+5)/2)
    return g_x

print('Metodo Punto Fijo \n')

table_PF = []  # Tabla punto fijo
root = []


x = float(input('Por favor, ingrese el valor inicial'))
ErrorM = float(input('Ingrese el error maximo que desea'))
err = 100
Itera = 1;
root.append(x)

while abs(err) > ErrorM:   #Ciclo hasta que el error sea menor al error maximo que se ha ingresado
    xs = Function_Des(x) #Se calcula una nueva iteración
    root.append(xs)
    err = abs((xs - x) / xs) * 100 #se calcula el error relativo
    table_PF.append([Itera,x,xs, abs(FuncionIn(x)),abs(err)])
    x = xs
    Itera +=1

#Tabla

print(tabulate(table_PF, headers=["i", "Xi", "g(Xi)","f(x)", "err %"]))
print('el valor exacto de la raiz es: ',x)

# Grafica
plt.title("Metodo Punto Fijo")
plt.ylabel("Eje X")
plt.xlabel("Eje y")

a = -3  # Empieza el eje x
b = 3 # Termina el eje y
n = 100  # la densidad de puntos para la grafica
xn = np.linspace(a, b, n)  # Se generan los valores de x para construir la grafica
yn = FuncionIn(xn)


plt.plot(xn, yn)  # Grafica la funcion
plt.grid(True)
plt.axhline(0, color="#000000")  
plt.axvline(0, color="#ff0000") 
plt.plot(x, 0, 'ko', label=("Raiz:"))  # Punto de corte x,y

plt.show()