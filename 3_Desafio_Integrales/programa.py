import numpy as np

def metodo_trapecio(x, y):
    n = len(x) - 1  # Número de subintervalos
    h = (x[-1] - x[0]) / n
    suma = y[0] + y[-1] + 2 * sum(y[1:-1])
    return (h / 2) * suma

def metodo_simpson(x, y):
    n = len(x) - 1  # Número de subintervalos (debe ser par)
    if n % 2 != 0:
        print("El método de Simpson requiere un número par de subintervalos")
        x = x[:-1]
        y = y[:-1]
        n = len(x) - 1
    h = (x[-1] - x[0]) / n
    suma = y[0] + y[-1]
    for i in range(1, n):
        coef = 4 if i % 2 != 0 else 2
        suma += coef * y[i]
    return (h / 3) * suma

# Datos del problema
x = np.array([0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8])
y = np.array([0, 0.85, 1.30, 1.60, 1.87, 2.14, 2.34, 2.52])

# Cálculo del trabajo usando ambos métodos
trabajo_trapecio = metodo_trapecio(x, y)
trabajo_simpson = metodo_simpson(x, y)

print(f"Trabajo calculado con el método del trapecio: {trabajo_trapecio:.3f} lb-in")
print(f"Trabajo calculado con el método de Simpson: {trabajo_simpson:.3f} lb-in")
