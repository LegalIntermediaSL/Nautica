# PER - Tema 11: La Carta Náutica y Publicaciones (Resolución Analítica)

El Tema 11 es la "prueba de fuego" y el terror del PER. Es una parte 100% práctica de cartografía que se realiza obligatoriamente sobre la Carta de enseñanza del **Estrecho de Gibraltar (Carta 105)**. Dominar este tema significa entender matemáticamente cómo trasladar el mundo físico real a un trozo de papel plano.

Debes llevar al examen material de delineante: regla larga, escuadra y cartabón grandes (o en su defecto un transportador de ángulos cuadrado náutico bretón), compás de dibujo (con punta de grafito duro), compás de puntas secas (para medir), y calculadora no programable. **Si fallas más de 2 problemas de los 4 de este bloque, suspendes todo el examen del PER automáticamente**, incluso si has sacado un 10 en toda la teoría.

---

## 1. La Proyección Mercator y la Deformación del Mundo
La carta náutica no es un mapa cualquiera, es una proyección cartográfica cilíndrica inventada por **Gerardus Mercator** en 1569. Su inmenso valor radica en que **mantiene los ángulos reales** (proyección conforme). Una línea recta trazada en una carta Mercator es un rumbo constante (Loxodrómica), lo que permite gobernar el barco con la brújula sin tener que ir virando.

Sin embargo, tiene un gran defecto: deforma enormemente las distancias a medida que te alejas del Ecuador. Por eso Groenlandia parece tan grande como África. En la navegación práctica, esto significa que **la escala de la carta no es constante**.

### 1.1 Coordenadas y el Uso Exclusivo del Compás

