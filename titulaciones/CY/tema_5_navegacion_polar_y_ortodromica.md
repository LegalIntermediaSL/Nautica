# Capitán de Yate - Tema 5: Navegación Polar, Ortodrómica y Rutas Oceánicas Complejas

Cuando un buque abandona la navegación costera (loxodrómica) y se enfrenta a cruzar océanos enteros o navegar en altas latitudes (por encima de los 60º Norte o Sur), la esfericidad de la Tierra deja de ser un efecto secundario para convertirse en el factor matemático dominante.

Este tema explora las técnicas avanzadas que utilizan los marinos profesionales y regatistas oceánicos (como los de la *Ocean Race* o *Vendée Globe*) para optimizar sus rutas y sobrevivir en los extremos magnéticos y de hielo del planeta.

---

## 1. Navegación por Círculo Máximo (Ortodrómica)

La **Loxodrómica** (línea recta en una carta Mercator) corta todos los meridianos con el mismo ángulo (rumbo constante), lo cual es muy cómodo para gobernar el timón. Sin embargo, matemáticamente NO es la distancia más corta entre dos puntos en una esfera.

La distancia más corta es el arco de **Círculo Máximo (Ortodrómica)** que une ambos puntos. En una carta Mercator, este camino se dibuja como una curva cóncava hacia el ecuador, obligando al navegante a cambiar el rumbo del compás continuamente.

### 1.1. El Triángulo Esférico de la Ortodrómica
Para calcular la distancia y los rumbos, se resuelve un triángulo esférico en la superficie terrestre cuyos vértices son:
1.  **Polo Elevado ($P$)**: El Polo Norte o Sur geográfico.
2.  **Punto de Salida ($A$)**: De coordenadas ($l_A, L_A$).
3.  **Punto de Llegada ($B$)**: De coordenadas ($l_B, L_B$).

Los lados del triángulo son las colatitudes de A ($90^\circ - l_A$), de B ($90^\circ - l_B$) y la Distancia Ortodrómica ($D$) que queremos calcular.
El ángulo en el polo es la diferencia de longitudes ($\Delta L = L_B - L_A$).

### 1.2. Fórmulas Fundamentales
**1. Cálculo de la Distancia Ortodrómica ($D$):**
Utilizando la fórmula de la cosenusa (similar a la de la altura estimada en astronomía):

$$
\cos(D) = \sin(l_A) \cdot \sin(l_B) + \cos(l_A) \cdot \cos(l_B) \cdot \cos(\Delta L)
$$

El resultado ($D$) es un ángulo. Para pasarlo a millas náuticas, simplemente multiplicamos los grados por 60 y sumamos los minutos.

**2. Cálculo del Rumbo Inicial ($R_i$):**
Utilizando el teorema de las cotangentes o de los senos. Es el rumbo exacto al que debes poner la proa en el momento de zarpar:

$$
\cot(R_i) = \frac{\cos(l_A) \cdot \tan(l_B) - \sin(l_A) \cdot \cos(\Delta L)}{\sin(\Delta L)}
$$

(Se nombra cardinalmente igual que el Azimut: Desde el polo de salida geográfico hacia el Este o el Oeste según el destino).

### 1.3. Resolución Completa del Triángulo: Paralelismo con el Triángulo de Posición Astronómico

El triángulo esférico $P$-$A$-$B$ del apartado 1.1 no es una herramienta exclusiva de la ortodromia: es exactamente el mismo tipo de objeto matemático que el **Triángulo Esférico de Posición** (Polo–Cenit–Astro) que se resuelve en el Tema 3, apartado 4, para hallar la Altura Estimada y el Azimut de un astro. La geometría de la esfera terrestre y la de la esfera celeste se resuelven con las mismas dos herramientas: la **Ley de Cosenos** (fórmula de la cosenusa) y la **Ley de Senos**. Lo único que cambia son los nombres de los vértices.

**Identificación de lados y ángulos del triángulo $P$-$A$-$B$:**
*   Lado $PA$ (opuesto al vértice $B$) $= 90^\circ - l_A$ (colatitud de salida).
*   Lado $PB$ (opuesto al vértice $A$) $= 90^\circ - l_B$ (colatitud de llegada).
*   Lado $AB$ (opuesto al vértice $P$) $= D$ (Distancia Ortodrómica).
*   Ángulo en $P$ $= \Delta L$.
*   Ángulo en $A$ $= R_i$ (Rumbo Inicial, el que buscamos).
*   Ángulo en $B$ $= R_f$ (Rumbo de llegada, el rumbo con el que "se entra" al puerto B).

