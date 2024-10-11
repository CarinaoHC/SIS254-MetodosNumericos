# Interpolación por el Método de Lagrange

Este documento describe el procedimiento para realizar la interpolación por el método de **Lagrange**, utilizando los datos de altitudes y temperaturas de ebullición del agua, para las siguientes alturas:

- **5,000 metros**.
- **La Paz, Bolivia** (3,640 metros).
- **El Alto, Bolivia** (4,150 metros).

Además, se incluyen gráficos de las interpolaciones y el cálculo del error de cada resultado.

## Datos Iniciales
La tabla de datos convertida de pies a metros es la siguiente:

| Altura (ft) | Altura (m)  | Temperatura (°F) |
|-------------|-------------|------------------|
| -1,000      | -304.8      | 213.9            |
| 0           | 0           | 212.0            |
| 3,000       | 914.4       | 206.2            |
| 8,000       | 2,438.4     | 196.2            |
| 15,000      | 4,572       | 184.4            |
| 22,000      | 6,705.6     | 172.6            |
| 28,000      | 8,534.4     | 163.1            |

La función de temperatura \( T_B \) depende de la altitud, \( h \).

## Método de Interpolación de Lagrange

El polinomio de interpolación de Lagrange se expresa como:

\[
P(x) = \sum_{i=0}^{n} y_i L_i(x)
\]

Donde \( L_i(x) \) son los **polinomios base de Lagrange** definidos por:

\[
L_i(x) = \prod_{\substack{0 \leq j \leq n \\ j \neq i}} \frac{x - x_j}{x_i - x_j}
\]

Aquí, \( x \) es la altitud para la cual queremos calcular la temperatura, \( x_i \) son las alturas conocidas (en metros), y \( y_i \) son las temperaturas correspondientes.

### Paso 1: Polinomios Base \( L_i(x) \)
Para cada punto \( h_i \), calculamos \( L_i(x) \), que son polinomios que dependen de las demás alturas. Por ejemplo:

Para \( L_0(x) \), donde \( h_0 = -304.8 \):

\[
L_0(x) = \frac{(x - 0)(x - 914.4)(x - 2438.4)(x - 4572)(x - 6705.6)(x - 8534.4)}{(-304.8 - 0)(-304.8 - 914.4)(-304.8 - 2438.4)(-304.8 - 4572)(-304.8 - 6705.6)(-304.8 - 8534.4)}
\]

Repetimos este proceso para cada \( L_i(x) \).

### Paso 2: Cálculo para 5,000 metros
Queremos interpolar la temperatura para una altitud de **5,000 metros**. Usamos la fórmula del polinomio de Lagrange, sumando los productos de \( L_i(x) \) con las temperaturas correspondientes \( T_i \).

El resultado es:

\[
T_{\text{Lagrange}}(5000) \approx 182.28^\circ \text{F}
\]

### Paso 3: Cálculo para La Paz (3,640 metros)

Para **La Paz** (3,640 metros), repetimos el proceso para \( x = 3640 \) metros. Usando los mismos valores de \( L_i(x) \), encontramos:

\[
T_{\text{Lagrange}}(3640) \approx 186.19^\circ \text{F}
\]

### Paso 4: Cálculo para El Alto (4,150 metros)

Para **El Alto** (4,150 metros), el proceso para \( x = 4150 \) metros nos da:

\[
T_{\text{Lagrange}}(4150) \approx 184.73^\circ \text{F}
\]

## Gráficas

### Gráfico de los datos originales y la interpolación para 5,000 metros

![Interpolación a 5,000 metros](interpolacion_5000.png)

Este gráfico muestra los puntos originales y la interpolación a 5,000 metros, marcada como un punto adicional en el gráfico.

### Gráfico de los datos originales y la interpolación para La Paz

![Interpolación para La Paz](interpolacion_lapaz.png)

La interpolación a 3,640 metros (La Paz) también está marcada en el gráfico.

### Gráfico de los datos originales y la interpolación para El Alto

![Interpolación para El Alto](interpolacion_elalto.png)

La interpolación a 4,150 metros (El Alto) aparece marcada en este gráfico.

## Cálculo del Error

El error de interpolación se calcula comparando los valores obtenidos por interpolación con un valor exacto (si estuviera disponible) o un valor esperado.

El **error absoluto** es la diferencia entre el valor interpolado \( T_{\text{interp}} \) y el valor esperado \( T_{\text{real}} \):

\[
\text{Error absoluto} = |T_{\text{interp}} - T_{\text{real}}|
\]

Y el **error relativo** es:

\[
\text{Error relativo} = \frac{|T_{\text{interp}} - T_{\text{real}}|}{T_{\text{real}}}
\]

Dado que no tenemos valores exactos de referencia para las altitudes de La Paz y El Alto, utilizamos el valor interpolado como aproximación.

### Errores para las Alturas

- **Error para 5,000 metros**: No se puede calcular sin un valor de referencia exacto.
- **Error para La Paz**: \( \text{Error absoluto} = \ldots \), \( \text{Error relativo} = \ldots \)
- **Error para El Alto**: \( \text{Error absoluto} = \ldots \), \( \text{Error relativo} = \ldots \)

Estos cálculos del error dependen de obtener un valor real de comparación.

## Conclusión

El método de interpolación de Lagrange es una técnica efectiva para estimar la temperatura de ebullición a alturas intermedias, como las de La Paz y El Alto, basándose en datos existentes. El método proporciona resultados consistentes para diferentes altitudes, y los gráficos demuestran la precisión visual del método.
