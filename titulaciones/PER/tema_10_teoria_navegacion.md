# Tema 10: Teoría de Navegación

Este tema asienta las bases matemáticas y cartográficas necesarias para poder resolver posteriormente los ejercicios sobre la carta de navegación. 

## 1. La Esfera Terrestre

La Tierra no es una esfera perfecta (está achatada por los polos), pero a efectos de navegación básica la consideramos esférica.

*   **Eje Terrestre:** Línea imaginaria alrededor de la cual rota la Tierra. Sus extremos son el Polo Norte (Pn) y el Polo Sur (Ps).
*   **Ecuador:** Círculo máximo perpendicular al eje terrestre. Divide la Tierra en Hemisferio Norte y Hemisferio Sur.
*   **Paralelos:** Círculos menores paralelos al Ecuador.
*   **Meridianos:** Círculos máximos que pasan por los Polos. Todos los meridianos convergen en los polos. El meridiano de referencia (0º) es el Meridiano de Greenwich.

## 2. Coordenadas Geográficas

Para situar un punto exacto en el mar, utilizamos dos coordenadas:

*   **Latitud (l):** Es el arco de meridiano contado desde el Ecuador hasta el paralelo del lugar. Se mide de 0º a 90º hacia el Norte (N) o hacia el Sur (S). *1 minuto de latitud equivale a 1 milla náutica.*
*   **Longitud (L):** Es el arco de Ecuador contado desde el meridiano de Greenwich hasta el meridiano del lugar. Se mide de 0º a 180º hacia el Este (E) o hacia el Oeste (W).

## 3. Direcciones y Rumbos

La Rosa de los Vientos está dividida en 360 grados, comenzando en el Norte (000º) y contando en el sentido de las agujas del reloj.

*   **Rumbo (R):** Es el ángulo que forma la línea de crujía (proa) de nuestro barco con un Norte de referencia.
*   **Norte Verdadero (Nv):** El norte geográfico, el Polo Norte. Es el que aparece en las cartas náuticas.
*   **Norte Magnético (Nm):** Hacia donde apunta realmente la aguja imantada del compás debido al campo magnético terrestre (que varía según el lugar y el año).
*   **Norte de Aguja (Na):** Hacia donde apunta el compás a bordo de NUESTRO barco, afectado tanto por el campo magnético de la Tierra como por el magnetismo propio del barco (hierros, electrónica).

## 4. Declinación Magnética y Desvío

La diferencia entre estos "nortes" genera errores que debemos corregir para que la lectura de nuestra brújula coincida con el mapa:

### Declinación Magnética (dm)
Es el ángulo entre el Norte Verdadero y el Norte Magnético. 
Viene indicada en las cartas náuticas (ej. rosa de los vientos de la carta). **Varía con el lugar geográfico y con el tiempo** (se indica la variación anual). 
*Regla de signos:* Hacia el Este (E) es Positiva (+). Hacia el Oeste (W) es Negativa (-).

### Desvío de Aguja (Δ)
Es el ángulo entre el Norte Magnético y el Norte de Aguja. 
Es el error propio de nuestro barco (por sus hierros). **Varía según el rumbo al que navegue el barco**. Se consulta en la "Tablilla de Desvíos" del barco.
*Regla de signos:* Hacia el Este (E) es Positivo (+). Hacia el Oeste (W) es Negativo (-).

### Corrección Total (Ct)
Es la suma algebraica de ambos errores:
**Ct = dm + Δ**

### Ecuación Fundamental del Rumbo
**Rumbo Verdadero = Rumbo de Aguja + Corrección Total**
*(Rv = Ra + Ct)*

> [!TIP]
> Si te lías con los cálculos de la Corrección Total, te animamos a abrir la herramienta de simulación interactiva en nuestro repositorio `simulaciones/01_calculo_rumbo_verdadero.py` para visualizarlo paso a paso.
