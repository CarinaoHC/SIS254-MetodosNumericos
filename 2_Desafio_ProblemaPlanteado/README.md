# Predicción del Nivel del Mar usando Interpolación de Lagrange

## Introducción

El cambio climático es uno de los mayores retos de nuestra época, y el aumento del nivel del mar es una de sus manifestaciones más visibles y preocupantes. Las comunidades costeras de todo el mundo están enfrentando la amenaza de inundaciones, erosión y la pérdida de hábitats naturales debido a este fenómeno. Estimar con precisión el incremento del nivel del mar en el futuro es esencial para tomar decisiones informadas en la planificación urbana y en la adaptación a estos cambios climáticos.

### ¿Por qué este problema?

El objetivo de este estudio es predecir el nivel del mar en el futuro utilizando la **Interpolación Polinómica de Lagrange**, que es un método matemático clásico para la estimación de valores desconocidos en base a un conjunto de puntos conocidos. Aunque la interpolación de Lagrange puede ser útil dentro del rango de datos conocidos, su uso para extrapolación (predicción fuera del rango de datos) puede ser problemático. Esta investigación busca ilustrar las ventajas y desventajas de este método, mostrando su comportamiento cuando se intenta extrapolar a largo plazo.

## Fuentes de Datos Reales

Los datos sobre el aumento del nivel del mar pueden obtenerse de múltiples fuentes confiables, incluyendo:

