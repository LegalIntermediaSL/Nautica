# PER - Tema 9: Meteorología Básica y Costera (Nivel Universitario)

Para el patrón de embarcaciones de recreo, la meteorología es la barrera que separa un día idílico de una pesadilla. No hace falta tener nivel de ingeniero atmosférico, pero sí es vital saber interpretar los boletines locales, conocer la dinámica de los vientos costeros y prever la formación del oleaje antes de que sea demasiado tarde para volver a puerto. A nivel superior, la meteorología náutica se rige por la termodinámica atmosférica y las fuerzas de inercia del planeta Tierra.

---

## 1. Conceptos Básicos y Presión Atmosférica

El motor de la meteorología es la **Presión Atmosférica**, que es literalmente el peso de la enorme columna de aire que descansa sobre nuestros hombros y sobre la superficie del mar. Se mide usando un **barómetro** aneroide o electrónico, y su unidad oficial de medida náutica es el **milibar (mb)**, equivalente exacto al hectopascal (hPa).

*   La presión media considerada "neutra" a nivel del mar es de **1013 milibares**.
    *   Si la presión es **mayor** de 1013 mb $\rightarrow$ **Anticiclón** (Alta Presión - A/H). El aire pesado cae hacia el suelo aplastando las nubes. Significa tiempo estable, cielos limpios y vientos flojos.
    *   Si la presión es **menor** de 1013 mb $\rightarrow$ **Borrasca** (Baja Presión - B/L). El aire ligero sube rápidamente llevándose la humedad, que se enfría arriba formando nubes densas y lluvias. Significa mal tiempo.

### 1.1 Física Isobárica y Termodinámica de Masas de Aire

El comportamiento del aire no es puramente mecánico; responde a la ecuación de estado de los gases ideales:
$$ P \cdot V = n \cdot R \cdot T $$
Donde la presión ($P$) y la temperatura ($T$) dictan la densidad de la masa de aire. Cuando una masa de aire asciende (borrasca), experimenta una expansión adiabática (sin intercambio de calor con el entorno), lo que provoca su enfriamiento.

**Gradiente Termo-Adiabático (Adiabatic Lapse Rates):**
El aire ascendente se enfría a un ritmo conocido matemáticamente como el Gradiente Adiabático Seco (GAS), de aproximadamente $9.8^\circ\text{C}$ por cada 1000 metros. Sin embargo, si alcanza el punto de rocío y el vapor de agua se condensa, se libera calor latente de vaporización. A partir de este nivel de condensación (la base de las nubes), el aire se enfría más lentamente, según el Gradiente Adiabático Saturado, en torno a $5^\circ\text{C}$ a $6^\circ\text{C}$ por cada 1000 metros.

### 1.2 Isobaras (El Mapa del Tiempo)
Son las curvas cerradas que dibujan los meteorólogos en los mapas uniendo los puntos geográficos que tienen exactamente la misma presión atmosférica (suelen dibujarse de 4 en 4 milibares).
*   **Gradiente de Presión:** Al igual que las curvas de nivel en un mapa de montaña indican la pendiente, las isobaras indican el "desnivel" del aire. El vector de fuerza de gradiente de presión ($\vec{F}_p$) empuja perpendicularmente a las isobaras, desde altas a bajas presiones:
$$ \vec{F}_p = -\frac{1}{\rho} \nabla P $$
Donde $\rho$ es la densidad del aire y $\nabla P$ es el gradiente de presión. Cuanto **más juntas** están las isobaras en el mapa, mayor es la fuerza impulsora.

## 2. Dinámica del Viento y el Efecto Coriolis

El viento es el desplazamiento físico de las masas de aire intentando rellenar los vacíos. El aire **siempre viaja desde las zonas de Alta Presión hacia las de Baja Presión**.

### 2.1 Fuerza de Coriolis (Inercia Planetaria)
A nivel de la costa, la rotación de la Tierra genera una aceleración aparente sobre el fluido en movimiento conocida como el **Efecto Coriolis**. Esta fuerza desvía los vientos hacia la **derecha en el Hemisferio Norte** y hacia la izquierda en el Hemisferio Sur.

La aceleración de Coriolis ($\vec{a}_c$) se define matemáticamente mediante el producto vectorial de la velocidad angular de la Tierra ($\vec{\Omega}$) y el vector velocidad del viento ($\vec{v}$):
$$ \vec{a}_c = -2 \vec{\Omega} \times \vec{v} $$
Su magnitud escalar en la superficie horizontal depende de la latitud ($\phi$):
$$ f_c = 2 \Omega \cdot v \cdot \sin(\phi) $$
Donde $\Omega \approx 7.292 \times 10^{-5} \text{ rad/s}$.
Esto significa que en el Ecuador el efecto Coriolis es nulo, pero a latitudes medias, el viento no viaja perpendicular a las isobaras, sino casi paralelo a ellas (Viento Geostrófico).

