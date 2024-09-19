import numpy as np
from scipy.linalg import lu

# Definición de las matrices A y b
A = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]])
b = np.array([7.85, -19.3, 71.4])

# Descomposición LU con pivoteo parcial
P, L, U = lu(A)

# Resolución del sistema
y = np.linalg.solve(L, P.T @ b)
x = np.linalg.solve(U, y)

# Impresión de la solución
print("Solución del sistema (LU):\n", x)