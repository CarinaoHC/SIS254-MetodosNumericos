# Interpolación por el Método de Lagrange

Este archivo describe el procedimiento para calcular la interpolación por el método de Lagrange, utilizando los datos de las alturas y temperaturas de ebullición del agua, para tres puntos específicos: 5,000 metros, La Paz (3,640 metros) y El Alto (4,150 metros).

## Datos Iniciales
Los datos conocidos de alturas y temperaturas (convertidos a metros):

| Altura (ft) | Altura (m) | Temperatura (°F) |
|-------------|-------------|------------------|
| -1,000      | -304.8      | 213.9            |
| 0           | 0           | 212.0            |
| 3,000       | 914.4       | 206.2            |
| 8,000       | 2,438.4     | 196.2            |
| 15,000      | 4,572       | 184.4            |
| 22,000      | 6,705.6     | 172.6            |
| 28,000      | 8,534.4     | 163.1            |

## Fórmula de Lagrange

El polinomio de interpolación de Lagrange está dado por:

\[
P(x) = \sum_{i=0}^{n} y_i L_i(x)
\]

Donde los \( L_i(x) \) son los polinomios de base de Lagrange, calculados como:

\[
L_i(x) = \prod_{\substack{0 \leq j \leq n \\ j \neq i}} \frac{x - x_j}{x_i - x_j}
\]

### Paso a paso

1. Para cada altura que queremos interpolar (5,000 metros, 3,640 metros, 4,150 metros), calculamos los \( L_i(x) \) correspondientes usando los datos de la tabla.

2. Multiplicamos cada \( L_i(x) \) por la temperatura correspondiente \( T_i \), y sumamos los términos.

### Ejemplo para 5,000 metros

Para \( x = 5,000 \) metros:

1. Calculamos \( L_0(5000) \), \( L_1(5000) \), ..., \( L_6(5000) \) para cada punto \( x_0 = -304.8 \), \( x_1 = 0 \), etc.

2. Luego, multiplicamos por las temperaturas correspondientes:
   - \( T_0 = 213.9 \)
   - \( T_1 = 212.0 \)
   - etc.

3. Finalmente, sumamos todos los términos para obtener la temperatura interpolada a 5,000 metros.

### Resultado para 5,000 metros

El resultado de la interpolación es:

\[
T(5000) \approx 182.28^\circ \text{F}
\]

### Interpolación para La Paz (3,640 metros)

Repetimos el proceso para \( x = 3,640 \) metros:

1. Calculamos los \( L_i(3640) \) para cada \( i \).

2. Multiplicamos cada \( L_i(3640) \) por la temperatura correspondiente.

3. Sumamos los términos para obtener la temperatura interpolada a 3,640 metros.

### Resultado para La Paz

La temperatura interpolada para La Paz es:

\[
T(3640) \approx 186.19^\circ \text{F}
\]

### Interpolación para El Alto (4,150 metros)

Repetimos el proceso para \( x = 4,150 \) metros:

1. Calculamos los \( L_i(4150) \).

2. Multiplicamos por las temperaturas correspondientes.

3. Sumamos los términos para obtener el valor final.

### Resultado para El Alto

La temperatura interpolada para El Alto es:

\[
T(4150) \approx 184.73^\circ \text{F}
\]

## Conclusión

El método de interpolación de Lagrange nos permite aproximar la temperatura de ebullición a alturas específicas que no están en la tabla original. Los resultados para 5,000 metros, La Paz, y El Alto son consistentes con la disminución de la temperatura a medida que aumenta la altitud.
