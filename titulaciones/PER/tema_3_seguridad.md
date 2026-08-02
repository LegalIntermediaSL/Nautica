# PER - Tema 3: Seguridad Marítima y Estabilidad Naval (Teoría Avanzada)

La seguridad en la mar es una ciencia interdisciplinaria que combina física termodinámica, dinámica de cuerpos flotantes y protocolos estrictos de derecho marítimo internacional (SOLAS).

---

## 1. Física y Matemáticas de la Estabilidad

Para que un buque recupere su posición adrizada tras una escora, requiere un momento adrizante positivo. 

### Los 6 Grados de Libertad (6-DOF)
Un barco navega en un fluido dinámico sujeto a oscilaciones no lineales:
*   **Rotaciones:**
    *   *Balanceo (Roll, $\phi$):* Movimiento transversal. Peligro de vuelco.
    *   *Cabeceo (Pitch, $\theta$):* Movimiento longitudinal.
    *   *Guiñada (Yaw, $\psi$):* Rotación sobre el eje vertical Z.
*   **Traslaciones:**
    *   *Avance/Retroceso (Surge).*
    *   *Abatimiento lateral (Sway).*
    *   *Ascenso/Descenso vertical (Heave).*

### Metacentro, Centro de Gravedad y Curva GZ
*   **Centro de Gravedad (G):** Punto donde se concentra la masa total ($W$).
*   **Centro de Carena (B):** Centroide geométrico del volumen sumergido, origen de la fuerza de empuje (Principio de Arquímedes).
*   **Metacentro (M):** Intersección de las líneas de empuje al escorar ángulos pequeños.
La **Altura Metacéntrica ($GM$)** es crítica:

$$
GM = KB + BM - KG
$$

donde $BM = \frac{I}{V}$ (Inercia de la superficie de flotación entre Volumen sumergido).
*   Si $GM > 0$: Equilibrio estable.
*   El **Brazo Adrizante (GZ)** dicta la fuerza de restitución:
    

$$
GZ = GM \cdot \sin(\phi)
$$

 (para pequeños ángulos).
    *Nunca* elevar pesos (ej. tripulación en el techo) ya que incrementa $KG$, reduce $GM$ peligrosamente y lleva al barco a la zozobra.

## 2. Equipamiento de Salvamento (SOLAS y Normativa Nacional - Zona 4, 12 Millas)

El equipamiento está regulado por la DGMM y el Convenio SOLAS (Safety of Life at Sea). El incumplimiento acarrea la inmovilización del buque.

### 2.1 Equipos de Flotabilidad
*   **Chalecos Salvavidas:** Uno por persona + 10% adicional. Mínimo **150 Newtons** de flotabilidad para Zona 4 (Normativa ISO 12402-3). Deben asegurar que la boca quede a $12$ cm del agua en $5$ segundos para un tripulante inconsciente.
*   **Aro Salvavidas:** Obligatorio 1 unidad tipo herradura o circular con luz Sirio (activada por contacto con agua salada) y rabiza flotante de $27.5$ metros. Zafado rápido en popa.

### 2.2 Material Pirotécnico (Química y Señalización)
Basados en nitrato de estroncio (luz roja). Poseer caducados es infracción grave en la Ley de Puertos y de la Marina Mercante (RD Legislativo 2/2011).
*   **3 Bengalas de mano:** 15.000 candelas. Duración $> 1$ min. Alcance visual de $3-5$ millas.
*   **3 Cohetes con paracaídas:** Ascienden a $\approx 300$ metros y descienden a $\leq 5$ m/s, iluminando a 30.000 candelas por $\geq 40$ s. Alcance visual más de 25 millas en la noche.
*   **1 Bote fumígeno flotante:** Humo naranja denso por $\geq 3$ minutos. Exclusivo diurno (helirrescates).

### 2.3 Medios Contraincendios (Termodinámica del Fuego)
*   **Extintores:** Tipo 21B (polvo químico seco). Cortan la reacción en cadena del triángulo del fuego (combustible, comburente, energía de activación). Barcos $> 10$m requieren mínimo 2 extintores.

## 3. Procedimientos de Riesgo y Cinemática de Rescate (MOB)

*   **Línea de Vida y Arnés:** Fuerza de rotura de al menos $2000$ kg. El arnés (tether) debe usarse de noche o con mar gruesa.

