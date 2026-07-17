# Patrón de Yate - Tema 4: Navegación Avanzada (Loxodrómica, Análisis Vectorial de Corrientes y Trigonometría Costera)

El examen de Patrón de Yate en la carta del Estrecho de Gibraltar (105) es un ejercicio absoluto de destreza geométrica y álgebra vectorial. La precisión en el trazado se entrelaza con el uso intensivo de trigonometría plana (loxodrómica) para trayectos largos y cálculos de cinemática de derroteros bajo influencia fluida.

---

## 1. Fundamentos Matemáticos de la Navegación Loxodrómica (Estima Analítica)

La Navegación por Estima Analítica ("Dead Reckoning" algorítmica) permite deducir las coordenadas latitud/longitud de llegada a partir de un punto de salida, resolviendo las ecuaciones diferenciales del movimiento sobre un elipsoide simplificado como plano ecuatorial (Trigonometría Plana de Corta Distancia).

El Rumbo Loxodrómico es aquel que corta todos los meridianos terrestres con un ángulo de incidencia constante. Sobre la proyección Mercator de la carta, se representa como una línea recta perfecta, aunque físicamente corresponda a una espiral que envuelve el polo sobre la esfera terrestre.

### 1.1 Deducción del Triángulo de Estima
Si partimos de unas coordenadas iniciales de Salida ($l_s, L_s$), mantenemos un Rumbo Verdadero ($R_v$) y navegamos una Distancia de corredera ($D$) en millas náuticas, el viaje traza la hipotenusa de un triángulo rectángulo diferencial en la superficie.

1.  **Diferencia de Latitud ($\Delta l$):** Proyección polar (Norte/Sur).
    Integrando el diferencial geográfico $dl = dD \cdot \cos(R_v)$:
    $$ \Delta l = D \cdot \cos(R_v) $$
    *El resultado es en minutos de grado (millas náuticas). Algebráico (+ Norte, - Sur). Latitud de llegada = $l_s + \Delta l$.*

2.  **Apartamiento ($A$):** Longitud del arco paralelo (Este/Oeste) medido en millas físicas.
    $$ A = D \cdot \sin(R_v) $$

3.  **Latitud Media ($l_m$):** Como la Tierra es esférica, la separación física de los meridianos es máxima en el ecuador y colapsa a 0 en los polos. El apartamiento se ajusta tomando la secante de la latitud promedio de la travesía:
    $$ l_m = \frac{l_s + l_{\text{llegada}}}{2} $$

4.  **Diferencia de Longitud ($\Delta L$):** Proyección ecuatorial angular, requerida para calcular el meridiano final.
    $$ \Delta L = \frac{A}{\cos(l_m)} = A \cdot \sec(l_m) $$
    *(Resultado en minutos angulares. Algebráico: + Este, - Oeste. Longitud de llegada = $L_s + \Delta L$)*.

### 1.2 Problema Inverso (Determinación Analítica del Vector Directo)
Para efectuar operaciones de salvamento hacia unas coordenadas de rescate precisas ($l_{\text{llegada}}, L_{\text{llegada}}$):
1.  Hallar $\Delta l$ y $\Delta L$ por sustracción algebraica.
2.  Calcular $l_m$ y despejar Apartamiento: $A = \Delta L \cdot \cos(l_m)$
3.  Determinar el Rumbo Directo (Tangente):
    $$ \tan(R_v) = \frac{A}{\Delta l} $$
    *(Se obtiene un ángulo de cuadrante. Si $\Delta l < 0$ y $A > 0$, el rumbo es del 2º Cuadrante, es decir, el $R_v$ final será $180^\circ - \text{ángulo}_{\text{calculado}}$.)*
4.  Distancia al objetivo (Euclidiana):
    $$ D = \frac{\Delta l}{\cos(R_v)} $$

---

## 2. Abatimiento: Dinámica Aerodinámica Transversal

La acción de las partículas de viento sobre la obra muerta del buque genera una fuerza lateral que, conjugada con la resistencia hidrodinámica longitudinal, produce un ángulo de guiñada asimétrica: el **Abatimiento ($A_b$)**.

$$ R_s = R_v + A_b $$
Donde $R_s$ es el **Rumbo de Superficie**, es decir, el vector estela real sobre el mar.

**Convenio de Signos Analítico:**
*   Viento recibiendo por la aleta o amura de **Babor**: Empuje lateral a Estribor. Abatimiento hacia la derecha. $\Rightarrow \mathbf{A_b > 0}$
*   Viento recibiendo por la aleta o amura de **Estribor**: Empuje lateral a Babor. Abatimiento hacia la izquierda. $\Rightarrow \mathbf{A_b < 0}$

