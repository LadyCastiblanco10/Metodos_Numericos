import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

a = -3         
b = 11           
n = 50   
#Formula original
x = np.linspace(a, b, n)     #Valores de x para construir la grafica
def f(xs):
  f_x = (xs**3)+(2*xs**2)+(10*xs) -20 
  return (f_x)

#Derivada de f(x)
def f1(xs):
  f1_x = (3*xs**2)+(4*xs)+10
  return (f1_x)

emax = float(input('Por favor, ingrese el margen de error que desea'))
x1 = float(input('Por favor, ingrese el valor inicial'))





def NewtonRaphson(x1, es):
    x = x1  # aproximaciones de la raiz
    xv = []  # vector que guarda las aproximaciones de la raiz
    ea = 2 * es  # error absoluto
    eav = []  # vector que guarda el error absoluto
    i = 0  # numero de iteraciones
    niter = []  # vector numero de iteraciones
    fxv = []  # vector de la funcion f(x)
    Newton_table = []  # tabla de datos del metodo newton - raphson

    Newton_table.append([i, x,  "XXXX", "XXXX"])  #colocamos la primera fila de datos en la 1 iteracion
    xv.append(x)

    while ea > es and i <= 7:
        x = x - f(x) / f1(x)  # formula de newton - raphson
        xv.append(x)
        fxv.append(f1(x))
        i += 1
        niter.append(i)


        if x != 0:
            ea = abs((xv[i] - xv[i - 1]))
            er = abs((xv[i] - xv[i - 1]) / xv[i]) * 100  # error relativo
            eav.append(ea)
        Newton_table.append([i, x, ea, er])
    print('El valor  de la raiz es: ',x)

    # Tabla 
    print("Metodo Newton-Raphson")
    print(tabulate(Newton_table, headers=["i", "xi",  "(xi+1-xi)", "e%"]))

    return (x, f(x))
xr, yr = NewtonRaphson(x1, emax)

#Grafica

fx = f(x)

print("Grafica de la funcion")
plt.figure(figsize=(6, 4))
plt.plot(x, fx)
plt.plot(x, np.zeros(len(x)), 'k:')
plt.axvline(0,color="#000000")
plt.plot(xr, yr, 'ko')  #grafica el punto de corte          
plt.title("Grafica Newton Rapson")
plt.legend()                    
plt.grid(True)
plt.show()                     