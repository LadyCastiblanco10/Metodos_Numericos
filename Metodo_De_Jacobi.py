import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, x0, tol, max_iterations):
    B = np.diag(np.diag(A))
    Lu = A - B
    x = x0
    errors = []  # Lista para almacenar los valores del error en cada iteración
    
    for i in range(max_iterations):
        D_inv = np.linalg.inv(B)
        xtemp = x
        x = np.dot(D_inv, np.dot(-Lu, x)) + np.dot(D_inv, b)
        err = np.linalg.norm(x - xtemp)
        errors.append(err)  # Agregar el error actual a la lista
        
        print("Iteración", i + 1, ": x =", x, "Error =", err)
        
        if err < tol:
            print("Tolerancia alcanzada.")
            break    
    return x


filas = int(input("Ingrese el número de Filas: "))
columnas = int(input("Ingrese el número de Columnas: "))
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input("Fila {}, Columna {} : ".format(i + 1, j + 1)))
        fila.append(valor)
    matriz.append(fila)

print("\nMatriz A:")
for fila in matriz:
    print(fila)


print("\nIngreso del Vector Independiente:")
matrizInd = []
for ind in range(filas):
    dato = float(input("Vector independiente {} fila: ".format(ind + 1)))
    matrizInd.append(dato)
b = matrizInd

# vector solución inicial
print("\nIngreso del Vector Inicial:")
matrizSol = []
for ind in range(filas):
    datoSol = float(input("X{}: ".format(ind + 1)))
    matrizSol.append(datoSol)
x0 = matrizSol


tolerancia = float(input("\nIngrese el error máximo (tolerancia): "))
num_iteraciones = int(input("Ingrese la cantidad de iteraciones máximas: "))

# Llamada a la función jacobi
x = jacobi(np.array(matriz), np.array(b), np.array(x0), tolerancia, num_iteraciones)
print("Solución final:", x)

