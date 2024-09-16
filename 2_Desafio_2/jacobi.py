import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def metodo_jacobi(A, b, x0, tol, max_iter):
    # Calcular la matriz de Jacobi (D-L-U)
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    T_jacobi = np.linalg.inv(D) @ (L + U)
    c_jacobi = np.linalg.inv(D) @ b
    
    # Mostrar la matriz despejada y el vector c_jacobi
    print("\nMatriz despejada (T):\n", T_jacobi)
    print("\nVector c_jacobi:\n", c_jacobi)

    # Calcular la norma infinito de T_jacobi
    alfa = np.linalg.norm(T_jacobi, np.inf)
    print("\nAlfa (norma infinito de T):", alfa)
    print()
    
    # Verificar si el método puede converger
    if alfa > 1:
        print("Advertencia: El método de Jacobi puede no converger para esta matriz.")

    # Crear listas para almacenar los resultados
    valores_x = []
    errores = []

    # Iteraciones del método de Jacobi
    for i in range(max_iter):
        x_new = np.dot(T_jacobi, x0) + c_jacobi

        error = np.abs(x_new - x0)
        valores_x.append(x_new)
        errores.append(error)

        if np.linalg.norm(error) < tol:
            break

        x0 = x_new

    # Crear DataFrame con los resultados
    df = pd.DataFrame(valores_x, columns=['x1', 'x2', 'x3'])
    df['e1'] = [error[0] for error in errores]
    df['e2'] = [error[1] for error in errores]
    df['e3'] = [error[2] for error in errores]
    df['error_max'] = [np.max(error) for error in errores]
    
    return df

# Datos del problema
A = np.array([[0.52, 0.2, 0.25], [0.3, 0.5, 0.2], [0.18, 0.3, 0.55]])
b = np.array([4800, 5810, 5690])
x0 = np.zeros(3)
tol = 0.0005
max_iter = 100

# Resolver el sistema
resultados = metodo_jacobi(A, b, x0, tol, max_iter)

pd.set_option('display.max_rows', None)

# Mostrar los resultados
print(resultados)

# Graficar la convergencia del error máximo
plt.plot(range(1, len(resultados)+1), resultados['error_max'])
plt.xlabel('Iteración')
plt.ylabel('Error máximo')
plt.title('Convergencia del método de Jacobi')
plt.show()