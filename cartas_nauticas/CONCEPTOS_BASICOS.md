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

## 4. La Proyección Mercator: Por Qué Navegamos Sobre Ella

Toda carta náutica de navegación está construida sobre la **Proyección de Mercator** (1569), una proyección cilíndrica que traslada la esfera terrestre a un plano. No se eligió al azar: se eligió porque es **conforme**, es decir, conserva los ángulos localmente.

*   **Ventaja principal (por qué se usa):** al conservar los ángulos, un rumbo constante (mantener siempre el mismo ángulo con los meridianos) se dibuja en la carta como una **línea recta**. Esto es enormemente práctico: el navegante traza una recta entre dos puntos, mide su ángulo con el transportador y ya tiene el rumbo de aguja a gobernar, sin necesidad de ir corrigiendo el rumbo constantemente como ocurriría con otras proyecciones.
*   **El precio a pagar (la distorsión):** para lograr esa conformidad, Mercator tiene que separar progresivamente los paralelos a medida que nos alejamos del Ecuador. El resultado es que **las áreas se distorsionan muchísimo en latitudes altas**. Groenlandia, en una carta Mercator, parece casi del tamaño de África, cuando en realidad es catorce veces más pequeña. Por eso la escala de una carta Mercator no es constante: **crece con la latitud**.
*   **Consecuencia práctica para medir:** como la escala varía según la latitud, nunca se mide una distancia con el compás de puntas en cualquier parte de la carta. Siempre se mide en la escala de latitudes (margen lateral) **a la altura del tramo que se está midiendo** (ver punto 2).
*   **Límite de uso:** por esta misma distorsión, la proyección Mercator deja de ser útil cerca de los polos (más allá de unos 80º de latitud), zona donde se usan otras proyecciones (como la Polar Estereográfica) que no se emplean en la náutica comercial o de recreo habitual.

## 5. Milla Náutica vs. Milla Terrestre

Conviene no confundir la milla náutica con la **milla terrestre o milla estatutaria** (statute mile), de origen romano y muy usada en tierra en países anglosajones (por ejemplo, en las señales de carretera de EE.UU. o Reino Unido).

| Unidad | Equivalencia en metros | Origen / Uso |
| :--- | :--- | :--- |
| **Milla Náutica (M)** | 1.852 m | Un minuto de arco de meridiano terrestre. Uso marítimo y aéreo. |
| **Milla Terrestre (mi)** | 1.609,344 m | Medida romana/anglosajona. Uso terrestre (carreteras, EE.UU./UK). |

**Fórmulas de conversión:**
*   De millas náuticas a millas terrestres: `mi = M × 1,1508`
*   De millas terrestres a millas náuticas: `M = mi × 0,8690`

*Nota práctica:* Esta confusión es habitual al usar cartografía o GPS de origen estadounidense configurados por defecto en "statute miles" en lugar de "nautical miles". Siempre hay que comprobar la unidad activa del instrumento antes de fiarse de una distancia.

## 6. Escalas de la Carta: General, de Aproximación y Portulano

No todas las cartas náuticas tienen el mismo nivel de detalle. La escala (relación entre una distancia en la carta y la distancia real, ej. 1:150.000) determina para qué sirve cada carta.

| Tipo de Carta | Escala aproximada | Uso |
| :--- | :--- | :--- |
| **Carta General (de Punto Mayor)** | 1:1.000.000 o menor (ej. 1:3.500.000) | Planificación de travesías largas y navegación oceánica. Poco detalle costero. |
| **Carta de Navegación Costera / de Aproximación** | 1:150.000 a 1:300.000 aprox. | Aproximarse a la costa desde mar abierto, reconocer golfos, bahías y accidentes costeros generales. |
| **Carta Portulano / Plano de Puerto** | 1:5.000 a 1:50.000 aprox. | Máximo detalle: entrada a puertos, canales estrechos, maniobra y fondeo. Imprescindible cerca de la costa y bajos. |

**Regla práctica:** se debe navegar siempre con la carta de **mayor escala disponible** para la zona en la que realmente se está (es decir, la más detallada, el portulano si existe), reservando la carta general únicamente para trazar la derrota global entre puntos alejados. Confiar en una carta general para maniobrar cerca de la costa es una causa común de varada, ya que muchos peligros pequeños (bajos, rocas aisladas) no caben representados a esa escala.
