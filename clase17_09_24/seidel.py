import numpy as np

def gauss_seidel(A, b, x0, tol=1e-5, max_iter=100):
    """
    Implementa el método de Gauss-Seidel para resolver un sistema de ecuaciones lineales.

    Args:
        A: Matriz de coeficientes.
        b: Vector de términos independientes.
        x0: Vector inicial de aproximación.
        tol: Tolerancia para la convergencia (opcional, por defecto 1e-5).
        max_iter: Número máximo de iteraciones (opcional, por defecto 100).

    Returns:
        x: Vector solución.
        iteraciones: Número de iteraciones realizadas.
    """

    n = len(b)
    x = x0.copy()

    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += A[i, j] * x[j]
            x[i] = (b[i] - suma) / A[i, i]

        if np.linalg.norm(x - x_old, np.inf) < tol:
            print(f"Convergió en {k+1} iteraciones")
            break

    return x, k+1

# Datos del problema
A = np.array([[3, -0.1, -0.2],
              [0.1, 7, 0.3],
              [0.3, -0.2, 10]])
b = np.array([7.85, -19.3, 71.4])
x0 = np.zeros(3)

# Resolver el sistema
x, iteraciones = gauss_seidel(A, b, x0)

# Imprimir la solución
print("La solución aproximada es:")
print(x)