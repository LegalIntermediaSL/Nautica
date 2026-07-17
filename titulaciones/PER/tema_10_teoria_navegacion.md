# PER - Tema 10: Teoría de Navegación Cartográfica y Geodesia Matemática

Este tema es el cimiento absoluto. Asienta las bases matemáticas, geodésicas y magnéticas sin las cuales es físicamente imposible resolver posteriormente un solo ejercicio de trazado sobre la carta de navegación. Todo buen patrón debe entender con rigor científico el mundo sobre el que navega, un mundo que no es plano, sino un elipsoide complejo.

---

## 1. Geometría de la Esfera Terrestre y Geodesia de Precisión

Aunque nuestro planeta está ligeramente achatado por los polos debido a la fuerza centrífuga de su rotación, a efectos de navegación clásica básica y cartas Mercator, lo consideramos una esfera perfecta. Sin embargo, la navegación moderna requiere comprender los **Datums Geodésicos**, como el WGS84 (World Geodetic System 1984), que modela la Tierra como un elipsoide de revolución matemático:
*   **Semieje Mayor (Ecuatorial, $a$):** $6.378.137,0$ metros.
*   **Semieje Menor (Polar, $b$):** $6.356.752,3142$ metros.
*   **Achatamiento ($f$):** $f = \frac{a - b}{a} \approx \frac{1}{298,257223563}$.

### 1.1 Elementos de Referencia Clásica
*   **Eje Terrestre:** Es la varilla imaginaria que atraviesa el planeta y sobre la cual la Tierra da una vuelta completa (aproximadamente 23 horas, 56 minutos y 4 segundos, un día sideral). Los puntos de intersección del eje con la corteza son el Polo Norte (Pn) y Polo Sur (Ps).
*   **Ecuador:** El círculo máximo perpendicular al Eje Terrestre, fruto del corte de un plano que pasa por el centro del elipsoide terrestre. Divide el planeta en Hemisferios Norte y Sur. En el Ecuador, la aceleración centrípeta reduce ligeramente la gravedad neta ($g \approx 9,78 \text{ m/s}^2$).
*   **Paralelos:** Son círculos menores paralelos al Ecuador. Su circunferencia decrece al acercarnos a los polos según la relación $C = 2\pi R \cos(l)$.
*   **Meridianos:** Son grandes semicírculos elípticos de meridiano a meridiano, pasando por ambos Polos. El meridiano primario (Longitud $0^\circ$) es el Meridiano de Greenwich (Londres).

## 2. Coordenadas Geográficas (El DNI Vectorial de una posición)

Para clavar un punto exacto en la inmensidad del océano, usamos un sistema de coordenadas esféricas medido en Grados ($^\circ$), Minutos (') y décimas de minuto.
*(Nota: Un grado tiene 60 minutos. $1^\circ = 60'$)*.

*   **Latitud ($l$ o $\phi$):** El ángulo formado por la vertical del observador con el plano ecuatorial. Se mide a lo largo del meridiano local, desde el Ecuador hasta el paralelo del barco.
    *   Se mide de **$0^\circ$ a $90^\circ$** indicando **Norte (N) o Sur (S)**.
    *   *Propiedad mágica:* La longitud del arco de 1 minuto de latitud varía levísimamente por el achatamiento polar, pero se asume universalmente que **1 minuto de Latitud = 1 Milla Náutica (1852 metros)**. En rigor geodésico, $1 \text{ mn} = \frac{\pi}{10800} R_m$, donde $R_m$ es el radio medio.
*   **Longitud ($L$ o $\lambda$):** El ángulo diédrico formado por el plano del Meridiano de Greenwich y el plano del meridiano del lugar.
    *   Se mide de **$0^\circ$ a $180^\circ$** indicando **Este (E) u Oeste (W - West)**.
    *   El Apartamiento ($A$, distancia física en millas entre dos meridianos a una latitud $l$) decae rápidamente con el coseno: $A = \Delta L \cdot \cos(l)$.

## 3. Direcciones, Rumbos y Dinámica del Magnetismo Terrestre

La **Rosa de los Vientos** está dividida en 360 grados, contando desde el Norte ($000^\circ$) en sentido levógiro (horario).
El **Rumbo ($R$)** es el ángulo físico que forma la crujía del buque respecto a una dirección de referencia. La complejidad surge del Geomagnetismo.

### 3.1 El Campo Magnético y los Tres Nortes
La geodinamo terrestre, impulsada por las corrientes convectivas de aleaciones de hierro y níquel en el núcleo externo líquido (Efecto Dinamo), genera una magnetosfera que oscila. Esto crea tres vectores de Norte distintos:
1.  **Norte Verdadero ($N_v$):** La dirección estática hacia el eje de rotación (Polo Norte geográfico). Es el eje-$Y$ positivo sobre la cuadrícula cilíndrica de una carta.
2.  **Norte Magnético ($N_m$):** Hacia donde confluyen las líneas de flujo del campo geomagnético. Actualmente en movimiento migratorio de Canadá hacia Siberia a una tasa de ~50 km/año.
3.  **Norte de Aguja ($N_a$):** El vector resultante de sumar vectorialmente el campo magnético terrestre y el campo ferromagnético parásito generado por el propio buque (motores, quilla, alternadores).

## 4. Cálculo Vectorial de Errores: Declinación, Desvío y Corrección Total

Para transformar el dato físico de la brújula en un rumbo loxodrómico traza-ble, se aplica álgebra simple de ángulos.

### Error 1: Declinación Magnética ($dm$ o $D$)
Ángulo entre $N_v$ y $N_m$. Este dato depende de las coordenadas $(l, L)$ y del tiempo ($t$). En las cartas, viene tabulado con un incremento secular. 
$$ dm_t = dm_0 + \Delta t \cdot (\text{variación anual}) $$
*   *Convención de Signos:* Este ($+$), Oeste ($-$).

### Error 2: Desvío de Aguja ($\Delta$)
Ángulo entre $N_m$ y $N_a$. Surge de la interferencia constructiva/destructiva de los hierros "dulces" (magnetismo inducido, dependiente del rumbo) e "imanes duros" (magnetismo permanente del buque) modulados por ecuaciones de Poisson complejas. Se tabula en la "Tablilla de Desvíos".
*   *Convención de Signos:* Este ($+$), Oeste ($-$).

### La Corrección Total ($C_t$)
Es la sumatoria algebraica de las dos perturbaciones:
$$ C_t = dm + \Delta $$

### Ecuaciones Fundamentales del Triángulo de Rumbos
Para plasmar la lectura de la aguja en el mundo real (carta):
$$ R_v = R_a + C_t $$
*(Rumbo Verdadero = Rumbo de Aguja + Corrección Total)*

Para indicarle al timonel qué lectura mantener basándonos en un trazado cartográfico ideal:
$$ R_a = R_v - C_t $$
*(Rumbo de Aguja = Rumbo Verdadero - Corrección Total)*

Para las marcaciones y demoras (observaciones de puntos conspicuos de la costa con la pínula):
$$ D_v = D_a + C_t $$
De manera análoga, la demora verdadera ($D_v$) corrige el sesgo magnético local de nuestra observación.
