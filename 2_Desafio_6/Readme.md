## Sistema de Ecuaciones Lineales Mal Condicionado

### Introducción

Este documento presenta un ejemplo sencillo de un sistema de ecuaciones lineales que está mal condicionado. Un sistema mal condicionado es aquel en el que pequeñas variaciones en los coeficientes o en los términos independientes producen grandes cambios en la solución.

### Ejemplo: Sistema de 3x3

**Sistema de ecuaciones:**
10x + 9y + 8z = 27
9x + 8y + 7z = 24
8x + 7y + 6z = 21

**Forma matricial:**

| 10  9  8 |   | x |   | 27 |
|  9  8  7 | * | y | = | 24 |
|  8  7  6 |   | z |   | 21 |

### ¿Por qué está mal condicionado?

* **Coeficientes muy cercanos:** Los coeficientes forman una secuencia, lo que indica una alta correlación entre las filas de la matriz.
* **Dependencia lineal:** Las ecuaciones son casi redundantes, lo que significa que proporcionan esencialmente la misma información.

### Prueba numérica

* **Solución exacta:** Aunque existen infinitas soluciones, una posible es x=1, y=1, z=1.
* **Perturbación:** Al cambiar ligeramente un coeficiente, el sistema puede volverse inconsistente o tener una solución muy diferente.

### Consecuencias del mal condicionamiento
* **Inestabilidad:** Pequeños errores pueden amplificarse significativamente.
* **Dificultad para encontrar la solución exacta:** Métodos numéricos pueden fallar o dar resultados imprecisos.
* **Interpretación geométrica:** Los planos representados por las ecuaciones son casi paralelos, lo que dificulta encontrar su intersección exacta.

### Resumen

Este ejemplo simple demuestra cómo pequeñas variaciones en los coeficientes pueden tener un gran impacto en la solución de un sistema mal condicionado. Es fundamental identificar y manejar estos sistemas para obtener resultados confiables en aplicaciones reales.

### Visualización
* **Gráfico:** 


### Código (Octave/MATLAB)
```octave
A = [10 9 8; 9 8 7; 8 7 6];
b = [27; 24; 21];

% Resolver el sistema
x = inv(A)*b

% Calcular el número de condición
cond(A)

% Verificar la identidad
A*inv(A)

% Calcular el determinante
det(A)

% Perturbar la matriz y resolver nuevamente
A1 = [10 8.98 8; 9 8 7; 8 7 6];
b1 = [27; 24; 21];
x1 = inv(A1)*b1

% Calcular el número de condición y el determinante de la matriz perturbada
cond(A1)
det(A1)
```

### Conclusiones
El código de Octave demuestra claramente cómo un pequeño cambio en un coeficiente de un sistema de ecuaciones mal condicionado puede provocar grandes cambios en la solución. Esto es una característica distintiva de los sistemas mal condicionados y subraya la importancia de identificar y manejar estos sistemas con cuidado.