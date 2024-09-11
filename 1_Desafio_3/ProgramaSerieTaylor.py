import sympy as sp, math

def taylor_series(f, x0, x_val, tol=0.0005, max_iter=100):
    x = sp.symbols('x')
    taylor_approx = 0 
    h = x_val - x0
    error = float('inf')
    i = 0 
    actual_value = f.subs(x, x_val).evalf()
    
    while abs(error) > tol and i < max_iter:
        f_deriv = f.diff(x, i).subs(x, x0).evalf()
        taylor_approx += (f_deriv / sp.factorial(i)) * h**i
        # Calcular el error
        error = taylor_approx - actual_value
        i += 1
        
        print(f"Iteración {i}: Aproximación de Taylor = {taylor_approx}, Error = {abs(error)}")
    
    return taylor_approx, i

# Ejemplo de uso: 
x = sp.symbols('x')
f_ln = sp.ln(x)  # Función ln(x)
#f_cos = sp.cos(x)
#f_sin = sp.sin(x)
#f_exp = sp.exp(x)
print("\nSERIE DE TAYLOR DE F(X) = LN(X)")

approximation, iterations = taylor_series(f_ln, x0=1, x_val=2, tol=0.0005)

print(f"\nAproximación final: {approximation}")
print(f"Número de iteraciones: {iterations}")