### 2.2 Vientos Locales (El Régimen de Brisas)
Debido a la física térmica, la arena y las rocas de la costa se calientan como una sartén durante el día, pero se congelan rápido de noche. El agua del mar, en cambio, es un regulador térmico masivo con una altísima capacidad calorífica específica ($C_p \approx 4184 \text{ J/(kg}\cdot\text{K)}$). Tarda meses en calentarse y meses en enfriarse, por lo que su temperatura se mantiene constante día y noche.

*   **Virazón (Brisa de Mar) - El Viento de Día:**
    *   A media mañana, el Sol calienta la costa terrestre. El aire sobre la playa se calienta, disminuye su densidad ($\rho$) y sube por convección térmica, dejando un vacío (baja presión térmica).
    *   El aire fresco que reposa sobre el mar (alta presión) corre hacia la costa para rellenar ese hueco.
    *   **Dirección:** Sopla **desde el mar hacia la tierra**.
    *   *Ciclo:* Empieza típicamente a las 11:00h, alcanza su pico máximo de intensidad (puede llegar a Fuerza 4) a media tarde y muere en absoluta calma al ponerse el Sol.
*   **Terral (Brisa de Tierra) - El Viento de Noche:**
    *   De madrugada, la tierra se ha enfriado muchísimo. El mar ahora está más caliente que la tierra por su inercia térmica.
    *   El aire sobre el mar asciende.
    *   El aire helado de las montañas costeras desciende (viento catabático en miniatura) y corre hacia el mar para rellenar el vacío.
    *   **Dirección:** Sopla **desde la tierra hacia el mar**.
    *   *Ciclo:* Nace a media noche y dura hasta el amanecer. Suele ser más flojo que el Virazón y deja el mar muy plano cerca de la costa.

## 3. Estado de la Mar (Escala Douglas y Fetch)

El viento transfiere su energía cinética al mar creando olas por fricción y presión asimétrica sobre la superficie. La **Escala Douglas** clasifica el estado de la mar basándose exclusivamente en la **altura** de esas olas (de 0 a 9). En el examen del PER debes dominar los niveles inferiores:

*   **0: Calma:** ($0 \text{ metros}$). Mar como un espejo de cristal.
*   **1: Mar Rizada:** ($0 \text{ a } 0.1 \text{ m}$). Pequeñas arrugas como escamas, sin formar espuma blanca.
*   **2: Marejadilla:** ($0.1 \text{ a } 0.5 \text{ m}$). Olas pequeñas pero ya con forma.
*   **3: Marejada:** ($0.5 \text{ a } 1.25 \text{ m}$). Aparecen los temidos "borreguillos" (la cresta de la ola rompe formando espuma blanca extensa).
*   **4: Fuerte Marejada:** ($1.25 \text{ a } 2.5 \text{ m}$). Olas que ya tapan el horizonte a los barcos pequeños.

> [!WARNING]
> A partir de Marejada/Fuerte Marejada (Estado 3-4), la navegación de recreo para esloras menores de 8 metros se vuelve muy incómoda, propensa a mareos severos de la tripulación y potencialmente insegura.

### 3.1 Fetch y Desarrollo del Oleaje
La altura máxima significativa de la ola ($H_s$) generada por un viento sostenido depende de tres factores matemáticos: la velocidad del viento ($U$), la duración del mismo ($t$), y el **Fetch** ($F$), que es la distancia rectilínea sobre el agua en la que el viento sopla sin encontrar obstáculos terrestres. Las relaciones empíricas de Sverdrup-Munk-Bretschneider (SMB) nos dictan que la energía transferida al mar escala rápidamente. Cuando el fetch y la duración son suficientemente largos, se alcanza un mar "completamente desarrollado" (Fully Developed Sea), donde la energía disipada por la rotura de las olas iguala a la energía inyectada por el viento.

## 4. Previsión Empírica (Leyendo el Entorno)

Un buen patrón no solo mira la pantalla del móvil, también lee la naturaleza aplicando leyes termodinámicas visuales:
*   **El Barómetro avisa:** Una bajada de presión rápida ($\frac{dP}{dt} < -2 \text{ mb/3h}$) indica la llegada inminente de un frente profundo o ciclogénesis explosiva. **Es el momento exacto de buscar puerto refugio**.
*   **El Cielo (Nubes altas):** La invasión en el cielo azul de "colas de caballo" (nubes tipo Cirros de cristales de hielo muy altas, formadas por la deposición directa del vapor) que poco a poco van cubriendo el cielo y bajando de altura, son la vanguardia clásica de un Frente Cálido. El aire caliente trepa lentamente sobre una cuña de aire frío, enfriándose adiabáticamente y trayendo lluvias persistentes en las siguientes 24 horas.
*   **Halo Solar/Lunar:** Un anillo de arcoíris alrededor del Sol o de la Luna indica refracción de la luz a través de cristales de hielo hexagonales en cirrostratos a 6000-8000 metros de altitud; precede casi infaliblemente a un frente activo.
*   **Líneas de Turbonada y Frentes Fríos:** Nubes oscuras de desarrollo vertical tremendo (Cumulonimbus) que avanzan como una muralla maciza, indicando que una masa de aire polar densa está arando la superficie como una cuña, obligando al aire caliente a ascender de forma explosiva, desatando el caos atmosférico y rachas de viento brutales.
