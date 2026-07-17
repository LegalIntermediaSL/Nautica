# PER - Tema 13: Anexo - Física Óptica y Los Faros de España

Aunque el temario oficial del PER cubre las señales luminosas dentro del bloque de Balizamiento, la comprensión de un sistema de ayuda a la navegación exige conocer la física óptica de la refracción y el cálculo del alcance de luz frente al horizonte elipsoidal. España cuenta con una red de 187 faros monumentales, guardianes ingenieriles de su complejo litoral.

---

## 1. El Libro de Faros e Interpretación Cartográfica

El **Instituto Hidrográfico de la Marina (IHM)** publica el catálogo de ayudas visuales. La leyenda en una Carta Mercator (p. ej., INT-1) condensa el funcionamiento fotométrico del faro.

### Descodificación de Frecuencias:
> **GpD(3) B 15s 50m 22M**

*   **Característica:** `GpD(3)` (Fl(3)). Grupo de destellos. El ciclo temporal de destellos y eclipses.
*   **Color:** `B` (Blanco / White `W`), minimizando la dispersión espectral (Ley de dispersión de Rayleigh en nieblas finas).
*   **Periodo ($T$):** `15s`. Tiempo entre el inicio de un ciclo y el inicio del siguiente repitiendo el patrón de fotones exactamente.
*   **Elevación focal ($E$):** `50m`. La distancia desde el filamento emisor de fotones hasta el Nivel Medio de las Pleamares Vivas o Cero Hidrográfico.
*   **Alcance Nominal ($D_N$):** `22M`. Intensidad luminosa calibrada según la ecuación empírica de Allard, definida a una transparencia atmosférica $T=0.74$.

## 2. Ingeniería Óptica, Refracción y Fresnel

Antes de 1822, las lámparas de Argand usaban reflectores parabólicos metálicos (sistema catóptrico) que absorbían el 50% de la energía. Augustin-Jean Fresnel diseñó el sistema **Dióptrico** (lentes) y **Catadióptrico** (lentes + prismas de refracción total).
Las **Lentes de Fresnel** están formadas por anillos prismáticos concéntricos que curvan todos los rayos de la fuente divergente (bombilla halógena o LED focalizado) hacia el infinito.
Aplicando la Ley de Snell ($n_1 \sin(\theta_1) = n_2 \sin(\theta_2)$) a la geometría del vidrio, Fresnel logró haces horizontales casi paralelos con divergencias microscópicas menores a $1^\circ$, intensificando la candela luminosa de miles a millones de unidades.

### 2.1. Alcance Geográfico y Trigonometría Esférica

El impedimento definitivo de la visibilidad no es la fotonesfera, sino la litosfera: la curvatura del planeta interrumpe el trayecto del haz rectilíneo ($c = 3\times 10^8 \text{ m/s}$).
El cálculo del alcance en navegación costera utiliza trigonometría asumiendo una refracción atmosférica estándar (la luz tiende a "doblarse" ligeramente hacia la tierra por el gradiente de densidad térmica, agrandando el horizonte en torno al 8%).

La distancia en millas marinas $d$ a la que un objeto de altura $E$ es tangente al horizonte visible para un observador en un punto elevado $e$ se calcula analíticamente derivando el Teorema de Pitágoras sobre el elipsoide expandido para refracción:
$$ d_{\text{geo}} = 2,08 \cdot \left(\sqrt{E} + \sqrt{e}\right) $$
Donde $d_{\text{geo}}$ es el resultado en millas, $E$ es la elevación focal del faro y $e$ es la altura del ojo del observador (ambas variables insertadas obligatoriamente en metros).

> [!TIP]
> **Umbral Lógico de Avistamiento:**
> La detección ocular ($d_{\text{real}}$) estará gobernada por la función MÍNIMA entre lo que permite la termodinámica atmosférica ($D_L$, Alcance Luminoso) y la trigonometría terrestre ($d_{\text{geo}}$):
> $$ d_{\text{real}} = \min(D_L, d_{\text{geo}}) $$

## 3. Catálogo Monumental e Hitos de Geoposicionamiento

### 3.1. Galicia: El Corredor de Finisterre
*   **Torre de Hércules (A Coruña):** Faro romano del s.I d.C. ($57 \text{ m}$). Su fuego alimentado por aceite de oliva se ha transformado hoy en bombillas de haluro metálico marcando el Golfo Ártabro.
*   **Faro de Cabo Finisterre:** Erigido en 1853, marca el principal Waypoint de los buques VLOC y petroleros europeos navegando el dispositivo de separación de tráfico de Finisterre (TSS).
*   **Faro de Cabo Vilán:** El primer hito histórico iluminado eléctricamente en España (1896) por una máquina de vapor de corriente continua. $105 \text{ m}$ de altura plano-focal, crucial en la siniestra Costa da Morte.

### 3.2. Cornisa Cantábrica
*   **Faro de Cabo Mayor (Santander):** Faro de recalada a $91 \text{ m}$, construido sobre un promontorio de estratos de caliza erosionados por el empuje brutal de las olas de viento noroccidental.
*   **Faro de Cabo Peñas (Asturias):** Posee uno de los alcances fotométricos más brutales de Europa septentrional: 35 millas náuticas para librar los acantilados verticales asturianos y el bajo de la Romanela.

