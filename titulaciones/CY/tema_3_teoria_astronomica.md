# Capitán de Yate - Tema 3: Teoría Astronómica y Astrofísica Avanzada

Para dominar el cálculo de posiciones mediante el sextante, el Capitán de Yate debe visualizar y comprender con precisión geométrica el universo observable desde nuestro planeta, así como la mecánica física que altera sutilmente estas observaciones. Esta abstracción requiere proyectarse al centro del Universo de forma puramente matemática.

---

## 1. La Esfera Celeste y el Paradigma del Geocentrismo Náutico

En la navegación astronómica moderna, **revertimos funcionalmente a la teoría geocéntrica de Ptolomeo**. A efectos de cálculo de trigonometría esférica, la Tierra está absolutamente quieta en el centro exacto del Universo, y todos los astros (Sol, Luna, planetas y el firmamento estelar) están adosados a la pared interior de una Esfera Celeste de radio infinito que gira de Este a Oeste.

### Puntos, Ejes y Planos de Referencia Absoluta
*   **Eje del Mundo:** La prolongación geométrica infinita del eje de rotación terrestre. Corta la bóveda en el **Polo Norte Celeste ($Pn$)** (próximo a Polaris, $\alpha$ Ursae Minoris) y el **Polo Sur Celeste ($Ps$)** (próximo a Sigma Octantis).
*   **Ecuador Celeste ($QQ'$):** Extensión del plano del Ecuador Terrestre hacia el infinito. Divide la esfera en Hemisferio Norte Celeste y Sur Celeste. Es el plano fundamental de declinación.
*   **La Vertical del Observador ($ZZ'$):** La recta topocéntrica (plomada) que une el centro de la Tierra, el observador y el infinito celeste. 
    *   **Cenit ($Z$):** Intersección superior de la vertical con la Esfera Celeste.
    *   **Nadir ($Z'$):** Intersección inferior, diametralmente opuesta.
*   **Horizonte Astronómico o Racional ($HH'$):** El plano que pasa por el centro de la Tierra y es ortogonal ($90^\circ$) a la Vertical del Observador. No debe confundirse con el Horizonte Aparente o de la Mar, deprimido por la altitud del ojo del navegante.
*   **Eclíptica:** La trayectoria aparente anual del Sol sobre la Esfera Celeste. Se encuentra inclinada respecto al Ecuador Celeste unos $23^\circ 27'$ (Oblicuidad de la Eclíptica), marcando los Trópicos.

```mermaid
stateDiagram-v2
    direction LR
    state "Esfera Celeste Absoluta" as EC {
        EjeDelMundo --> PoloNorteCeleste
        EjeDelMundo --> PoloSurCeleste
        PoloNorteCeleste --> EcuadorCeleste : Ortogonal (90º)
    }
    state "Dinámica Orbital Terrestre" as Orb {
        PlanoOrbital --> Ecliptica
        Ecliptica --> Oblicuidad : Inclinación 23º27'
        EcuadorCeleste --> Interseccion_Equinoccial
        Ecliptica --> Interseccion_Equinoccial
        Interseccion_Equinoccial --> PuntoAries : Nodo Ascendente (Primavera)
        Interseccion_Equinoccial --> PuntoLibra : Nodo Descendente (Otoño)
    }
    state "Topocentrismo del Observador" as Topo {
        CentroTierra --> Vertical_ZZ
        Vertical_ZZ --> Cenit_Z
        Vertical_ZZ --> Horizonte_Racional : Plano Ortogonal
        EcuadorCeleste --> Altura_Ecuador : 90º - Latitud
        PoloNorteCeleste --> Altura_Polo : Igual a Latitud
    }
    EC --> Orb
    EC --> Topo
```

```mermaid
graph TD
    A[Cenit] ---|Vertical Z-Z'| B(Observador en la Tierra)
    B ---|Vertical Z-Z'| C[Nadir]
    D[Horizonte Astronómico] --- B
    E[Polo Norte Celeste Pn] --- B
    F[Ecuador Celeste QQ'] --- B
    style B fill:#f9f,stroke:#333,stroke-width:4px
```

---

## 2. Astrofísica: Movimientos Complejos y Mecánica Celeste

El eje de la Tierra y sus órbitas no son perfectas, introduciendo variaciones astrofísicas que obligan a recalibrar el Almanaque Náutico cada año.

### Precesión de los Equinoccios
La Tierra no es una esfera perfecta; tiene un ensanchamiento ecuatorial. La atracción gravitatoria combinada de la Luna y el Sol sobre este abultamiento produce un momento de fuerza que hace que el eje de rotación de la Tierra describa un cono inmenso, como una peonza perdiendo inercia.
*   **Período:** Un ciclo de precesión dura aproximadamente **25.772 años** (Año Platónico).
*   **Efecto Náutico:** El Punto de Aries (el $0^\circ$ de Ascensión Recta) retrocede a lo largo de la eclíptica unos $50.3$ segundos de arco por año. Además, la Estrella Polar no será siempre la estrella del Norte (en el año 14.000 d.C., será Vega).

### Nutación y Bamboleo de Chandler
*   **Nutación:** Una pequeña oscilación o "cabeceo" superpuesta al cono de precesión, debida principalmente a la inclinación de la órbita de la Luna (5º sobre la eclíptica) y la regresión de sus nodos. Tiene un período principal de 18,6 años y una amplitud de 9 segundos de arco.
*   **Bamboleo de Chandler (Chandler Wobble):** Un pequeño movimiento irregular de los polos geográficos sobre la superficie terrestre (unos 9 metros) con un período de 433 días, producto de la distribución de masas fluidas y sólidas del planeta.

### Leyes de Kepler y la Ecuación del Tiempo
1.  **Órbitas Elípticas:** La Tierra orbita al Sol en una elipse. En el **Perihelio** (enero), estamos más cerca y la velocidad orbital de la Tierra es mayor. En el **Afelio** (julio), estamos más lejos y vamos más lentos.
2.  **Ecuación del Tiempo ($E$):** Como la velocidad orbital terrestre varía (y la eclíptica está inclinada), el "Sol Verdadero" a veces se adelanta y a veces se atrasa respecto a un "Sol Medio" imaginario que usaría un reloj atómico. La diferencia entre el Sol Verdadero (Almanaque) y el Sol Medio (Reloj) es la Ecuación del Tiempo, que puede llegar a $\pm 16$ minutos, siendo crítica para calcular la hora exacta de la Culminación del Meridiano.

---

## 3. Los Tres Sistemas de Coordenadas Celestes

### 3.1. Coordenadas Horizontales Topocéntricas (La Visión del Sextante)
Relativas a la posición y horizonte del navegante.
*   **Altura ($a$):** Ángulo vertical desde el Horizonte Astronómico ($0^\circ$) hasta el astro (máximo $90^\circ$ en el Cenit). Si $a < 0$, el astro no es visible.
*   **Azimut ($Z$ / $Zv$):** Ángulo en el plano horizontal desde el Polo Elevado (Norte verdadero $= 000^\circ$) girando en sentido horario ($0^\circ$ a $360^\circ$) hasta el círculo vertical que pasa por el astro.
*   **Distancia Cenital ($z$):** El complemento de la Altura. $z = 90^\circ - a$.

### 3.2. Coordenadas Ecuatoriales Locales y Absolutas (El Almanaque)
*   **Declinación ($\delta$ o $Dec$):** Distancia angular desde el Ecuador Celeste. Va de $0^\circ$ a $90^\circ$ Norte (+) o Sur (-). Equivalente cósmico de la **Latitud**.
*   **Ángulo Horario Local ($hL$):** Ángulo de $0^\circ$ a $360^\circ$ hacia el **Oeste**, medido desde el meridiano superior del observador hasta el semicírculo horario del astro.
*   **Ángulo Horario en Greenwich ($hG$):** Exactamente igual pero medido desde el Meridiano Principal (Greenwich).
    $$ hL = hG + L_{\text{observador}} $$ (Adoptando longitud Este +, Oeste -).

### 3.3. Coordenadas Ecuatoriales Uranográficas (Fijas en las Estrellas)
Para catalogar estrellas estáticas, se usa el "Greenwich de las Estrellas", que es el **Punto Vernal o Primer Punto de Aries ($\gamma$)** (donde el Sol cruza al Norte del ecuador en Primavera).
*   **Ángulo Sidéreo ($AS$):** Ángulo medido de Este a **Oeste** desde el Meridiano de Aries hasta la estrella.
*   **Ascensión Recta ($AR$ o $\alpha$):** Se mide de Oeste a **Este**. Por tanto, $AR = 360^\circ - AS$. Se suele medir en horas (0 a 24h).
    $$ hG_{\text{estrella}} = hG_{\text{Aries}} + AS_{\text{estrella}} $$

---

## 4. El Triángulo Esférico de Posición (Trigonometría Astronómica)

La navegación es la resolución pura del gigantesco triángulo curvado dibujado en la superficie de la bóveda celeste por los arcos de círculo máximo.

### Los Vértices, Lados y Ángulos
**Vértices:**
1.  **Polo Elevado ($Pn$ o $Ps$):** Polo de mismo nombre que la latitud de estima.
2.  **Cenit ($Z$):** El punto sobre la cabeza del observador.
3.  **Astro ($A$):** La posición proyectada del objeto observado.

**Lados (Arcos):**
*   **Colatitud ($c$):** $90^\circ - l_e$. Arco del Polo al Cenit.
*   **Codeclinación o Distancia Polar ($\Delta$):** $90^\circ - Dec$. Arco del Polo al Astro. Si Latitud y Declinación tienen distinto nombre, la Distancia polar es $90^\circ + Dec$.
*   **Distancia Cenital ($z$):** $90^\circ - a_e$. Arco del Cenit al Astro.

**Ángulos de los vértices:**
*   **Ángulo en el Polo ($P$):** Formado entre el meridiano local y el del astro. Es la versión semicircular del $hL$ (se mide de $0^\circ$ a $180^\circ$ hacia el E o W).
*   **Ángulo Cénit o Azimutal ($Z$):** Ángulo en el vértice del Cenit.
*   **Ángulo Paraláctico ($q$):** Ángulo en el vértice del Astro. Poco usado en navegación, vital en astronomía para orientación de telescopios.

Para resolver este triángulo y hallar la Altura Estimada ($a_e$) y el Azimut ($Z$), utilizamos la **Ley de los Cosenos para lados esféricos** (conocida en náutica como *Fórmula de la Cosenusa*):

$$ \cos(z) = \cos(c) \cdot \cos(\Delta) + \sin(c) \cdot \sin(\Delta) \cdot \cos(P) $$

Sustituyendo por Lat, Dec y $a_e$:

$$ \sin(a_e) = \sin(l_e) \cdot \sin(Dec) + \cos(l_e) \cdot \cos(Dec) \cdot \cos(P) $$

---

## 5. Fenómenos Celestes Críticos

### Tránsito o Culminación (Paso por el Meridiano)
Cuando el $hL = 0^\circ$ (paso superior) o $180^\circ$ (paso inferior). El astro alcanza la altura máxima, $P = 0$ y su Azimut es exactamente Norte o Sur. La derivada del arco cenital respecto al tiempo es cero, haciendo el cálculo inmensamente sencillo para determinar Latitud de manera analítica directa sin fórmulas trigonométricas (Meridiana).

### Las Fases del Crepúsculo
El horizonte es indispensable para la observación, al igual que las estrellas. La intersección funcional donde ambos son visibles es mínima.
*   **Crepúsculo Civil ($0^\circ$ a $-6^\circ$):** El cielo está muy iluminado por dispersión atmosférica de Rayleigh. Las estrellas mayores aún no compiten con el fondo celeste.
*   **Crepúsculo Náutico ($-6^\circ$ a $-12^\circ$):** **La Ventana Crítica.** Dura de 20 a 45 minutos dependiendo de la latitud. Suficiente oscuridad para identificar estrellas de 1ª y 2ª magnitud, pero con remanente lumínico que permite ver el recorte afilado del horizonte de la mar en los espejos del sextante. Si se dilata la observación a $-11^\circ$, el error en altura se dispara porque el horizonte de la mar real se confunde con las bandas de oscuridad superficial.
*   **Crepúsculo Astronómico ($-12^\circ$ a $-18^\circ$):** Oscuridad inservible para el sextante marino (aunque existen sextantes de burbuja artificial o visores nocturnos para estos casos extremos, no regulados en CY).

---

## Ejemplos Prácticos

**Problema 1: Teorema del Coseno para el Triángulo de Posición**
Calcule la Altura Estimada ($a_e$) de la estrella Sirio para un observador situado en la latitud $l_e = 40^\circ 00.0' \text{ N}$. Los datos del Almanaque arrojan que Sirio tiene una declinación $Dec = 16^\circ 42.9' \text{ S}$ y el Ángulo en el Polo es $P = 45^\circ$ hacia el Oeste.

*Solución:*
Fórmula de la altura estimada:
$$ \sin(a_e) = \sin(l_e) \cdot \sin(Dec) + \cos(l_e) \cdot \cos(Dec) \cdot \cos(P) $$

Criterio de signos: Al ser la Latitud Norte (+) y la Declinación Sur (-), tomaremos el primer término como negativo en la suma. Para evitar errores, usamos valores con signo: $l_e = +40^\circ$, $Dec = -16.715^\circ$, $P = 45^\circ$.

$$ \sin(a_e) = \sin(40^\circ) \cdot \sin(-16.715^\circ) + \cos(40^\circ) \cdot \cos(-16.715^\circ) \cdot \cos(45^\circ) $$
$$ \sin(a_e) = (0.6428 \cdot -0.2876) + (0.7660 \cdot 0.9577 \cdot 0.7071) $$
$$ \sin(a_e) = -0.1849 + 0.5187 = 0.3338 $$
Despejando la altura estimada:
$$ a_e = \arcsin(0.3338) \approx 19.50^\circ = 19^\circ 30' $$
La Altura Estimada de Sirio será de $19^\circ 30'$.

**Problema 2: Matriz de Rotación para Transformación de Coordenadas de Nutación Estelar**
El punto vernal de Aries ($\gamma$) sufre una retrogradación anual (Precesión) y una oscilación (Nutación). Para calcular la Ascensión Recta aparente ($\alpha_{ap}$) de la estrella Capella desde sus coordenadas medias catalogadas ($\alpha_m$, $\delta_m$), debemos aplicar las correcciones astrofísicas.
Suponga una variación temporal en longitud de nutación $\Delta \psi = 15''$ y una variación en oblicuidad $\Delta \epsilon = -8''$. Si la oblicuidad media de la eclíptica es $\epsilon = 23.43^\circ$ y Capella tiene $\alpha_m = 5^h 16^m 41^s$ ($79.17^\circ$), $\delta_m = +45.99^\circ$.
Calcule la corrección total en Ascensión Recta ($\Delta \alpha$) por nutación.

*Solución:*
La fórmula diferencial rigurosa de la trigonometría esférica para la corrección en $\alpha$ debida a la nutación es:
$$ \Delta \alpha = (\cos \epsilon + \sin \epsilon \cdot \sin \alpha \cdot \tan \delta) \cdot \Delta \psi - (\cos \alpha \cdot \tan \delta) \cdot \Delta \epsilon $$
Transformando a radianes y grados decimales:
$\alpha = 79.17^\circ$, $\delta = 45.99^\circ$, $\epsilon = 23.43^\circ$.
Calculamos los términos trigonométricos:
$\cos(23.43^\circ) = 0.9175$
$\sin(23.43^\circ) = 0.3976$
$\sin(79.17^\circ) = 0.9822$
$\cos(79.17^\circ) = 0.1879$
$\tan(45.99^\circ) = 1.0351$
Sustituyendo en el primer término (factor de $\Delta \psi$):
$$ F_1 = 0.9175 + (0.3976 \cdot 0.9822 \cdot 1.0351) = 0.9175 + 0.4042 = 1.3217 $$
Sustituyendo en el segundo término (factor de $\Delta \epsilon$):
$$ F_2 = 0.1879 \cdot 1.0351 = 0.1945 $$
Ecuación completa de $\Delta \alpha$:
$$ \Delta \alpha = (1.3217 \cdot 15'') - (0.1945 \cdot -8'') = 19.825'' + 1.556'' = 21.381'' \text{ de arco} $$
En tiempo ($\div 15$): $\Delta \alpha_t = +1.425 \text{ segundos de tiempo}$.
Esta corrección microscópica la asume el Almanaque internamente, pero es esencial para la programación de efemérides en software ECDIS avanzado.

**Problema 3: Ecuación del Tiempo y Hora del Tránsito Superior del Sol**
Calcule la Hora Civil del Lugar (HCL) y la Hora Universal (UTC) exacta del tránsito superior del Sol (Paso por el Meridiano, donde $Azimut = 180^\circ$ o $000^\circ$ y la altura es máxima) para un buque en Longitud $L = 120^\circ 45' \text{ W}$. La Ecuación del Tiempo ($E$) interpolada para ese día es $E = -14^m 22^s$ (El Sol Verdadero retrasa sobre el Medio).

*Solución:*
1. **Definición Astronómica:** El Paso por el Meridiano ocurre cuando el Ángulo Horario Local del Sol Verdadero ($h_{L\odot}$) es exactamente $0^\circ$ ($00^h 00^m 00^s$).
2. **Relación de Tiempos:** La Hora Civil del Lugar (HCL) cuenta el tiempo desde la medianoche inferior del Sol Medio. Por tanto, el Sol Medio cruza el meridiano superior a las $12:00:00 \text{ HCL}$.
3. **Aplicación de la Ecuación del Tiempo ($E$):**
Dado que $E = \text{HCL (Medio)} - \text{HVL (Verdadero)}$ (o dependiendo de la convención de signo, el Almanaque náutico define a veces $E$ para sumarlo directamente). Si $E = -14^m 22^s$ y el sol retrasa, la Culminación del Sol Verdadero se producirá $14^m 22^s$ DESPUÉS de las 12:00 HCL.
Hora de Paso (HCL): $12^h 00^m 00^s + 14^m 22^s = 12^h 14^m 22^s$.
4. **Cálculo de UTC (Universal Time Coordinated):**
La longitud determina la diferencia de hora con Greenwich.
Longitud en tiempo = $120^\circ 45' / 15 = 8^h 03^m 00^s$.
Como la longitud es Oeste, Greenwich está más adelantado en el tiempo:
$$ UTC = \text{HCL} + \text{Longitud (W)} = 12^h 14^m 22^s + 8^h 03^m 00^s = 20^h 17^m 22^s $$
A esa precisa HORA UTC, el observador en el Pacífico levantará el sextante para medir la Latitud directamente sin cálculos trigonométricos.

---

## Referencias Bibliográficas y Jurisprudencia

*   **Bibliografía Recomendada:**
    *   *Astronomía Náutica*, Moreu Curbera. Obra magna de la náutica hispana.
    *   *The American Practical Navigator (Bowditch)*. Editado por la NGA.
*   **Convenciones OMI:**
    *   IMO Model Course 7.03 (Officer in Charge of a Navigational Watch): Detalla las exigencias obligatorias de la navegación celestial astronómica a bordo.
*   **Jurisprudencia (Admiralty Court):**
    *   *The "Lady Gwendolen" (1965)*: Aunque se centró en el radar, estableció el precedente legal de que el uso inapropiado o el desconocimiento de los instrumentos y técnicas de posicionamiento clásicos a bordo por parte del mando constituye grave negligencia e incompetencia técnica que rompe la limitación de responsabilidad del armador.