**Paso 1 — Ley de Cosenos aplicada al lado $AB$:**

$$
\cos(D) = \cos(90^\circ - l_A)\cos(90^\circ - l_B) + \sin(90^\circ - l_A)\sin(90^\circ - l_B)\cos(\Delta L)
$$

Como $\cos(90^\circ - l) = \sin(l)$ y $\sin(90^\circ - l) = \cos(l)$, esta expresión se reduce exactamente a la fórmula del apartado 1.2:

$$
\cos(D) = \sin(l_A)\sin(l_B) + \cos(l_A)\cos(l_B)\cos(\Delta L)
$$

Es idéntica en estructura a $\sin(a_e) = \sin(l_e)\sin(Dec) + \cos(l_e)\cos(Dec)\cos(P)$ del Tema 3: en ambos casos se resuelve el lado desconocido de un triángulo esférico conociendo los otros dos lados y el ángulo comprendido entre ellos.

**Paso 2 — Ley de Senos para obtener $R_i$ de forma directa:**

$$
\frac{\sin(\Delta L)}{\sin(D)} = \frac{\sin(R_i)}{\sin(90^\circ - l_B)} \quad\Rightarrow\quad \sin(R_i) = \frac{\cos(l_B)\cdot\sin(\Delta L)}{\sin(D)}
$$

> [!NOTE]
> La Ley de Senos, por su propia naturaleza, entrega un ángulo ambiguo: $R_i$ y $180^\circ - R_i$ comparten el mismo seno, y ambos son matemáticamente compatibles con los datos. Por eso, para resolver el cuadrante correcto sin ambigüedad, en la práctica se recurre a la fórmula de la cotangente del apartado 1.2 (equivalente a la fórmula de las cuatro partes de Napier). Es exactamente el mismo problema — y la misma solución — que aparece al despejar el Azimut $Z$ en el triángulo de posición astronómico del Tema 3: la Ley de Senos orienta, pero solo la cotangente (o una comprobación de cuadrante con los signos de latitud y $\Delta L$) resuelve el rumbo real de forma unívoca.

### 1.4. El Vértice de la Ortodrómica ($V$)
El Vértice es el punto de la ruta que alcanza la máxima latitud (más cercano al polo). En ese punto exacto, el rumbo de la nave es **exactamente $090^\circ$ (Este) o $270^\circ$ (Oeste)**, y el meridiano corta a la ortodrómica en un ángulo recto.
*   **Latitud del Vértice ($l_v$):** $\cos(l_v) = \cos(l_A) \cdot \sin(R_i)$
*   **Longitud del Vértice ($L_v$):** Se halla calculando la diferencia de longitud entre la salida y el vértice mediante la ecuación: $\sin(\Delta L_{AV}) = \frac{\cos(R_i)}{\sin(l_v)}$.

> [!WARNING]
> **Peligro Náutico del Vértice:** El vértice de la ruta ortodrómica (por ejemplo, navegando de Japón a San Francisco) puede alcanzar latitudes altísimas (Ej: $55^\circ$ Norte), arrojando el barco a zonas de tormentas brutales (Mar de Bering), niebla engelante y hielo. Aquí es donde entra en juego la navegación mixta.

---

## 2. Navegación Práctica en Tramos: de la Curva Continua a los Segmentos Rectos

Un dato fundamental que conviene remarcar: **ningún buque navega la ortodrómica pura en la práctica**. El arco de círculo máximo corta cada meridiano con un ángulo distinto, por lo que seguirlo con fidelidad exigiría corregir el rumbo de aguja de forma continua, grado a grado y milla a milla — algo inviable de gobernar manualmente, y que tampoco se puede trazar como una recta sobre una carta Mercator (donde la ortodrómica aparece como la curva cóncava ya descrita en el apartado 1).

La solución operativa universal —empleada tanto en la navegación clásica de altura como en los sistemas de gestión de ruta (Voyage Planning) de los buques modernos— consiste en **trocear la ortodrómica en una serie de puntos intermedios (waypoints o "vértices de tramo")** situados sobre el propio arco de círculo máximo, típicamente cada $5^\circ$ o $10^\circ$ de diferencia de longitud, y navegar entre cada dos puntos consecutivos un **tramo loxodrómico recto** (rumbo constante, resuelto con las fórmulas de estima analítica del apartado 3 de `CALCULOS_DE_NAVEGACION.md`).