### 3.3. Estrecho y Golfo de Cádiz
*   **Faro de Chipiona (Cádiz):** Monumento ciclópeo y máximo rascacielos náutico nacional ($69 \text{ m}$). Proyectado en tubo hueco estilo torreón ahusado de sillería labrada. Actúa como el sistema de intercepción visual clave para esquivar la Baja de Salmedina al enfilar hacia el Río Guadalquivir.
*   **Faro de Punta Tarifa:** Extremo sur continental europeo, dominando la cinemática de corrientes termohalinas extremas en el Estrecho y dictaminando la linde entre las aguas de Atlántico y Mediterráneo.

### 3.4. Levante y Baleares (Cinturón Mediterráneo)
*   **Faro de Cabo de Palos (Murcia):** Luz estroboscópica de salvamento marcando una sierra submarina brutal rematada en las Islas Hormigas, tumba de innumerables buques que no calibraron bien la corrección por abatimiento.
*   **Faro de Formentor (Mallorca):** Obra titánica colgando al vacío a $210 \text{ m}$ sobre el Cero Hidrográfico.
*   **Faro de La Mola (Formentera):** Instalado a $120 \text{ m}$ en acantilado vertical. Referencia geodésica esencial para los barcos roro procedentes del magreb.

### 3.5. Arcos Volcánicos Canarios
*   **Faro de Orchilla (El Hierro):** Histórico Meridiano $0^\circ$ ptolemaico europeo hasta 1884.
*   **Faro de Maspalomas (Gran Canaria):** Construido a base de bloques de cantería transportados por el mar. Faro de primera orden clave en las escalas carboneras trasatlánticas del siglo XIX hacia Sudamérica.

## 4. Técnicas de Recalada de Precisión Geométrica

Cuando los sistemas GNSS sufren "spoofing", interferencias solares o pérdida total de potencia, la navegación astronómica y visual es la última línea de defensa.
1.  **Líneas de Enfilación:** Posicionamiento hiper-preciso sin calculadora. Alinear el faro frontal (menor elevación $E$) con un faro o marca trasera (mayor elevación) genera una recta infinita que delimita matemáticamente una canal navegable. Al mantener las dos luces superpuestas verticalmente en el centro del ocular del timón, el error transversal es $0$.
2.  **Sectores Isofasés y de Color:** Cristales policromáticos de filtración de onda insertados dentro de la linterna del faro.
    *   Luz Blanca: Canal seguro y mar profundo.
    *   Luz Roja / Verde: Sector angular de peligro, rocas perimetrales o bajo calado.
3.  **Looming vs. Range:** Un observador podría divisar los fotones del faro colisionando y reflejándose elásticamente contra estratocúmulos a media altura (Looming o Resplandor), anticipando la posición visual mucho antes de que se produzca la intercepción trigonométrica del foco de luz en línea recta sobre el horizonte aparente del observador (Range). No se deben tomar demoras matemáticas a un looming, sólo al bulbo directo de luz focalizada.

## Ejemplos Prácticos

**Problema 1: Límite Termodinámico y Geométrico del Haz de un Faro**
A bordo de un buque mercantil, el observador tiene los ojos situados a una altura $e = 15 \text{ m}$ sobre el nivel del mar. Se aproxima de noche a un faro costero cuya elevación focal es $E = 81 \text{ m}$ y su alcance nominal tabulado (intensidad óptica pura) es $D_N = 20 \text{ millas}$. Calcule a qué distancia real ($d_{\text{real}}$) aparecerá el destello del faro tangencial sobre el horizonte en una noche de atmósfera estándar.

**Solución:**
El alcance fotométrico es $D_N = 20 \text{ millas}$. 
Ahora calculamos el límite geométrico interpuesto por el esferoide terrestre. La fórmula del alcance geográfico en millas náuticas, corregida por refracción atmosférica, es:
$$ d_{\text{geo}} = 2.08 \cdot \left( \sqrt{E} + \sqrt{e} \right) $$
Sustituyendo los valores de las elevaciones en metros:
$$ d_{\text{geo}} = 2.08 \cdot \left( \sqrt{81} + \sqrt{15} \right) $$
$$ d_{\text{geo}} = 2.08 \cdot (9 + 3.873) = 2.08 \cdot 12.873 \approx 26.77 \text{ millas náuticas} $$
El alcance de avistamiento real obedece al principio de restricción fundamental: la luz no puede ser vista más allá de lo que permite su potencia óptica, ni antes de sortear la curvatura de la Tierra.
$$ d_{\text{real}} = \min(D_N, d_{\text{geo}}) = \min(20, 26.77) = 20 \text{ millas} $$
El navegante avistará el faro a 20 millas, condicionado estrictamente por la debilidad de la candela luminosa (Alcance Nominal) y no por la obstrucción del horizonte de la Tierra.

## Referencias Bibliográficas y Jurisprudencia

*   **Bibliografía Básica:** IALA-AISM. (2014). *Navguide - Guía de la IALA sobre Ayudas a la Navegación*. International Association of Marine Aids to Navigation and Lighthouse Authorities.
*   **Convenios OMI:** Libro de Faros y Señales de Niebla del Instituto Hidrográfico de la Marina (IHM), y regulaciones estándar de la Organización Hidrográfica Internacional (OHI).
*   **Jurisprudencia:** *The "Norman Atlantic" (2014)* y colisiones afines cerca de enfilaciones. Decisiones de Cortes de Almirantazgo que analizan la responsabilidad del oficial de guardia por confundir la característica lumínica de faros principales con luminarias civiles de fondo (background lighting) en zonas densamente pobladas, un factor mitigable mediante el correcto cálculo de distancias trigonométricas y arcos de visibilidad.
