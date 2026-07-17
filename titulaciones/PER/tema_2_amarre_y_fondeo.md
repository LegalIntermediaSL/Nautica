# PER - Tema 2: Sistemas de Amarre, Fondeo y Dinámica del Anclaje

Dominar los conceptos de amarre es esencial. A nivel avanzado, el fondeo es una interacción compleja de catenarias, hidrodinámica y geología marina, requiriendo un conocimiento matemático riguroso de las fuerzas implicadas.

---

## 1. La Cabuyería, Materiales y Tensión de Rotura

La cabuyería moderna utiliza polímeros avanzados (Dyneema, Kevlar, Poliéster).

### Física de los Cabos
La carga de rotura (Breaking Load, $BL$) y la carga de trabajo segura (Safe Working Load, $SWL$) están definidas empíricamente. Generalmente:
$$ SWL = \frac{BL}{FS} $$
donde $FS$ es el factor de seguridad (habitualmente 5 o 6).
*   **Chicote:** Extremo del cabo.
*   **Firme:** Parte principal que soporta tensión axial.
*   **Seno:** Curva del cabo.

### Terminología Avanzada de Manejo
*   **Cobrar:** Recoger el cabo.
*   **Cazar:** Tensar el cabo. En veleros, esto incrementa la tensión de grátil.
*   **Lascar / Filar:** Aflojar bajo control, disipando energía cinética por fricción.
*   **Arriar:** Soltar por completo.
*   **Templar:** Tensar para igualar cargas (load sharing) sin sobrepasar el límite elástico.
*   **Adujar:** Recoger para evitar nudos topológicos no deseados.

## 2. Tipos de Amarras y Cinemática del Atracado

El barco es un cuerpo rígido sujeto a fuerzas y momentos respecto a su centro de rotación (pivote). Las amarras restringen grados de libertad.

1.  **Largo de Proa:** Restringe el movimiento (surge) hacia atrás.
2.  **Largo de Popa:** Restringe el movimiento hacia adelante.
3.  **Través de Proa / Través de Popa:** Restringen el movimiento lateral (sway).
4.  **Esprín (Spring) de Proa:** Evita el avance. Si se da motor avante con el esprín de proa amarrado, se genera un par de fuerzas (momento $M = F \times d$) que hace rotar la popa hacia afuera del muelle.
5.  **Esprín (Spring) de Popa:** Evita el retroceso. Útil para separar la proa del muelle al dar marcha atrás.

*Ejemplo Práctico:* Para desatracar con viento de proa (on-shore wind), se mantiene el esprín de proa, se da máquina avante con timón al muelle. La popa pivota contra el viento. Una vez la popa ha librado, se da máquina atrás y se suelta el esprín.

## 3. Dinámica del Fondeo y la Catenaria

Fondear (anchoring) es un problema clásico de estática de cables flexibles (catenaria). El objetivo es que la fuerza que llega al ancla sea puramente horizontal ($F_y = 0$).

### Matemáticas de la Catenaria
La forma que adopta una cadena pesada suspendida bajo su propio peso es una catenaria. La tensión horizontal ($T_H$) en el fondo y la longitud mínima de cadena apoyada en el fondo determinan el garreo. La ecuación de la curva es:
$$ y = a \cosh\left(\frac{x}{a}\right) $$
donde $a = \frac{T_H}{w}$, siendo $w$ el peso de la cadena por unidad de longitud en el agua.

### Tipos de Anclas Recreativas y Penetración del Lecho
*   **Danforth (De Uñas Articuladas):** Excelente en arena fina. Relación de agarre/peso (Holding Power) de hasta 10:1.
*   **Bruce / Trefoil:** Arado de una pieza. Flujo laminar del lecho sobre su geometría.
*   **CQR:** Arado articulado. Buena penetración en posidonia (aunque ecológicamente se debe evitar fondear sobre ella; múltiples directivas europeas lo prohíben estrictamente).
*   **Rezón:** Uso muy específico en roca, agarre mecánico directo (forma clamping).
*   **Almirantazgo:** Clásica, alto momento de inercia, muy difícil de estibar.