### Cálculo de los Puntos Intermedios
Para cada longitud intermedia elegida $L_x$ (comprendida entre $L_A$ y $L_B$), la latitud del punto correspondiente sobre el círculo máximo se obtiene con la fórmula clásica de Bowditch para puntos intermedios de la ortodrómica:

$$
\tan(l_x) = \frac{\tan(l_A)\cdot\sin(L_B - L_x) + \tan(l_B)\cdot\sin(L_x - L_A)}{\sin(L_B - L_A)}
$$

Uniendo sucesivamente estos puntos con segmentos de rumbo constante, la derrota resultante en la carta Mercator dibuja una **poligonal que aproxima visualmente la curva cóncava de la ortodrómica verdadera**. La pérdida de eficiencia frente al círculo máximo teórico es insignificante (unas pocas millas, tanto más pequeña cuanto más corto y numeroso es el tramo elegido), a cambio de una ganancia práctica enorme: cada tramo se gobierna con un rumbo de aguja fijo y se traza en la carta con la regla paralela, exactamente igual que cualquier derrota costera.

> [!NOTE]
> No hay que confundir esta técnica general de "troceado en waypoints" con la **Navegación Ortodrómica Mixta o Compuesta (Composite Sailing)** del apartado siguiente. El troceado en waypoints es una técnica de **gobierno práctico** (aproximar la curva con segmentos rectos) que se aplica siempre, incluso en rutas sin ninguna restricción. La navegación mixta, en cambio, es una técnica de **planificación estratégica** que deforma deliberadamente la ruta óptima para no sobrepasar un límite de latitud (hielo, tormentas). Ambas técnicas se combinan en la práctica: primero se decide la derrota óptima (pura o mixta) y, después, esa derrota —sea cual sea— se trocea en tramos loxodrómicos para navegarla.

---

## 3. Navegación Ortodrómica Mixta (Composite Great Circle Sailing)

Para ganar tiempo ahorrando millas, pero sin poner en riesgo mortal a la tripulación bajando a la zona de icebergs de los *Aulladores Cincuenta* ($50^\circ S$), se utiliza la ruta mixta.

Consiste en establecer un **Paralelo Límite ($l_{lim}$)** que el barco tiene prohibido cruzar. La derrota óptima se divide entonces en tres tramos:

1.  **Arco de Círculo Máximo 1**: Desde el Punto de Salida ($A$) tangenciando el Paralelo Límite en un punto ($V_1$).
2.  **Loxodrómica (Navegación por el Paralelo)**: Desde $V_1$, el barco navega exactamente al Este o al Oeste sobre el paralelo límite (rumbo constante $090^\circ$ o $270^\circ$) hasta alcanzar el punto $V_2$.
3.  **Arco de Círculo Máximo 2**: Desde $V_2$ abandonando el paralelo límite para descender tangencialmente hasta el Punto de Llegada ($B$).

### Cálculo Analítico mediante las Reglas de Napier
En los puntos $V_1$ y $V_2$, la ortodrómica es ortogonal al meridiano local (son vértices geométricos), formando **Triángulos Esféricos Rectángulos**. Esto simplifica drásticamente el cálculo utilizando la Regla del Pentágono de Napier:

$$
\sin(\text{parte central}) = \tan(\text{adyacentes}) \cdot \tan(\text{adyacentes}) = \cos(\text{opuestos}) \cdot \cos(\text{opuestos})
$$

Con Napier, es extremadamente rápido hallar las longitudes de tangencia ($L_{V1}$ y $L_{V2}$) y la distancia total del recorrido mixto.

---

## 4. Navegación en Altas Latitudes (Polar Navigation)

Más allá de los $60^\circ / 70^\circ$ Norte o Sur, las leyes de la navegación tradicional colapsan. 

### 4.1. Proyecciones Cartográficas
La proyección **Mercator cilíndrica**, estándar en toda la náutica (ver `cartas_nauticas/CONCEPTOS_BASICOS.md`, apartado 4, donde se explica por qué se usa y su límite de utilidad práctica en torno a los $80^\circ$ de latitud), **no sirve en los polos**. Como esa proyección debe separar progresivamente los paralelos para conservar los ángulos (conformidad), la escala tiende a infinito en el polo geográfico y la deformación de áreas se dispara: Groenlandia parece más grande que África. Un rumbo constante de $000^\circ$ trazado sobre una Mercator llevaría en teoría a una recta vertical que jamás llega a tocar el polo (asíntota matemática), lo que ilustra por sí solo que esta proyección deja de tener sentido físico en esas latitudes.
En latitudes polares, los buques cambian a cartas con proyección **Estereográfica Polar** (proyección azimutal sobre un plano tangente al polo).
*   En estas cartas, los meridianos son líneas rectas que irradian desde el centro (el polo).
*   Los paralelos son círculos concéntricos.
*   Una línea recta dibujada aquí aproxima un círculo máximo (ortodrómica), no una loxodrómica.

