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

## Recursos Audiovisuales (Videotutoriales de Apoyo)

*   📺 **Escuela Náutica Neptuno:** [Examen PER y PNB - NOMENCLATURA NÁUTICA - Tema 1](https://www.youtube.com/watch?v=FIjt7RyDYQg) (Excelente repaso visual de las partes del casco, estructura, equipo de fondeo, timón y dimensiones).

## Ejemplos Prácticos

**Problema 1: Cálculo de la Resistencia de Formación de Olas (Wave-Making Resistance)**
Un velero de diseño clásico posee una eslora en la línea de flotación de $L_{WL} = 10 \text{ m}$. Si el Número de Froude ($Fr$) se define matemáticamente como:
$$ Fr = \frac{v}{\sqrt{g \cdot L_{WL}}} $$
y se asume empíricamente que la resistencia por formación de olas diverge significativamente al alcanzar un Número de Froude de la "velocidad del casco" de $Fr \approx 0.4$, calcule la velocidad límite teórica del casco en nudos. Asuma $g = 9.81 \text{ m/s}^2$.

*Solución:*
1. Despejando la velocidad límite de la ecuación de Froude:
$$ v = Fr \cdot \sqrt{g \cdot L_{WL}} $$
2. Sustituyendo los valores conocidos:
$$ v = 0.4 \cdot \sqrt{9.81 \text{ m/s}^2 \cdot 10 \text{ m}} = 0.4 \cdot \sqrt{98.1} \text{ m/s} $$
$$ v \approx 0.4 \cdot 9.904 \text{ m/s} = 3.96 \text{ m/s} $$
3. Convirtiendo a nudos ($1 \text{ nudo} = 0.5144 \text{ m/s}$):
$$ V_{max} = \frac{3.96 \text{ m/s}}{0.5144 \text{ m/s/nudo}} \approx 7.70 \text{ nudos} $$
Esta fórmula subraya la barrera hidrodinámica ineludible para cascos de desplazamiento antes de entrar en régimen de planeo.

## Referencias Bibliográficas y Jurisprudencia

*   **Bibliografía:** Rawson, K. J., & Tupper, E. C. (2001). *Basic Ship Theory*. Butterworth-Heinemann.
*   **Bibliografía:** Marchaj, C. A. (2000). *Aero-Hydrodynamics of Sailing*. Tiller Publishing.
*   **Jurisprudencia:** *The "Eurasian Dream" [2002] 1 Lloyd's Rep 719* – Caso de la High Court of Justice (Admiralty Court) donde se estableció la inestabilidad inherente derivada de modificaciones estructurales en buques y la consecuente inhabilidad de gobierno por no documentar adecuadamente cambios en la geometría del casco.
