import matplotlib.pyplot as plt
import numpy as np

# Definimos el rango de valores para x
x = np.linspace(-5, 5, 100)

# Ecuaciones de las rectas
y1 = -1.0001*x + 2
y2 = -x + 2

# Graficamos
plt.plot(x, y1, label='y = -1.0001x + 2')
plt.plot(x, y2, label='y = -x + 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sistema de Ecuaciones Lineales Coincidentes')
plt.legend()
plt.grid(True)
plt.show()