### 4.2. Colapso del Compás Magnético
La brújula no señala al Norte Geográfico, sino al **Polo Norte Magnético** (actualmente vagando por el Ártico canadiense/ruso).
*   **Fuerza Directriz Nula:** Cerca del polo magnético, las líneas de fuerza del campo magnético terrestre son casi verticales (hacia abajo). La aguja del compás trata de apuntar hacia el suelo (Inclinación Magnética), quedando atascada contra la tarjeta del compás. La componente horizontal que dirige la aguja es tan débil que el compás es inservible.
*   **Declinación Extrema:** La Declinación Magnética varía brutalmente en pocos kilómetros, pasando de $40^\circ \text{ W}$ a $40^\circ \text{ E}$.

### 4.3. Colapso del Compás Giroscópico
El girocompás busca el Norte Geográfico basándose en la velocidad de rotación de la Tierra. En el ecuador, la velocidad lineal es de $1670 \text{ km/h}$. En las latitudes polares, esta velocidad lineal tiende a cero. 
Sin el par de precesión generado por la rotación terrestre, el girocompás pierde su capacidad directriz y empieza a vagar inútilmente.

> [!IMPORTANT]
> **Solución Tecnológica de Altas Latitudes:** En los rompehielos y submarinos, el girocompás se desconecta de su función "buscadora de norte" y se pasa a modo **Giro Direccional Libre (Free Directional Gyro)**. El navegante fija un "Falso Ecuador" o "Grid Navigation", utilizando una cuadrícula sobre la carta estereográfica. El compás mantiene ese rumbo relativo puro en el espacio inercial y se corrige astronómicamente cada pocas horas.

### 4.4. El "Salto" de Cuadrante del Rumbo Ortodrómico

En rutas de latitud moderada, el rumbo inicial ortodrómico se aparta de la loxodrómica directa, pero de forma razonable (como se ve en el Ejemplo 2 al final de este tema, donde la diferencia ronda los $22^\circ$). Sin embargo, en rutas de **muy alta latitud** —o, en el caso extremo, rutas subpolares que pasan cerca del propio polo—, el rumbo inicial ortodrómico puede llegar a **superar los $90^\circ$ de apartamiento respecto al cuadrante "intuitivo"** que uniría ambos puntos en línea recta sobre una carta plana.

Esto ocurre porque, cuanto más cerca del polo transcurre la ruta, más se curva el círculo máximo alrededor de este: el rumbo de salida puede llegar a apuntar **casi hacia el propio polo** (próximo a $000^\circ$ o $180^\circ$) aunque el punto de llegada esté, en términos de longitud, mayoritariamente al Este o al Oeste del de salida. Es el mismo fenómeno que arroja el vértice a latitudes altísimas (apartado 1.4), llevado a su extremo: cuando la colatitud de ambos puntos es pequeña, el "polo" del triángulo esférico $P$-$A$-$B$ está tan próximo a los otros dos vértices que el ángulo en $A$ (el rumbo inicial) deja de guardar relación intuitiva con la dirección geográfica directa hacia $B$.

**Consecuencia práctica:** la fórmula de la cotangente (o de Napier) del apartado 1.2 es indispensable en estos casos, porque una simple estima "a ojo" de qué cuadrante debería tener el rumbo lleva a errores groseros; hay que resolver el triángulo esférico con rigor y comprobar el cuadrante final con el signo de los términos, exactamente como se advierte en la nota del apartado 1.3 sobre la ambigüedad de la Ley de Senos.

### 4.5. Límites de Hielo (Ice Limits) en Rutas Transoceánicas de Alta Latitud

