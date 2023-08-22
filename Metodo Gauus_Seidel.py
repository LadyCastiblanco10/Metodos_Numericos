import numpy as np

def gauss_seidel_solver(matrix, vector, initial_guess, tolerance=0.001, max_iterations=20):
    m, n = matrix.shape
    x = initial_guess.copy()
    comp = np.zeros(m)
    error = []

    for k in range(max_iterations):
        for r in range(m):
            suma = 0
            for c in range(n):
                if c != r:
                    suma += matrix[r, c] * x[c]
            x[r] = (vector[r] - suma) / matrix[r, r]
            print("x[{}]: {}".format(r, x[r]))

        error.clear()
        for r in range(m):
            suma = np.dot(matrix[r, :], x)
            comp[r] = suma
            dif = abs(comp[r] - vector[r])
            error.append(dif)
            print("Error x[{}]: {}".format(r, error[r]))
        print("Iteraciones:", k + 1)

        if all(e <= tolerance for e in error):
            print("Convergencia alcanzada. El error es menor que la tolerancia.")
            break

    return x

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matrix = np.zeros((filas, columnas))
vector = np.zeros((filas))
x0 = np.zeros(filas)

for i in range(filas):
    print('Vector Inicial')
    print('Introduce vector inicial o iteración 1 ')
    x0[i] = float(input("Elemento x[{}]: ".format(i + 1)))

print('Método de Gauss-Seidel')
print('El elemento a es la matriz del sistema de ecuaciones')
print('El vector b es el vector independiente o las igualdades de las ecuaciones\n')
print('Introduce la matriz de coeficientes y el vector solución\n')

for r in range(filas):
    for c in range(columnas):
        matrix[r, c] = float(input("Elemento a[{}{}]: ".format(r + 1, c + 1)))
    vector[r] = float(input('b[{}]: '.format(r + 1)))

gauss_seidel_solver(matrix, vector, x0)