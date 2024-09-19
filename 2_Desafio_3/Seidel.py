import numpy as np

# Definición de la matriz A y el vector b
A = np.array([[0.52, 0.2, 0.25], [0.3, 0.5, 0.2], [0.18, 0.3, 0.55]])

b = np.array([4800, 5810, 5690])

x = np.zeros_like(b) 
n_iterations = 100
tolerance = 1e-5

# Método de Gauss-Seidel
print("Resultados de cada iteración:")

for iteration in range(n_iterations):
    x_old = x.copy()

    for i in range(len(b)):
        sigma = sum(A[i][j] * x[j] for j in range(len(b)) if j != i)
        x[i] = (b[i] - sigma) / A[i][i]

    print(f"Iteración {iteration + 1}: {x}")

    # Verificación de la convergencia
    if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
        print(f"Convergió en {iteration + 1} iteraciones.")
        break

# Resultados finales
print("Soluciones finales:")
print(x)
