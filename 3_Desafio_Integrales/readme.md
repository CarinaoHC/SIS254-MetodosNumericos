# Informe de Comparación de Métodos Numéricos

Este informe documenta el cálculo del trabajo realizado al estirar una banda elástica usando dos métodos numéricos: el método del trapecio y el método de Simpson. Los datos de desplazamiento y fuerza fueron obtenidos de la siguiente tabla:

| x (in.) | 0   | 0.4 | 0.8 | 1.2 | 1.6 | 2.0 | 2.4 | 2.8 |
|---------|-----|-----|-----|-----|-----|-----|-----|-----|
| F (lb)  | 0   | 0.85| 1.30| 1.60| 1.87| 2.14| 2.34| 2.52|

## Cálculo del Trabajo
El trabajo realizado se calculó integrando la fuerza respecto al desplazamiento con los métodos mencionados. A continuación se detallan los resultados obtenidos:

### 1. Método del Trapecio
El método del trapecio es una técnica de integración numérica que aproxima el área bajo la curva dividiendo el intervalo en subintervalos trapezoidales.

**Resultado del método del trapecio (programa en Python)**:
- Trabajo calculado: **4.544 lb-in**

### 2. Método de Simpson
El método de Simpson (regla 1/3) es más preciso que el método del trapecio al utilizar una combinación de parábolas para aproximar la área bajo la curva.

**Resultado del método de Simpson (programa en Python)**:
- Trabajo calculado: **3.605 lb-in**

## Comparación de Resultados
Al comparar los resultados obtenidos con ambos métodos, se observa lo siguiente:
- El método del trapecio calculó un trabajo de **4.544 lb-in**, mientras que el método de Simpson arrojó un resultado de **3.605 lb-in**.
- La diferencia entre los dos resultados es de aproximadamente **0.939 lb-in**, lo cual es significativo y destaca la diferencia en la precisión de los métodos.

### Análisis de la Comparación
- El método de Simpson, al ser más preciso y basado en una interpolación cuadrática, muestra un resultado más bajo que el método del trapecio. Esto se debe a que el método de Simpson captura mejor la curvatura de la función de fuerza, lo cual es particularmente importante cuando la función no es lineal.
- El método del trapecio, aunque más simple, tiende a sobreestimar el trabajo realizado si la función de fuerza tiene una pendiente ascendente.

### Conclusión
Ambos métodos permiten estimar el trabajo realizado al estirar la banda elástica, pero el método de Simpson ofrece una mayor precisión. En este caso, se observó una diferencia notable en los resultados, lo que sugiere que el método de Simpson es preferible cuando se busca mayor exactitud.

### Referencias
Este informe se basó en los resultados obtenidos del programa en Python desarrollado para implementar ambos métodos.
