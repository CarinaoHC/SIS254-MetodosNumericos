import numpy as np

# Definir la fórmula de Manning
def manning_flow(B, H, n, S):
    return (1 / n) * (B * H**(5/3) * np.sqrt(S)) / ((B + 2 * H)**(2/3))

# Valores dados
B = 20  # ancho en metros
H = 0.3  # profundidad en metros
n = 0.03  # coeficiente de rugosidad
S = 0.0003  # pendiente

# Calcular el flujo Q
Q = manning_flow(B, H, n, S)

# Incertidumbres
sigma_n = 0.003  # ±10% de 0.03
sigma_S = 0.00003  # ±10% de 0.0003

# Derivadas parciales
partial_Q_n = -Q / n
partial_Q_S = 0.5 * Q / S

# Error total
sigma_Q = np.sqrt((partial_Q_n * sigma_n)**2 + (partial_Q_S * sigma_S)**2)

# Resultados
print(f"Flujo Q calculado: {Q:.4f} m³/s")
print(f"Error total en Q debido a incertidumbres: {sigma_Q:.4f} m³/s")
print(f"Derivada parcial de Q respecto a n: {partial_Q_n:.4f}")
print(f"Derivada parcial de Q respecto a S: {partial_Q_S:.4f}")