### Maniobra de Hombre al Agua (Man Overboard - MOB)
La supervivencia en aguas $< 15^\circ C$ (choque térmico) es de minutos.
1.  **Gritar y Asignar Vigía:** No perder visual (efecto de atenuación por olas).
2.  **Lanzamiento:** Aro salvavidas inmediato.
3.  **Botón MOB:** Fija el datum radiométrico en el plotter GPS.
4.  **Apartar la hélice:** Timón a la **misma banda** de la caída para apartar las palas.
5.  **Aproximación Táctica:**
    *   *Maniobra de Boutakov (Williamson Turn):* Caer $60^\circ$ a la banda de caída, luego todo el timón a la banda opuesta hasta el rumbo recíproco ($R_1 = R_0 + 180^\circ$). Lleva el buque matemáticamente a la estela original.
6.  **Recogida:** Aproximación por **Sotavento** para que el buque (gran abatimiento aerodinámico) derive hacia la víctima de forma pasiva, sin engranar la hélice.

## 4. Navegación Meteorológica Extrema

La hidrodinámica del temporal se aborda con dos tácticas primarias:
*   **Capear (Heave-to):** Tomar viento/mar por la amura ($45^\circ$). El barco entra en cuasi-equilibrio de fuerzas; deriva lentamente formando una gran mancha de turbulencia a barlovento (slick) que rompe la cresta de las olas entrantes.
*   **Correr el temporal (Running):** Navegar a favor de olas. Riesgo extremo de *guiñada de ronza* (broaching): Si la ola viaja a la velocidad del barco ($V \approx \sqrt{g \lambda / 2\pi}$), la popa pierde sustentación del timón, el barco se atraviesa al mar y zozobra instantáneamente. Solución: usar anclas de capa o amarras por popa (drogues) para inducir drag aerohidrodinámico y frenar el empuje.

## Ejemplos Prácticos

**Problema 1: Cálculo del Momento Adrizante y Altura Metacéntrica ($GM$)**
Un velero de desplazamiento $\Delta = 5000 \text{ kg}$ (con centro de gravedad a una altura $KG = 1.2 \text{ m}$ respecto a la quilla base) experimenta un corrimiento de carga. Durante una prueba de inclinación, un peso $p = 200 \text{ kg}$ se desplaza transversalmente una distancia $d = 2 \text{ m}$. Esto genera un ángulo de escora permanente $\phi = 5^\circ$.
Calcule la altura metacéntrica inicial ($GM$) asumiendo pequeños ángulos.

*Solución:*
1. El momento escorante provocado por el desplazamiento transversal del peso es:

$$
M_{escorante} = p \cdot g \cdot d \cdot \cos(\phi) \approx p \cdot g \cdot d \quad \text{(para ángulos pequeños, } \cos(5^\circ) \approx 1\text{)}
$$

Consideraremos el momento en términos de masa-distancia por simplicidad:

$$
M_{escorante} \approx 200 \text{ kg} \cdot 2 \text{ m} = 400 \text{ kg}\cdot\text{m}
$$

2. En la condición de equilibrio, el momento escorante es igual al momento adrizante del buque ($M_{adrizante}$):

$$
M_{adrizante} = \Delta \cdot GM \cdot \tan(\phi)
$$

Igualando ambos momentos (omitiendo $g$ en ambos lados):

$$
p \cdot d = \Delta \cdot GM \cdot \tan(\phi)
$$

3. Despejando $GM$:

$$
GM = \frac{p \cdot d}{\Delta \cdot \tan(\phi)}
$$

4. Sustituyendo los valores conocidos:

$$
GM = \frac{200 \cdot 2}{5000 \cdot \tan(5^\circ)} = \frac{400}{5000 \cdot 0.0875} = \frac{400}{437.5}
$$

$$
GM \approx 0.91 \text{ m}
$$

El resultado ($0.91 \text{ m} > 0$) indica que el barco goza de una estabilidad inicial positiva y satisfactoria para la navegación costera.

## Referencias Bibliográficas y Jurisprudencia

*   **Convenios OMI:** *Convenio Internacional para la Seguridad de la Vida Humana en el Mar (SOLAS)* – Capítulo II-1: Construcción - Estructura, compartimentado y estabilidad; y Capítulo III: Dispositivos y medios de salvamento.
*   **Bibliografía:** Derrett, D. R. (1999). *Ship Stability for Masters and Mates*. Butterworth-Heinemann.
*   **Jurisprudencia:** *The "Toledo" [1995] 1 Lloyd's Rep 40* – Caso de Admiralty en el que se dictaminó sobre la negligencia en la estiba y el incumplimiento de los criterios mínimos de estabilidad intacta (cálculos de la curva GZ), resultando en el hundimiento y las respectivas responsabilidades civiles de la armadora.
