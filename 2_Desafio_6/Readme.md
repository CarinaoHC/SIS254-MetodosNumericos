## Sistema de Ecuaciones Lineales Mal Condicionado

### Introducción

Este documento presenta un ejemplo sencillo de un sistema de ecuaciones lineales que está mal condicionado. Un sistema mal condicionado es aquel en el que pequeñas variaciones en los coeficientes o en los términos independientes producen grandes cambios en la solución.

### Ejemplo: Sistema de 3x3 sin decimales

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

### Visualización (opcional)
* **Gráficos:** Puedes incluir gráficos 3D para visualizar los planos representados por las ecuaciones y mostrar su casi paralelismo.
* **Animaciones:** Crear animaciones que muestren cómo pequeños cambios en los coeficientes afectan la posición de los planos.

### Código (Octave/MATLAB)
```octave
% ... tu código Octave aquí ...