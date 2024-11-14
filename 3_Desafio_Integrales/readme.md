# Informe de Comparación de Resultados: Cálculo en Excel vs. Programa en Python

Este informe documenta el cálculo del trabajo realizado al estirar una banda elástica usando los métodos numéricos del trapecio y de Simpson, comparando los resultados obtenidos mediante Excel con los resultados generados por un programa en Python. Los datos de desplazamiento y fuerza fueron obtenidos de la siguiente tabla:

| x (in.) | 0   | 0.4 | 0.8 | 1.2 | 1.6 | 2.0 | 2.4 | 2.8 |
|---------|-----|-----|-----|-----|-----|-----|-----|-----|
| F (lb)  | 0   | 0.85| 1.30| 1.60| 1.87| 2.14| 2.34| 2.52|

## Cálculo del Trabajo en Excel
Se realizó el cálculo del trabajo en Excel utilizando las siguientes técnicas:

### 1. Método del Trapecio (Excel)
El método del trapecio se implementó en Excel sumando las áreas de los trapezoides formados por cada subintervalo:
- Cálculo de área de cada subintervalo utilizando la fórmula:
  \[ A = \frac{(F_i + F_{i+1})}{2} \times (x_{i+1} - x_i) \]
- Suma de todas las áreas para obtener el trabajo total.

**Resultado del cálculo en Excel del trapecio**: **4.544 lb-in**

### 2. Método de Simpson (Excel)
El método de Simpson se realizó en Excel utilizando la regla 1/3 y asegurándose de que el número de subintervalos fuera par:
- Aplicación de la fórmula:
  \[ A = \frac{h}{3} [F_0 + 4(F_1 + F_3 + …) + 2(F_2 + F_4 + …) + F_n] \]
- Cálculo de las sumas de los términos impares y pares.

**Resultado del cálculo en Excel de Simpson**: **3.605 lb-in**

## Resultados del Programa en Python
El programa en Python fue desarrollado para calcular el trabajo realizado mediante ambos métodos numéricos de forma automática. Los resultados obtenidos fueron:

### 1. Método del Trapecio (Programa)
- **Resultado del programa**: **4.544 lb-in**

### 2. Método de Simpson (Programa)
- **Resultado del programa**: **3.605 lb-in**

## Comparación de Resultados
Al comparar los resultados obtenidos mediante Excel con los obtenidos por el programa en Python, se observa lo siguiente:
- **Método del Trapecio**:
  - Resultado en Excel: **4.544 lb-in**
  - Resultado del programa: **4.544 lb-in**
  - **Conclusión**: Los resultados coinciden, lo que valida la precisión del programa para este método.

- **Método de Simpson**:
  - Resultado en Excel: **3.605 lb-in**
  - Resultado del programa: **3.605 lb-in**
  - **Conclusión**: Los resultados coinciden también en este caso, confirmando la exactitud del programa.

## Conclusión General
El ejercicio de cálculo del trabajo realizado al estirar una banda elástica utilizando los métodos del trapecio y de Simpson ha demostrado ser una aplicación eficiente de las técnicas numéricas. La comparación de los resultados obtenidos en Excel y en el programa en Python confirma la consistencia y precisión de ambos enfoques. 