### Elementos del Sistema
*   **Molinete (Barboten):** Cabrestante diseñado según el paso y grosor de la cadena (ej. DIN 766, ISO 4565).
*   **Grillete de Unión y Quitavueltas (Swivel):** Soporta cargas extremas de torsión mecánica.

### Procedimiento y Cálculos Críticos
*   **Garrear (Dragging):** Falla el agarre por superar la resistencia al corte del suelo marino ($\tau = c + \sigma \tan \phi$).
*   **Longitud Recomendada (Scope):** 
    Para garantizar que la tracción en el ancla sea paralela al fondo (ángulo 0°), se calcula la longitud $L$ necesaria de cadena:
    $$ L \geq \sqrt{h(h + 2a)} $$
    donde $h$ es la profundidad total (sonda + altura de proa).
    Reglas prácticas:
    *   Arena, buen tiempo: $3 \times h$
    *   Temporal: $5 \times h$ a $7 \times h$.
*   **Borneo (Swing Circle):** Área barrida de radio $R \approx L$. Vital calcularlo con GPS para evitar colisiones con otros yates.
*   **Orinque (Trip Line):** Cabo atado a la cruz para invertir el vector de fuerza de extracción si el ancla se enroca.

## Ejemplos Prácticos

**Problema 1: Dinámica de la Catenaria de Fondeo bajo Tensión Máxima**
Una embarcación fondea a una profundidad $h = 10 \text{ m}$ (incluyendo la altura del escobén) utilizando una cadena cuyo peso sumergido es $w = 2.5 \text{ kg/m}$ (aproximadamente $24.5 \text{ N/m}$). Para evitar el garreo, se requiere que la fuerza ejercida en la caña del ancla sea estrictamente horizontal ($\theta = 0^\circ$). Durante un temporal, el viento y la corriente ejercen una tracción horizontal sobre la proa de $T_H = 4000 \text{ N}$.
Calcule la longitud mínima de cadena $L$ necesaria para asegurar que el ancla trabaje en condiciones óptimas sin componente vertical.

*Solución:*
1. Primero, determinamos el parámetro de la catenaria $a$, que representa la relación entre la tensión horizontal y el peso lineal sumergido de la cadena:
$$ a = \frac{T_H}{w} = \frac{4000 \text{ N}}{24.5 \text{ N/m}} \approx 163.26 \text{ m} $$
2. La longitud de cadena suspendida requerida para asegurar que la tangente geométrica al fondo sea cero se define por la ecuación geométrica de la catenaria:
$$ L = \sqrt{h(h + 2a)} $$
3. Sustituyendo los valores:
$$ L = \sqrt{10 \cdot (10 + 2 \cdot 163.26)} = \sqrt{10 \cdot (10 + 326.52)} = \sqrt{10 \cdot 336.52} = \sqrt{3365.2} $$
$$ L \approx 58 \text{ m} $$
En conclusión, el patrón deberá filar como mínimo 58 metros de cadena (casi 6 veces la sonda) para prevenir el garreo bajo esa fuerza aerodinámica.

## Referencias Bibliográficas y Jurisprudencia

*   **Bibliografía:** Taylor, D. W. (1910). *The Speed and Power of Ships*. (Manual clásico que fundamenta empíricamente los principios del esfuerzo tractor en amarras).
*   **Convenios OMI:** *Guidelines for the Preparation of the Towing and Mooring Arrangement Plan (IMO MSC.1/Circ.1620)* – Define la estandarización del SWL en accesorios de amarre.
*   **Jurisprudencia:** *The "Star Sea" [2001] UKHL 1* (House of Lords) – Caso fundamental que aborda la "seaworthiness" y la negligencia operativa en procedimientos de prevención a bordo, relacionado intrínsecamente con las fallas en los sistemas y accesorios de sujeción (aunque en este caso derivado de un incendio).