Cualquier hito en la carta náutica (un faro como los vistos en [Tema 13: Faros de España](./tema_13_faros_espana.md), un naufragio o tu barco) se clava geométricamente cruzando dos líneas rectas:
*   **Latitud ($l$):** Nos indica la altura vertical. Se lee única y exclusivamente en las escalas métricas verticales (situadas a la izquierda y derecha del papel). En el Estrecho de Gibraltar siempre estamos por encima del ecuador, por lo que se expresa en Grados y Minutos Norte (ej. $36^\circ 15,2' N$).
*   **Longitud ($L$):** Nos indica el desplazamiento horizontal. Se lee única y exclusivamente en las escalas horizontales (situadas arriba y abajo del papel). En el Estrecho siempre estamos a la izquierda de Greenwich, por lo que se expresa en Grados y Minutos Oeste (ej. $005^\circ 42,6' W$). *(Nota: W es West en inglés, normativa internacional).*

---



> [!CAUTION]
> **El Peligro de Medir Distancias:** Las distancias en la carta náutica (Millas Náuticas) se miden con el compás de puntas secas **ÚNICAMENTE en las escalas de Latitud (los márgenes verticales de los lados)**, abriendo el compás justo a la altura del meridiano donde estamos trabajando (porque la proyección Mercator deforma el mapa al ir hacia los polos). **Jamas uses la escala de longitud (arriba/abajo) para medir una distancia.** 
> *Equivalencia absoluta: 1 Minuto de Latitud en el lateral = 1 Milla Náutica = 1.852 Metros.*

## 2. Los Nortes y la Ecuación del Rumbo (Repaso Práctico)

En la carta náutica impresa de papel todo está orientado matemáticamente al **Norte Verdadero (Geográfico)**. Si unes dos puntos con la regla, estás dibujando un Rumbo Verdadero ($R_v$). Sin embargo, tu timonel en el barco lleva un compás magnético que sufre errores, por lo que gobierna según un **Norte de Aguja**.

**La Ecuación Maestra del PER:**
$$ R_v = R_a + C_t $$

### 2.1 Desglose de la Corrección Total ($C_t$)
Es la suma algebraica obligatoria de dos errores que te dan los enunciados:
$$ C_t = d_m + \Delta $$

*   **Declinación Magnética ($dm$):** Es culpa del planeta. La extraes leyendo la rosa de los vientos morada impresa en la carta para un año determinado, y sumando mentalmente la variación anual. 
    *   *(Ej de examen: "dm en 2005 = $2^\circ 50' W$, decresciendo anualmente $7'$". El examen es en 2024 (19 años). $19 \times 7 = 133' = 2^\circ 13'$. Como decrece, se lo restamos al original: $2^\circ 50' - 2^\circ 13' = 0^\circ 37' W$. Al ser W (Oeste) el signo final para la calculadora es NEGATIVO).*
*   **Desvío ($\Delta$):** Es culpa de los hierros de tu barco. Te lo dará directamente el enunciado (Ej: *$\Delta = +2^\circ$*).
*   **OJO a las Demoras:** Las demoras (marcar un faro con el compás) sufren EXACTAMENTE el mismo error que el rumbo, porque se leen en el mismo compás de tu barco. Por tanto: $D_v = D_a + C_t$.

## 3. Tipología de los 4 Problemas de Examen (Resolución Paso a Paso)

El examen constará de 4 problemas prácticos que rotan sobre estos cinco escenarios matemáticos:

### Escenario A: Cálculo Directo de Rumbo y Hora de Llegada (ETA)
*El enunciado te da un punto de salida (ej. Faro de Tarifa) y un punto de destino (ej. Faro de Punta Almina), te da el desvío, la velocidad y la hora a la que zarpas.*
1. Unes Tarifa y Punta Almina con la regla en el papel.
2. Trasladas esa recta paralela con la escuadra y cartabón hasta el centro de la Rosa de los Vientos de la carta. Lees el ángulo exacto al que apunta la línea. **¡PUM! Ya tienes el Rumbo Verdadero ($R_v$).**
3. Mides la longitud de esa recta con el compás y te lo llevas a la escala lateral de Latitud. Cuentas los minutos. **¡PUM! Ya tienes la Distancia ($D$) en millas.**
4. Con la fórmula $R_a = R_v - C_t$ calculas el Rumbo de Aguja que debes darle al timonel.
5. Con la fórmula cinemática $Tiempo = \frac{Distancia}{Velocidad}$ sacas las horas de travesía. Se las sumas a la hora de salida y sacas tu Hora Estimada de Llegada (ETA).

### Escenario B: Situación por Cruce de Dos Demoras
*El enunciado te dice: "A las 12:00 observamos el faro de Tarifa con una Demora de Aguja de 030º y el faro de Punta Cires con una Demora de Aguja de 120º. $C_t = -2^\circ$."*
1. Coges la $D_a$ de Tarifa (030) y le sumas la $C_t$ (-2) $\rightarrow D_v = 028^\circ$.
2. Te vas al compás de la carta, marcas 028º, y con la regla y escuadra arrastras esa línea recta hasta que **pase exactamente por encima del faro de Tarifa impreso en el papel**, trazando una línea infinita hacia el mar (la inversa de la demora).
3. Haces el mismo cálculo matemático para Punta Cires ($D_v = 118^\circ$) y trazas su línea infinita inversa desde el faro.
4. El cruce (la X perfecta) que hacen ambas líneas en medio del mar es tu posición milimétrica. Trazas las coordenadas en los laterales y marcas la casilla en el examen.

### Escenario C: Situación por Demora y Distancia Radar
*El enunciado te dice: "Vemos el faro de Trafalgar con Demora Verdadera de 045º y en el radar vemos la costa a 3 millas".*
1. Trazas la línea infinita de los 045º desde Trafalgar hacia el mar.
2. Abres el compás seco exactamente 3 minutos (3 millas) en la escala de latitudes lateral.
3. Pinchas la púa del compás en Trafalgar y cortas (trazas un pequeño arco de circunferencia) sobre la línea de demora que dibujaste antes. La intersección es tu barco.

### Escenario D: Situación por Loxodrómica de Estima (Rumbo y Distancia)
*El enunciado te dice: "A las 10:00 estamos en el Faro X. Ponemos Rumbo Verdadero 180º y a 5 nudos de velocidad. Damos nuestra situación a las 12:00".*
1. Desde el faro X, trazas una línea recta brutal hacia el Sur absoluto ($180^\circ$).
2. Sabes que has viajado 2 horas a 5 millas/hora. Distancia = 10 millas.
3. Abres el compás 10 millas en la escala vertical lateral.
4. Pinchas en el Faro X, cortas tu recta del sur. Ahí está tu situación por estima. *(Ver matemáticas analíticas de esto en [PY Tema 4: Navegación por Carta](../PY/tema_4_navegacion_carta.md)).*

---

## 4. Publicaciones Náuticas y Cartografía Electrónica (ECDIS)

Más allá de la carta de papel 105, la navegación moderna requiere consultar publicaciones oficiales.

### 4.1. Libro de Faros y Señales de Niebla
Editado por el Instituto Hidrográfico de la Marina (IHM), detalla absolutamente todas las balizas visuales y acústicas de la costa. Si ves una luz en la noche, consultas este libro para identificarla. (Ver Anexo [Los Faros de España](./tema_13_faros_espana.md) y [Tema 5: Balizamiento](./tema_5_balizamiento.md)).

### 4.2. El Manual INT-1 (Símbolos y Abreviaturas)
Es la "piedra Rosetta" de las cartas náuticas. Un pequeño libro oficial que estandariza internacionalmente cómo se dibujan los peligros:
*   Una cruz (`+`) rodeada de puntos significa una roca que siempre está bajo el agua.
*   Un asterisco (`*`) significa una roca que vela (asoma) durante la bajamar.
*   El fondo del mar se describe con letras: `S` (Sand/Arena), `M` (Mud/Fango), `R` (Rock/Roca), crítico para elegir zona de fondeo (Ver [Tema 2: Maniobras](./tema_2_amarre_fondeo.md)).

### 4.3. Cartografía Electrónica (ECDIS y Plotters)
Los buques modernos operan con un **ECDIS (Electronic Chart Display and Information System)**, mientras que las embarcaciones de recreo usan "Plotters" comerciales (Garmin, Raymarine).
Existen dos tipos fundamentales de cartas electrónicas:
1.  **Cartas Raster (RNC):** Son literalmente escaneos digitales como "fotos" de las cartas de papel. Al hacer zoom, los píxeles engordan y la letra se vuelve borrosa. Ya no se usan.
2.  **Cartas Vectoriales (ENC):** Son bases de datos dinámicas. Al hacer zoom, el ordenador dibuja las líneas de nuevo, revelando más información. Si programas el calado de tu barco a 2 metros, el ECDIS te pintará en rojo todas las zonas que tengan menos de esa profundidad.
