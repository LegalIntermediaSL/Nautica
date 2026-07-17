# PER - Tema 1: Nomenclatura Náutica y Arquitectura Naval Avanzada

Este tema es el diccionario fundamental y el cimiento de la arquitectura naval. Para aprobar el examen del PER (y del PNB) debes memorizar con total precisión las partes de la embarcación. A nivel universitario, esto implica comprender la hidrodinámica, las tensiones estructurales y el contexto histórico de la construcción naval.

---

## 1. Dimensiones Principales y Geometría del Buque

Las dimensiones definen no solo el tamaño legal, sino el comportamiento hidrodinámico y la resistencia al avance.

*   **Eslora (Length):** Es la longitud del barco. Se mide de proa a popa.
    *   *Eslora Máxima o Total ($L_{OA}$):* Medida desde los puntos más extremos.
    *   *Eslora de Flotación ($L_{WL}$):* La longitud de la obra viva. Determina la velocidad máxima teórica en cascos de desplazamiento mediante el Número de Froude. La velocidad del casco (en nudos) se aproxima con la fórmula matemática:
        $$ V_{max} \approx 1.34 \times \sqrt{L_{WL}} $$
        donde $L_{WL}$ está en pies.
    *   *Eslora entre Perpendiculares ($L_{BP}$):* Usada en cálculos de arquitectura naval, medida entre la perpendicular de proa y la de popa.
*   **Manga (Beam):** Es la anchura del barco. Define la estabilidad transversal inicial.
*   **Puntal (Depth):** Es la altura interior del casco, desde la quilla hasta la cubierta principal.
*   **Calado (Draft, $T$):** Profundidad sumergida. Crítico para evitar encallamientos y calcular el desplazamiento ($\Delta = L \times B \times T \times C_B \times \rho$).
*   **Francobordo (Freeboard):** Distancia vertical desde la línea de flotación hasta la cubierta principal. Un francobordo alto proporciona reserva de flotabilidad.
    *   *Fórmula fundamental:* $$ \text{Puntal} = \text{Calado} + \text{Francobordo} $$
*   **Asiento (Trim):** Diferencia entre el calado de popa ($T_A$) y el de proa ($T_F$).
    $$ \text{Asiento} = T_A - T_F $$
    Si $T_A > T_F$, tiene asiento apopante (positivo).

### Contexto Histórico
Históricamente, la evolución de la eslora y la manga estuvo dictada por los materiales. Los galeones de madera del siglo XVI tenían proporciones de eslora/manga de 3:1 para garantizar la integridad estructural bajo el embate de las olas, mientras que los modernos destructores alcanzan 10:1 gracias a aleaciones de acero y titanio.

## 2. Partes del Casco y Estructura: Tensiones y Resistencia

El casco es la viga principal que soporta cargas dinámicas extremas.

### Divisiones Visuales del Casco
*   **Proa:** Parte delantera. Diseñada con ángulos de ataque finos para reducir la resistencia por formación de olas.
*   **Popa:** Parte trasera. Su diseño de salida de aguas (ej. espejo) minimiza el desprendimiento de vórtices.
*   **Babor / Estribor:** Izquierda / Derecha mirando a proa. (Babor luz roja, Estribor luz verde).
*   **Línea de Crujía:** Eje de simetría longitudinal.
*   **Línea de Flotación:** Separa obra viva de obra muerta.
*   **Obra Viva (Carena):** Superficie mojada. Aquí la fricción viscosa es crítica y se modela según el Número de Reynolds ($Re = \frac{v L}{\nu}$).
*   **Obra Muerta:** Expuesta al viento (windage o resistencia aerodinámica), calculada como $R_a = \frac{1}{2} \rho_{aire} V_{rel}^2 C_d A$.

### Sectores de Orientación
*   **Amura:** Proa al través.
*   **Través:** Punto medio perpendicular a crujía.
*   **Aleta:** Través a popa.

### Estructura Interna y Física de Materiales
El barco actúa como una viga sometida a esfuerzos flectores sobre el oleaje:
*   **Arrufo (Sagging):** Cuando la proa y popa están sobre crestas de olas y el centro en un seno. La cubierta sufre compresión y la quilla tracción.
*   **Quebranto (Hogging):** El centro está en la cresta de la ola. La cubierta sufre tracción y la quilla compresión.
*   **Quilla:** La "columna vertebral". Soporta el momento flector máximo.
*   **Roda y Codaste:** Continuaciones de la quilla.
*   **Cuadernas:** Costillas transversales. Absorben esfuerzos cortantes.
*   **Baos:** Vigas que soportan la cubierta y evitan el colapso lateral (pandeo).
*   **Esloras y Varengas:** Refuerzos longitudinales.
*   **Sentina:** Parte más baja del casco donde convergen fluidos.
*   **Imbornales:** Drenaje.

## 3. Accesorios, Elementos de Cubierta y Apéndices Hidrodinámicos

*   **Timón:** Superficie de control. La fuerza de sustentación (lift) del timón sigue la teoría de perfiles alares:
    $$ L = \frac{1}{2} \rho v^2 A C_L $$
    donde el ángulo de ataque entra en pérdida (stall) si supera los 35°.
*   **Bañera:** Zona abierta para maniobra.
*   **Pasamanos / Candelabros:** Seguridad de tripulación.
*   **Cornamusas y Bitas:** Puntos de amarre, diseñados para resistir cargas de rotura altas.
*   **Guíacabos:** Reducen la concentración de esfuerzos por rozamiento.
*   **Escotillas y Portillos:** Cierres estancos, críticos para el cálculo de estabilidad en grandes ángulos (curva GZ).
*   **Púlpito:** Barandillas en proa/popa.

## 4. Conceptos de Movimiento en Fluidos (Rolar vs. Caer)

En la dinámica de fluidos marítima, la cinemática es esencial:

*   **Rolar:** Cambio de dirección del viento real.
*   **Caer:** Modificación del rumbo del barco mediante un par de fuerzas generado por el timón.
*   **Abatir:** Desplazamiento lateral por fuerza del viento ($F_w$). En veleros, se contrarresta con la sustentación hidrodinámica de la quilla.
*   **Derivar:** Desplazamiento vectorial absoluto provocado por la corriente ($V_c$).
El vector de velocidad absoluta del barco ($V_{SOG}$) es la suma del vector de velocidad sobre el agua ($V_{STW}$), el vector viento (abatimiento) y el vector corriente.