1. **NOAA (National Oceanic and Atmospheric Administration)**: Proporciona datos sobre el aumento del nivel del mar basados en observaciones de mareógrafos y satélites. Es una de las principales fuentes de información científica sobre este tema. [Sitio web de NOAA](https://tidesandcurrents.noaa.gov/sltrends/).

2. **NASA (National Aeronautics and Space Administration)**: A través de sus programas de observación satelital, la NASA monitorea el nivel del mar globalmente y tiene proyecciones basadas en sus estudios climáticos. [Sitio web de NASA sobre el nivel del mar](https://climate.nasa.gov/vital-signs/sea-level/).

3. **IPCC (Intergovernmental Panel on Climate Change)**: El IPCC publica informes periódicos con modelos y proyecciones sobre el aumento del nivel del mar bajo diferentes escenarios de emisiones de gases de efecto invernadero. [IPCC Reports](https://www.ipcc.ch/reports/).

### Datos Utilizados

Para este ejercicio, se han utilizado datos hipotéticos que reflejan una tendencia de aumento del nivel del mar similar a los observados por estas fuentes entre **1950** y **2020**. Estos datos están basados en observaciones históricas que muestran un aumento progresivo del nivel del mar, con una tendencia acelerada en las últimas décadas.

| Año  | Nivel del Mar (cm) |
|------|--------------------|
| 1950 | 0.0                |
| 1960 | 1.2                |
| 1970 | 2.4                |
| 1980 | 4.0                |
| 1990 | 6.5                |
| 2000 | 9.8                |
| 2010 | 13.4               |
| 2020 | 18.0               |

## Objetivos

1. Utilizar la **Interpolación de Lagrange** para predecir el nivel del mar en los años **2050**, **2075** y **2100**.
2. Demostrar los límites y problemas de la extrapolación utilizando un polinomio de alto grado.
3. Comparar los resultados con proyecciones científicas basadas en modelos más avanzados.
4. Evaluar la precisión de la interpolación de Lagrange en problemas reales de predicción a largo plazo.

## Procedimiento Completo: Interpolación de Lagrange

### Paso 1: Definir los Puntos Conocidos

Los datos históricos del nivel del mar son:

| Año  | Nivel del Mar (cm) |
|------|--------------------|
| 1950 | 0.0                |
| 1960 | 1.2                |
| 1970 | 2.4                |
| 1980 | 4.0                |
| 1990 | 6.5                |
| 2000 | 9.8                |
| 2010 | 13.4               |
| 2020 | 18.0               |

### Paso 2: Construcción del Polinomio de Lagrange

#### 2.1: Fórmula de Interpolación

La fórmula de la interpolación de Lagrange es:

$P(x) = \sum_{i=0}^{n} y_i \cdot L_i(x)$

donde:

$L_i(x) = \prod_{\substack{0 \leq j < n \\ j \neq i}} \frac{x - x_j}{x_i - x_j}$

Aquí, \( n = 8 \) (8 puntos de datos).

#### 2.2: Cálculo de los Términos \( L_i(x) \)

Vamos a calcular \( L_i(x) \) para cada \( i \) de 0 a 7.

1. **Para \( i = 0 \)** (1950):

$L_0(x) = \frac{(x - 1960)(x - 1970)(x - 1980)(x - 1990)(x - 2000)(x - 2010)(x - 2020)}{(1950 - 1960)(1950 - 1970)(1950 - 1980)(1950 - 1990)(1950 - 2000)(1950 - 2010)(1950 - 2020)}$

Calculando el denominador:

$(1950 - 1960)(1950 - 1970)(1950 - 1980)(1950 - 1990)(1950 - 2000)(1950 - 2010)(1950 - 2020) = (-10)(-20)(-30)(-40)(-50)(-60)(-70) = -50400000$

Por lo tanto:

$L_0(x) = \frac{(x - 1960)(x - 1970)(x - 1980)(x - 1990)(x - 2000)(x - 2010)(x - 2020)}{-50400000}$

2. **Para \( i = 1 \)** (1960):

$L_1(x) = \frac{(x - 1950)(x - 1970)(x - 1980)(x - 1990)(x - 2000)(x - 2010)(x - 2020)}{(1960 - 1950)(1960 - 1970)(1960 - 1980)(1960 - 1990)(1960 - 2000)(1960 - 2010)(1960 - 2020)}$

El denominador se calcula como:

$(1960 - 1950)(1960 - 1970)(1960 - 1980)(1960 - 1990)(1960 - 2000)(1960 - 2010)(1960 - 2020) = (10)(-10)(-20)(-30)(-40)(-50)(-60) = 36000000$

Por lo tanto:

$L_1(x) = \frac{(x - 1950)(x - 1970)(x - 1980)(x - 1990)(x - 2000)(x - 2010)(x - 2020)}{36000000}$

3. Repetimos este procedimiento para \( i = 2, 3, 4, 5, 6, 7 \) obteniendo sus respectivas expresiones.

#### 2.3: Construcción del Polinomio Interpolante

El polinomio \( P(x) \) se construye sumando todos los términos:

$P(x) = \sum_{i=0}^{7} y_i \cdot L_i(x)$

Sustituyendo los valores:

$P(x) = 0.0 \cdot L_0(x) + 1.2 \cdot L_1(x) + 2.4 \cdot L_2(x) + 4.0 \cdot L_3(x) + 6.5 \cdot L_4(x) + 9.8 \cdot L_5(x) + 13.4 \cdot L_6(x) + 18.0 \cdot L_7(x)$

### Paso 3: Cálculo de las Predicciones

Ahora evaluamos \( P(x) \) para los años 2050, 2075 y 2100.

1. **Predicción para 2050**:

$P(2050) = \sum_{i=0}^{7} y_i \cdot L_i(2050)$

Sustituyendo cada \( L_i(2050) \) en la ecuación anterior, obtenemos:

- Calcular \( L_i(2050) \) para cada \( i \).

2. **Predicción para 2075**:

$P(2075) = \sum_{i=0}^{7} y_i \cdot L_i(2075)$

3. **Predicción para 2100**:

$P(2100) = \sum_{i=0}^{7} y_i \cdot L_i(2100)$

### Resultados

Después de realizar los cálculos para cada uno de los años:

- **2050**: \( P(2050) \approx 153.6 \, \text{cm} \)
- **2075**: \( P(2075) \approx 1196.5 \, \text{cm} \)
- **2100**: \( P(2100) \approx 5956.4 \, \text{cm} \)

### Paso 4: Análisis de Errores

Para evaluar el error, comparamos las predicciones de Lagrange con proyecciones de fuentes confiables:

- **2050**: Predicción de 153.6 cm frente a proyecciones del IPCC de 30 a 90 cm.
- **2075** y **2100**: Las predicciones son notablemente más altas y poco realistas, mostrando la incapacidad del método para extrapolar correctamente.

### Conclusiones

1. **Limitaciones del Método**: La interpolación de Lagrange es adecuada para la interpolación de datos dentro del rango conocido, pero sus resultados son ineficaces para la extrapolación, lo que resulta en predicciones exageradas.

2. **Predicciones Irreales**: Las predicciones para 2075 y 2100 son significativamente mayores que las estimaciones científicas, lo que destaca la inadecuación de este método para problemas complejos como el aumento del nivel del mar.

3. **Recomendaciones**: Para futuras proyecciones, se deben utilizar modelos climáticos más sofisticados que integren diversos factores y variables.

### Recomendaciones para Futuros Trabajos

1. **Usar Splines Cúbicos**: Mejorar la precisión mediante el uso de splines cúbicos para evitar oscilaciones.

2. **Datos Actualizados**: Incorporar datos de fuentes como NOAA, NASA, e IPCC para hacer comparaciones válidas.

3. **Análisis Comparativo**: Realizar un análisis comparativo de diferentes métodos de interpolación y modelos avanzados para determinar cuál es más efectivo en diferentes contextos.

## Código para la Resolución del Problema

A continuación se presenta un ejemplo de código en Python para calcular el polinomio de Lagrange y graficar los resultados:

```python
import numpy as np
import matplotlib.pyplot as plt

# Datos históricos del nivel del mar
years = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
sea_levels = np.array([0.0, 1.2, 2.4, 4.0, 6.5, 9.8, 13.4, 18.0])

# Función de interpolación de Lagrange
def lagrange_interpolation(x, years, sea_levels):
    result = 0.0
    n = len(years)
    for i in range(n):
        term = sea_levels[i]
        for j in range(n):
            if j != i:
                term *= (x - years[j]) / (years[i] - years[j])
        result += term
    return result

# Valores para los cuales queremos predecir el nivel del mar
future_years = np.array([2050, 2075, 2100])
predicted_levels = [lagrange_interpolation(year, years, sea_levels) for year in future_years]

# Imprimir predicciones
for year, level in zip(future_years, predicted_levels):
    print(f'Predicción para {year}: {level:.2f} cm')

# Graficar resultados
x_values = np.linspace(1940, 2100, 300)
y_values = [lagrange_interpolation(x, years, sea_levels) for x in x_values]

plt.figure(figsize=(10, 6))
plt.plot(years, sea_levels, 'ro', label='Datos históricos')
plt.plot(x_values, y_values, 'b-', label='Interpolación de Lagrange')
plt.scatter(future_years, predicted_levels, color='green', label='Predicciones')
plt.xlabel('Año')
plt.ylabel('Nivel del Mar (cm)')
plt.title('Predicción del Nivel del Mar usando Interpolación de Lagrange')
plt.axhline(y=0, color='k', linestyle='--')
plt.legend()
plt.grid()
plt.show()
