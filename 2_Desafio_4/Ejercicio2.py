import numpy as np

# Definir la fórmula de Taylor para ln(x) hasta cuarto orden
def taylor_ln(x, x0):
    return ((x - x0) - (1/2) * (x - x0)**2 +
            (1/6) * (x - x0)**3 - (1/24) * (x - x0)**4)

# Valores dados
x_val = 2.5
x0 = 1

# Calcular la expansión de Taylor
f_approx = taylor_ln(x_val, x0)

# Calcular el valor exacto de ln(x) en x = 2.5
f_exact = np.log(x_val)

# Calcular el error relativo porcentual verdadero
error_relativo_porcentual = abs(f_exact - f_approx) / abs(f_exact) * 100

# Imprimir resultados
print(f"Expansión de Taylor hasta cuarto orden en x = {x_val}: {f_approx:.6f}")
print(f"Valor exacto en x = {x_val}: {f_exact:.6f}")
print(f"Error relativo porcentual verdadero: {error_relativo_porcentual:.2f}%")