*(El cálculo magistral del puente dicta que para trazar el Rumbo de Aguja en el compás magistral: $R_a = R_s - A_b - C_t$)*.

---

## 3. Cinemática Exacta del Vector Corriente

La corriente oceánica arrastra pasivamente todo el dominio hidro-espacial del barco, introduciendo una componente de traslación inercial galileana pura. Sus componentes son el Rumbo de la Corriente ($R_c$) y la Intensidad Horaria de Corriente ($I_{hc}$ en nudos).

### 3.1 Geometría del Problema Directo (¿Dónde caeremos?)
Si aplicamos nuestras máquinas para hacer un Rumbo de Superficie ($R_s$) a una Velocidad de Buque ($V_b$), y sufrimos un sistema de corriente ($R_c, I_{hc}$):

$$ \vec{V}_{\text{efectiva}} = \vec{V}_{\text{buque}} + \vec{V}_{\text{corriente}} $$

En el plano vectorial cartesiano ($x=$ Este, $y=$ Norte):
$$ V_{x, \text{efectivo}} = V_b \cdot \sin(R_s) + I_{hc} \cdot \sin(R_c) $$
$$ V_{y, \text{efectivo}} = V_b \cdot \cos(R_s) + I_{hc} \cdot \cos(R_c) $$
$$ R_{\text{efectivo}} = \arctan\left(\frac{V_{x, \text{efectivo}}}{V_{y, \text{efectivo}}}\right) $$
$$ V_{\text{efectiva}} = \sqrt{V_{x, \text{efectivo}}^2 + V_{y, \text{efectivo}}^2} $$

El **Rumbo Efectivo ($R_{ef}$)** es la traza sobre el suelo del fondo oceánico; la **Velocidad Efectiva ($V_{ef}$)** es la celeridad absoluta respecto a un satélite.

### 3.2 Geometría del Problema Inverso (Solución Táctica de Intercepción)
Requerimos innegociablemente navegar sobre una trayectoria geométrica (Rumbo Efectivo deseado para llegar a puerto) bajo fuertes mareas del Estrecho. Debemos hallar el **Rumbo Verdadero (ángulo de cangrejo)** de la proa.

**Método Gráfico en Carta (Ley de los Senos aplicados al Triángulo):**
1.  Situación de Origen $\rightarrow$ Trazar infinito el segmento del $R_{ef}$ deseado.
2.  Desde el Origen, situar el vector de corriente $(R_c, I_{hc})$ a escala. El extremo de este vector es el origen virtual de proa.
3.  Con el compás metálico calibrado a la magnitud modular de nuestra $V_b$, apoyando en el extremo del vector corriente, trazamos un arco que interseque con el rayo infinito del $R_{ef}$.
4.  La línea que une el extremo del vector corriente con la intersección dicta el ángulo exacto al que debemos poner nuestra proa, compensando isométricamente la deriva de la masa fluida.

---

## 4. Trigonometría de Situación Costera de Precisión

### 4.1 Triangulación por Demoras (Error de Somville)
Tres o más Demoras Verdaderas ($D_v$) intersecan idóneamente en un punto euclidiano simple. Sin embargo, debido al error sistemático y accidental (vibración, paralaje, aguja), conforman el **Triángulo de Error**. El lugar geométrico de máxima verosimilitud de la posición baricéntrica, según el axioma de Somville, reside en el incentro/ortocentro del polígono formado, si el error magnético es constante en los tres relevamientos.

### 4.2 Arco Capaz (Técnica Analítica de Ángulos Horizontales)
Es el método de posicionamiento más resiliente pues resulta matemáticamente indemne frente a errores magnéticos o de desvío del compás. Se efectúa operando un sextante naval en plano paralelo al horizonte, extrayendo el arco angular real ($\alpha$) entre dos faros colineales $A$ y $B$.

El locus geográfico resultante pertenece al **Arco Capaz** geométrico que subtende el segmento $\overline{AB}$.
Para hallar los centros de la circunferencia en la carta:
1.  Unimos ambos faros $A$ y $B$. Trazamos su mediatriz de forma analítica (ortogonal de punto medio).
2.  En el faro $A$ y en el $B$, levantamos sendos rayos a $90^\circ - \alpha$ de la línea base (si el ángulo del sextante $\alpha$ es $< 90^\circ$).
3.  La intersección del rayo con la mediatriz dicta las coordenadas precisas del Centro ($O$) de la circunferencia isométrica. Apoyando el compás, el trazo englobará A, B, y todas las posibles situaciones del yate en el mar.
