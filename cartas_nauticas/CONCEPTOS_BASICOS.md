# Conceptos Básicos de Cartografía Náutica

Para poder situarnos en una carta y trazar rumbos, primero debemos dominar algunos conceptos espaciales fundamentales.

## 1. Coordenadas Geográficas

La posición de cualquier punto en la Tierra se define por dos coordenadas:
*   **Latitud (l):** Es la distancia angular desde el Ecuador hasta el paralelo de un lugar. Se mide de 0º a 90º hacia el Norte (N) o hacia el Sur (S). En la carta náutica, la latitud se lee en los márgenes **derecho e izquierdo**.
*   **Longitud (L):** Es la distancia angular desde el Meridiano Cero (Meridiano de Greenwich) hasta el meridiano de un lugar. Se mide de 0º a 180º hacia el Este (E) o hacia el Oeste (W). En la carta náutica, la longitud se lee en los márgenes **superior e inferior**.

La posición se expresa siempre indicando primero la latitud y después la longitud. Ejemplo: `l = 36º 05' N`, `L = 005º 20' W`.

## 2. La Milla Náutica

En el mar no utilizamos kilómetros, utilizamos la **milla náutica (M o nm)**.
*   Una milla náutica equivale a la longitud de un minuto de arco de meridiano terrestre (un minuto de latitud).
*   **1 Milla Náutica = 1.852 metros.**
*   *Nota Práctica:* Las distancias en la carta siempre se miden en las escalas de latitudes (márgenes laterales) a la misma altura en la que nos encontramos navegando, ya que un minuto de latitud siempre equivale a una milla náutica, independientemente del lugar de la Tierra. No se debe medir en las escalas de longitudes (arriba/abajo).

El **nudo** es la unidad de velocidad: 1 nudo = 1 milla náutica por hora.

## 3. Norte Verdadero, Norte Magnético y Aguja

La brújula del barco (el compás magnético o "aguja") no apunta exactamente al Polo Norte geográfico (Norte Verdadero), sino al Norte Magnético Terrestre, que se desplaza con el tiempo. Además, los hierros y campos magnéticos del propio barco desvían la aguja. 

Para poder llevar un rumbo medido en la carta a la realidad, o viceversa, tenemos que corregir estos dos factores:

*   **Norte Verdadero (Nv):** El Polo Norte geográfico, el norte de la carta.
*   **Declinación Magnética (dm):** Es el ángulo que forma el Norte Magnético (Nm) con el Norte Verdadero. Su valor viene impreso en la rosa de los vientos de la carta náutica, indicando el valor de un año base y su variación anual. Debemos calcularla para el año actual.
*   **Desvío de Aguja (Δ):** Es el ángulo que forma la aguja del barco con respecto al Norte Magnético debido a las interferencias magnéticas del propio barco. Cada barco tiene su propia tabla de desvíos en función del rumbo al que navegue.
*   **Corrección Total (Ct):** Es la suma algebraica de la declinación magnética y el desvío. `Ct = dm + Δ`

Fórmula fundamental para convertir rumbos: **Rumbo Verdadero = Rumbo de Aguja + Corrección Total** (`Rv = Ra + Ct`)
