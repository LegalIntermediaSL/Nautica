# PER - Tema 11: La Carta Náutica, Proyección Mercator y Resolución Analítica

El Tema 11 es la "prueba de fuego" y el terror del PER. Es una parte 100% práctica de cartografía analítica y gráfica que se realiza obligatoriamente sobre la Carta del **Estrecho de Gibraltar (Carta 105)**. Dominar este tema significa entender las transformaciones matemáticas necesarias para proyectar el elipsoide de la Tierra en un plano euclidiano, resolviendo interceptaciones y trayectorias.

Si fallas más de 2 problemas de los 4 de este bloque, suspendes todo el examen del PER automáticamente, evidenciando que no eres apto para guiar vidas en alta mar.

---

## 1. La Matemática de la Proyección Mercator

La carta náutica no es un mapa pictórico, es una proyección cartográfica cilíndrica ecuatorial inventada por **Gerardus Mercator** en 1569. Su inmenso valor operativo radica en su propiedad isogonal: **es una proyección conforme** (conserva los ángulos locales). 

Matemáticamente, la latitud mercatoriana (partes meridionales, $PM$) sufre una expansión que sigue la integral de la secante de la latitud:
$$ PM = \int_{0}^{l} \sec(\phi) \, d\phi = \ln\left( \tan\left( \frac{\pi}{4} + \frac{l}{2} \right) \right) $$
Esta alteración exponencial del eje $Y$ provoca que las distancias a medida que nos alejamos del Ecuador (altas latitudes) se dilaten drásticamente en el papel (Groenlandia parece gigantesca). En consecuencia, **la escala de la carta Mercator es una variable dependiente de la latitud**, $E(l) = E_0 \sec(l)$. 

La línea recta que se traza sobre una carta Mercator corta a todos los meridianos con el mismo ángulo. Esta curva espacial sobre la Tierra se llama **Loxodrómica**.

### 1.1 Coordenadas y el Uso Exclusivo del Compás

