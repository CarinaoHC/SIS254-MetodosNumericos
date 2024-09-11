import sympy as sp

# Definir la variable simbólica y la función
x = sp.symbols('x')
f = 25*x**3 - 6*x**2 + 7*x - 88

# Calcular las derivadas
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)
f_triple_prime = sp.diff(f_double_prime, x)

# Evaluar las derivadas en x0 = 1
x0 = 1
f_x0 = f.subs(x, x0)
f_prime_x0 = f_prime.subs(x, x0)
f_double_prime_x0 = f_double_prime.subs(x, x0)
f_triple_prime_x0 = f_triple_prime.subs(x, x0)

# Expansión de Taylor hasta tercer orden
def taylor_series(x_val):
    return (f_x0 + 
            f_prime_x0 * (x_val - x0) + 
            f_double_prime_x0 / sp.factorial(2) * (x_val - x0)**2 + 
            f_triple_prime_x0 / sp.factorial(3) * (x_val - x0)**3)

# Calcular la predicción usando la serie de Taylor
x_val = 3
f_approx = taylor_series(x_val)

# Calcular el valor exacto de f en x = 3
f_exact = f.subs(x, x_val)

# Calcular el error relativo porcentual verdadero
error_relativo_porcentual = abs(f_exact - f_approx) / abs(f_exact) * 100

# Imprimir resultados
print(f"Expansión de Taylor hasta tercer orden en x = {x_val}: {f_approx}")
print(f"Valor exacto en x = {x_val}: {f_exact}")
print(f"Error relativo porcentual verdadero: {error_relativo_porcentual:.2f}%")