Las grandes rutas de círculo máximo que cruzan el Atlántico Norte o el Pacífico Norte en derrota directa (por ejemplo, entre Norteamérica y Europa, o entre Japón y la costa oeste de EE.UU.) no pueden seguirse sin más hasta el vértice teórico: hay que respetar los **Límites de Hielo (Ice Limits)**, líneas de latitud variables (estacionales, no fijas como el paralelo límite del apartado 3) publicadas por organismos como la **International Ice Patrol** (nacida precisamente tras el hundimiento del *Titanic* en 1912, que navegaba una gran ruta transatlántica) y recogidas en las Derrotas (*Sailing Directions*) y Cartas Piloto (*Pilot Charts*) de cada época del año.
*   Estas líneas delimitan la extensión máxima observada o prevista de icebergs desprendidos de Groenlandia (Gran Banco de Terranova) o del hielo del Ártico y del Antártico (los *Aulladores Cincuenta*, ya mencionados en el apartado 3).
*   Cuando el vértice teórico de la ortodrómica cae dentro de la zona de hielo, el buque debe aplicar exactamente la técnica de **Navegación Ortodrómica Mixta** del apartado 3: sustituir el Paralelo Límite fijo por el límite de hielo vigente esa temporada, y navegar el tramo central sobre (o justo al Sur/Norte de) esa línea en vez de sobre el vértice puro.
*   La consecuencia operativa es la misma que en cualquier ruta mixta: se sacrifican unas pocas millas de la distancia ortodrómica teórica a cambio de eliminar el riesgo de colisión con hielo a la deriva, invisible de noche o con niebla incluso para el radar en determinadas condiciones.

---

## 5. Peligros de Hielos y Convención SOLAS

La formación de hielo no es solo un peligro por colisión (icebergs), sino por el **"Icing" (Acumulación de hielo en superestructuras)**.
Cuando la niebla engelante o el rocío de mar impactan contra los candeleros, mástiles y obenques a temperaturas bajo cero, se congelan instantáneamente.

**Peligro Crítico de Estabilidad:**
Toneladas de hielo acumulado en la jarcia elevan drásticamente el **Centro de Gravedad ($G$)** del buque. La distancia metacéntrica ($GM$) se reduce a cero o se hace negativa. El buque se escorará bruscamente y **zozobrará** (volcará).
*   **Maniobra de emergencia ante Icing:** Caer a un rumbo a favor del viento y de la mar (para reducir el rocío aparente relativo en la proa), reducir velocidad, y mandar tripulación con piquetas de bronce (anti-chispas) y mangueras de agua caliente para destruir el hielo de la superestructura inmediatamente.

## Ejemplos Prácticos

**Problema de Distancia Ortodrómica Básica:**
Un buque parte de Las Palmas de Gran Canaria ($l_A = 28^\circ 08' \text{ N}$, $L_A = 015^\circ 25' \text{ W}$) hacia San Juan de Puerto Rico ($l_B = 18^\circ 28' \text{ N}$, $L_B = 066^\circ 07' \text{ W}$). Calcule la distancia directa por Círculo Máximo.

*Solución:*
$\Delta L = 66^\circ 07' - 15^\circ 25' = 50^\circ 42'$.
$\cos(D) = \sin(28.13^\circ) \cdot \sin(18.46^\circ) + \cos(28.13^\circ) \cdot \cos(18.46^\circ) \cdot \cos(50.7^\circ)$
$\cos(D) = (0.4714 \cdot 0.3166) + (0.8818 \cdot 0.9485 \cdot 0.6333)$
$\cos(D) = 0.1492 + 0.5296 = 0.6788$
$D = \arccos(0.6788) = 47.24^\circ$
Para pasar los grados de distancia esférica a millas náuticas, multiplicamos por 60:
$D = 47.24^\circ \cdot 60 = \mathbf{2834.4 \text{ millas náuticas}}$.
*(La loxodrómica para esta misma ruta daría unas 2845 millas, ahorrando unas 10 millas, lo cual es modesto porque ambas latitudes son tropicales. En rutas como Japón-EEUU en paralelo 45, el ahorro asciende a más de 300 millas).*

---

**Problema Completo: Rumbo Inicial y Distancia en una Ruta de Alta Latitud Este-Oeste**

Un buque parte de un punto $A$ situado a $l_A = 45^\circ 00' \text{ N}$, $L_A = 010^\circ 00' \text{ W}$ (Atlántico Norte, altura de Galicia) con destino a un punto $B$ situado a $l_B = 45^\circ 00' \text{ N}$, $L_B = 070^\circ 00' \text{ W}$ (altura de Nueva Escocia, Canadá), es decir, dos puntos **exactamente sobre el mismo paralelo**, separados por $\Delta L = 60^\circ$ de longitud. Calcule (a) la Distancia Ortodrómica, (b) el Rumbo Inicial ortodrómico, y compárelo con el rumbo de la loxodrómica directa entre ambos puntos.