Cualquier hito en la carta se ancla geométricamente en dos ejes perpendiculares:
*   **Latitud ($l$):** Nos indica la distancia angular al Ecuador. Debido a la dilatación logarítmica de la proyección, **se mide única y exclusivamente en las escalas métricas verticales** a la misma altura del paralelo de trabajo. 
*   **Longitud ($L$):** El desplazamiento angular horizontal desde el meridiano base (Greenwich). Las subdivisiones de longitud son constantes en la carta, localizadas en los márgenes superior/inferior. (ej. $005^\circ 42,6' W$).

> [!CAUTION]
> **El Peligro Euclidiano de Medir Distancias:**
> Dado que el diferencial de latitud deformado es $dl' = dl \sec(l)$, las distancias (Millas Náuticas) se miden con el compás de puntas secas **ÚNICAMENTE en las escalas de Latitud laterales**, tomando el tramo que coincida con el rango de latitud del segmento a medir. 
> *Equivalencia de conversión métrica: 1 Minuto de Latitud = 1 Milla Náutica = 1.852 Metros.*

## 2. Álgebra Vectorial de los Nortes y el Rumbo

En la carta náutica, toda la cartografía está referenciada matemáticamente al **Norte Verdadero ($N_v$)**. Sin embargo, la plataforma dinámica del buque navega basándose en un compás que percibe un entorno ferromagnético distorsionado (**Norte de Aguja, $N_a$**).

La Ecuación Maestra de Transferencia Angular del PER es:
$$ R_v = R_a + C_t $$

### 2.1 Desglose Geofísico de la Corrección Total ($C_t$)
Es la suma de la declinación magnética local ($dm$) y la anomalía del propio barco ($\Delta$):
$$ C_t = dm + \Delta $$

*   **Declinación Magnética ($dm$):** Dato del campo geomagnético. En un examen, requiere extrapolar la variación secular lineal desde la fecha base de la carta (ej. 2005) hasta el año actual usando sumas/restas de minutos ($'$), teniendo un cuidado extremo con cruzar el cero a la hora de restar minutos occidentales y orientales.
*   **Desvío ($\Delta$):** El tensor magnético del buque. Tabulado directamente.
*   **Demoras (Observaciones visuales):** Las alidadas o pínulas leen demoras influenciadas por el mismo $C_t$ de la aguja: $D_v = D_a + C_t$.

## 3. Tipología Analítica de Problemas (Resolución Geométrica)

El examen evaluará 4 problemas estructurados en torno a las siguientes construcciones de geometría plana:

### Escenario A: Cálculo de Trayectoria Cinemática y ETA
*Problema de Cinemática 2D en movimiento rectilíneo uniforme.*
1. Se unen dos puntos geográficos, creando el vector desplazamiento $\vec{d}$.
2. Trasladando el vector al origen de la Rosa, su ángulo respecto al eje $Y$ puro determina el **Rumbo Verdadero ($R_v$)**.
3. La magnitud del vector $|\vec{d}|$ medida en la escala lateral de latitud nos entrega la Distancia ($D$) en millas.
4. Aplicando álgebra: $R_a = R_v - C_t$ para obtener el rumbo del timonel.
5. Aplicando cálculo diferencial elemental integrado: $\Delta t = \frac{|\vec{d}|}{v}$. La Hora Estimada de Llegada se obtiene mediante sumas sexagesimales de tiempo ($t_{\text{llegada}} = t_{\text{salida}} + \Delta t$).

### Escenario B: Intersección de Loci (Cruce de Demoras)
*Resolución de un sistema de dos ecuaciones lineales en el plano.*
1. Dada $D_a$ de dos faros, se halla su $D_v$ respectiva.
2. Una demora observada genera una **Línea de Posición (LDP)**. Para trazarla, se dibuja su recíproco o inverso (la demora desde el faro hacia el barco: $D_v \pm 180^\circ$).
3. La intersección de las dos rectas (LDP 1 y LDP 2) en el plano cartesiano local es la posición matemática del observador, asumiendo error cero.

### Escenario C: Situación Híbrida (Demora y Distancia Radar)
*Intersección de una recta con una circunferencia parabólica.*
1. Se traza la línea infinita de la Demora Verdadera invertida desde el faro costero.
2. El eco de radar ($D$) define un círculo de radio fijo ($R = D$) cuyo centro está en el objetivo (Faro). Ecuación: $(x - x_f)^2 + (y - y_f)^2 = R^2$.
3. Se pincha el compás en el Faro (centro del círculo) con radio $R$ medido en latitudes, trazando el arco hasta cortar la recta de la demora. El punto de corte es la solución del sistema.

### Escenario D: Navegación de Estima (Dead Reckoning)
*Integración vectorial a ciegas basada en velocidad sobre el agua y rumbo verdadero.*
1. A partir de un fijado geográfico conocido ($P_0$), se proyecta un vector en la dirección $R_v$.
2. La magnitud de desplazamiento es $D = v \cdot \Delta t$.
3. Situación final: $P_{1} = P_0 + \vec{D}$. Sobre el papel, esto es extender un arco de longitud $D$ sobre la loxodrómica trazada desde $P_0$. (Físicamente en navegación real se complica por el abatimiento (viento) y la deriva (corriente) sumando más vectores $\vec{v}_{\text{viento}}$ y $\vec{v}_{\text{corriente}}$, aunque en PER básico suele simplificarse).

## 4. Publicaciones Oficiales y Modelos de Datos ECDIS

### 4.1. El Manual INT-1
La nomenclatura cartográfica está estandarizada por la OHI (Organización Hidrográfica Internacional). 
*   `+` rodeada de puntos: Roca siempre sumergida.
*   `*`: Roca que vela en bajamar, peligro catastrófico de choque con calado.
*   Naturaleza del fondo marino en inglés: `S` (Sand), `M` (Mud), `R` (Rock), `Wd` (Weed), afectando al coeficiente de fricción de las anclas.

### 4.2. Sistemas ECDIS (Electronic Chart Display)
El estándar WGS84 se traduce a formato electrónico utilizando dos aproximaciones topológicas:
1.  **Cartas Raster (RNC):** Matrices de píxeles estáticas georreferenciadas (imágenes escaneadas). Sufren de aliasing al hacer zoom matemático.
2.  **Cartas Vectoriales (ENC):** Son bases de datos orientadas a objetos espaciales (puntos, polígonos, líneas) con atributos. Si el ECDIS está acoplado al GPS y al calado paramétrico introducido ($Z$), las líneas isobáticas y rocas calculan umbrales booleanos en tiempo real para disparar alarmas anti-colisión.

## Ejemplos Prácticos

**Problema 1: Cálculo Analítico de la Loxodrómica (Meridian Parts)**
Se desea trazar una derrota desde el punto de salida $P_1(l_1 = 35^\circ 00' \text{N}, L_1 = 006^\circ 00' \text{W})$ hasta el punto de llegada $P_2(l_2 = 36^\circ 00' \text{N}, L_2 = 005^\circ 00' \text{W})$. Asumiendo la Tierra como una esfera perfecta, calcule analíticamente el Rumbo Verdadero ($R_v$) exacto de la loxodrómica utilizando el concepto de Partes Meridionales ($PM$).

**Solución:**
La fórmula para la Partes Meridionales en una esfera es:
$$ PM(l) = \frac{10800}{\pi} \ln\left[ \tan\left( 45^\circ + \frac{l}{2} \right) \right] $$
Calculamos las PM para $l_1 = 35^\circ$ y $l_2 = 36^\circ$:
$$ PM_1 = \frac{10800}{\pi} \ln\left[ \tan\left( 45^\circ + 17.5^\circ \right) \right] \approx 2244.29 \text{ pm} $$
$$ PM_2 = \frac{10800}{\pi} \ln\left[ \tan\left( 45^\circ + 18^\circ \right) \right] \approx 2317.84 \text{ pm} $$
La diferencia de Partes Meridionales ($\Delta PM$) es:
$$ \Delta PM = PM_2 - PM_1 = 2317.84 - 2244.29 = 73.55 \text{ pm} $$
La diferencia de Longitud ($\Delta L$) en minutos es:
$$ \Delta L = L_2 - L_1 = (-5^\circ) - (-6^\circ) = +1^\circ = 60' \text{ (Hacia el Este)} $$
El rumbo loxodrómico ($R_v$) cumple que:
$$ \tan(R_v) = \frac{\Delta L}{\Delta PM} = \frac{60}{73.55} \approx 0.8157 $$
$$ R_v = \arctan(0.8157) \approx 39.2^\circ = 039.2^\circ $$
El rumbo a gobernar en el compás verdadero es $039.2^\circ$.

## Referencias Bibliográficas y Jurisprudencia

*   **Bibliografía Básica:** Moreu Curbera, J.M. (2010). *Astronomía Náutica y Navegación*. Editorial de la Universidad de Cádiz.
*   **Convenios OMI:** Normas IHO S-52 y S-57 relativas al rendimiento y especificaciones de las Cartas Electrónicas de Navegación (ENC).
*   **Jurisprudencia:** *USS Guardian Grounding (2013)* en el Arrecife Tubbataha. Un fallo catastrófico debido a un error geodésico de desplazamiento de 8 millas en las cartas náuticas digitales vectoriales provistas por NGA, demostrando la necesidad imperiosa de cotejar el datum de las cartas rasterizadas/vectoriales y el uso combinado con medios de navegación puramente visuales y de ecosonda.
