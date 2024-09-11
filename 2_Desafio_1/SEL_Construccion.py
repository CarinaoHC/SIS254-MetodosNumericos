import numpy as np
from prettytable import PrettyTable

# Datos de entrada (matriz A y vector B)
A = np.array([[0.52, 0.2, 0.25], [0.3, 0.5, 0.2], [0.18, 0.3, 0.55]])

B = np.array([4800, 5810, 5690])

# Calcular la inversa de A
inv_A = np.linalg.inv(A)

# Calcular el resultado (X = inv(A) * B)
X = np.dot(inv_A, B)

# Crear una tabla para la matriz inversa
table_invA = PrettyTable()
table_invA.field_names = ["Col1", "Col2", "Col3"]
for row in inv_A:
    table_invA.add_row(row)

# Crear una tabla para el resultado
table_result = PrettyTable(["Material", "Volumen (m³)"])
materials = [
    "Arena",
    "Grano fino",
    "Grano grueso",
]  # Adapta los nombres según tus necesidades
for material, volume in zip(materials, X):
    table_result.add_row([material, f"{volume:.4f} m³"])

# Imprimir las tablas
print("Matriz Inversa:")
print(table_invA)
print("\nResultado:")
print(table_result)