*Solución:*

**a) Distancia Ortodrómica ($D$)**, con $l_A = l_B = 45^\circ$ y $\Delta L = 60^\circ$:

$$
\cos(D) = \sin(45^\circ)\sin(45^\circ) + \cos(45^\circ)\cos(45^\circ)\cos(60^\circ)
$$

$$
\cos(D) = (0.70711 \cdot 0.70711) + (0.70711 \cdot 0.70711 \cdot 0.5) = 0.5 + 0.25 = 0.75
$$

$$
D = \arccos(0.75) = 41.4096^\circ \quad\Rightarrow\quad D = 41.4096^\circ \cdot 60 = \mathbf{2484.6 \text{ millas náuticas}}
$$

**b) Rumbo Inicial Ortodrómico ($R_i$)**, con la fórmula de la cotangente del apartado 1.2 (usando $\Delta L = 60^\circ$ hacia el Oeste):

$$
\cot(R_i) = \frac{\cos(45^\circ) \cdot \tan(45^\circ) - \sin(45^\circ) \cdot \cos(60^\circ)}{\sin(60^\circ)} = \frac{(0.70711 \cdot 1) - (0.70711 \cdot 0.5)}{0.86603} = \frac{0.35355}{0.86603} = 0.40825
$$

$$
R_i = \text{arccot}(0.40825) = 67^\circ 47' \quad\text{(cuadrantal, medido desde el Norte hacia el Oeste)}
$$

Es decir, $R_i = \text{N } 67^\circ 47' \text{ W}$, que en rumbo verdadero circular equivale a $360^\circ - 67^\circ 47' = \mathbf{292^\circ 13' \text{ (T)}}$.

*(Verificación cruzada mediante la Ley de Senos del apartado 1.3: $\sin(R_i) = \dfrac{\cos(l_B)\sin(\Delta L)}{\sin(D)} = \dfrac{0.70711 \cdot 0.86603}{0.66144} = 0.9259 \Rightarrow R_i = 67.79^\circ$, coincidente).*

**c) Comparación con la Loxodrómica directa:**
Como $l_A = l_B$, la diferencia de latitud es nula ($\Delta l = 0$), y la fórmula de estima analítica ($\Delta l = D_{loxo}\cdot\cos(R)$) solo se cumple con $\cos(R)=0$: el rumbo loxodrómico entre A y B es, por tanto, **exactamente $270^\circ$ (Oeste puro)**, navegando todo el tramo sobre el propio paralelo de $45^\circ$N. Su distancia es:

$$
D_{loxo} = \Delta L(\text{en minutos}) \cdot \cos(l_m) = 3600' \cdot \cos(45^\circ) = 3600 \cdot 0.70711 = \mathbf{2545.6 \text{ millas náuticas}}
$$

**Conclusión:** aunque el sentido común indica "poner rumbo 270° y navegar recto por el paralelo", el rumbo verdaderamente óptimo de salida es $292^\circ 13'$, **casi $22^\circ$ al Norte de la ruta loxodrómica directa**. El buque debe proyectar la proa visiblemente hacia el Noroeste al zarpar, remontar hasta el vértice —cuya latitud es $l_v = \arccos(\cos(l_A)\cdot\sin(R_i)) = \arccos(0.70711 \cdot 0.9259) = \arccos(0.6547) \approx 49^\circ 05' \text{ N}$— y descender simétricamente hasta B con un rumbo de aproximación final de $\text{S } 67^\circ 47' \text{ W} = 180^\circ + 67^\circ47' = \mathbf{247^\circ 47' \text{ (T)}}$, es decir, $22^\circ$ al Sur del rumbo directo (270°) en la llegada, simétrico respecto al de salida. El ahorro de distancia es de $2545.6 - 2484.6 \approx \mathbf{61 \text{ millas}}$ (un 2,4%), modesto en este caso porque $60^\circ$ de longitud es una separación moderada, pero el desvío de casi $22^\circ$ en el rumbo inicial —pese a partir y llegar en la misma latitud— ilustra bien por qué en rutas reales de este tipo (ver apartado 4.5, Gran Círculo del Atlántico Norte) el buque se ve empujado varios grados más al Norte de lo intuitivo, acercándose a las zonas de hielo y mal tiempo del apartado 4.
