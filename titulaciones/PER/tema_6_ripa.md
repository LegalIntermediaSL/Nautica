# Tema 6: Reglamento Internacional para Prevenir Abordajes (RIPA) - Tratado Avanzado de Jurisprudencia y Cinemática

El RIPA (COLREGs 1972) es el marco normativo internacional inamovible dictado por la OMI (Organización Marítima Internacional). En los exámenes náuticos, es la parte más crítica y **tiene carácter eliminatorio**. En el PER, de las 10 preguntas de RIPA, un máximo de 5 fallos supone el suspenso automático e irrevocable. 
A nivel jurídico y penal, el RIPA no es un mero "reglamento de tráfico", sino un tratado internacional vinculante cuya violación se enmarca en la jurisdicción penal y civil del Almirantazgo (Derecho Marítimo Internacional), con casos que se remontan al *Boleslaw Chrobry (1974)* y *The Volvox Hollandia (1988)*.

---

## Parte A: Generalidades y Jurisprudencia (Reglas 1 a 3)

### Regla 1: Ámbito de Aplicación
Se aplica a todos los buques en alta mar y aguas navegables conectadas. No exime del cumplimiento de reglas locales, pero prevalece en tribunales internacionales en caso de controversia sobre prioridades generales.

### Regla 2: Responsabilidad y el "Buen Sentido Marinero"
Conocida en derecho marítimo como la *Regla de la Negligencia* o *Agony of the Moment*. "Ninguna disposición eximirá a un buque de las consecuencias de cualquier negligencia".
**Jurisprudencia:** Si tienes preferencia de paso (Buque que sigue rumbo), y el buque que debe ceder no actúa, y tú observas pasivamente cómo ocurre la colisión, **eres corresponsable civil y penalmente**. La inacción ("stand-on inertia") no te protege. Debes realizar maniobras evasivas *in extremis* (Regla 17b).

### Regla 3: Definiciones Legales Excluyentes
*   **Buque de propulsión mecánica:** Cualquier buque movido por máquina. Un velero con el motor encendido *es un barco a motor* legalmente.
*   **Buque en navegación:** Ni fondeado, ni amarrado, ni varado. ¡Un barco a la deriva (motor apagado) SÍ está en navegación!
*   **Buque sin gobierno:** Incapaz de maniobrar por avería crítica.
*   **Buque con capacidad de maniobra restringida:** Incapacitado por la *naturaleza de su trabajo* (dragado, remolque complejo, oceanografía).

---

## Parte B: Reglas de Rumbo y Gobierno - Cinemática Vectorial

### Sección I: Visibilidad General (Reglas 4 a 10)

#### Regla 7: Riesgo de Abordaje y Cálculo de CPA/TCPA
La existencia de riesgo se determina evaluando la **Demora (Compass Bearing)**. Si la demora de un blanco que se acerca *no varía apreciablemente*, el abordaje existe.
Cinemáticamente, esto se modela calculando el CPA (Closest Point of Approach) y TCPA (Time to CPA).
Sean $\mathbf{v}_1$ y $\mathbf{v}_2$ los vectores de velocidad (Rumbo y Velocidad de Superficie) de dos buques, y $\Delta\mathbf{p}_0$ el vector de posición relativa inicial. La velocidad relativa es $\mathbf{v}_{rel} = \mathbf{v}_2 - \mathbf{v}_1$.
El tiempo hasta el CPA es:

$$ TCPA = - \frac{\Delta\mathbf{p}_0 \cdot \mathbf{v}_{rel}}{\|\mathbf{v}_{rel}\|^2} $$

Si $TCPA > 0$ y la distancia en el CPA ($D_{CPA} = \|\Delta\mathbf{p}_0 + \mathbf{v}_{rel} \times TCPA\|$) es inferior a un umbral de seguridad, la Regla 7 dicta que **HAY RIESGO**.

#### Regla 8: Maniobras para Evitar Abordajes
Toda maniobra debe ser amplia, evidente (evitar pequeños cambios de rumbo < 15º que el radar ARPA rival no filtrará a tiempo) y hecha con antelación.

### Sección II: Buques a la Vista (Reglas 11 a 18)

#### Regla 12: Velero vs Velero (Viento Aerodinámico)
1.  Viento por bandas contrarias: Cede el que amura a **babor**.
2.  Viento por misma banda: Cede el que está a **barlovento**.
*Física:* El buque a barlovento ensucia el flujo laminar de aire (desvente aerodinámico) del que está a sotavento, reduciendo la capacidad de maniobra de este último.

#### Regla 13: Alcance ("El que alcanza paga")
Se considera alcance cuando se aproxima desde > 22,5º a popa del través. Esta regla **anula absolutamente a todas las demás**. Un pequeño yate a vela que alcanza por la popa a un gigantesco petrolero debe apartarse. (Incluso si el petrolero está a motor y tú a vela).

#### Reglas 14 y 15: Vueltas Encontradas y Cruces (A motor)
*   **Frente a frente (14):** Ambos caen a **estribor**.
*   **Cruce (15):** Cede el paso el que vea al otro por **estribor** (debe pasar por su popa).

#### Regla 18: La Jerarquía Absoluta (Prioridad de Paso)
(S-R-P-V-M):
1.  **S**in gobierno.
2.  **R**estringido por maniobrabilidad/calado.
3.  **P**escando (redes/palangres profesionales).
4.  **V**ela.
5.  **M**otor.

---

## Parte C: Luces y Marcas - Espectrometría y Geometría Angular

### Regla 21: Sectores Angulares
La fotometría de las luces a bordo debe cumplir estrictos arcos de visibilidad para permitir trigonometría visual:
*   Tope (Blanca): $225^\circ$ ($112.5^\circ$ a cada lado de la proa).
*   Babor (Roja): $112.5^\circ$ desde proa.
*   Estribor (Verde): $112.5^\circ$ desde proa.
*   Alcance (Blanca): $135^\circ$ en popa (suma $225^\circ + 135^\circ = 360^\circ$).

### Configuraciones Críticas
*   **Velero:** Costados y alcance. (Día si va a motor: cono negro vértice abajo).
*   **Sin Gobierno:** Roja sobre Roja. Día: 2 bolas negras.
*   **Restringido:** Roja - Blanca - Roja. Día: Bola-Diamante-Bola.
*   **Fondeado:** Blanca todo horizonte. Día: 1 bola negra.
*   **Varado:** 2 rojas + luces fondeo. Día: 3 bolas negras.
*   **Pescando Arrastre:** Verde sobre Blanca. Red/Palangre: Roja sobre Blanca. Día: 2 conos opuestos por vértices.

---

## Parte D: Señales Acústicas (Física del Sonido)

*   **1 corta:** Caigo a Estribor.
*   **2 cortas:** Caigo a Babor.
*   **3 cortas:** Atrás.
*   **5 cortas:** ¡Peligro/Duda!

### Niebla y Visibilidad Reducida (Atenuación Acústica)
En niebla, la atenuación acústica es severa, exigiendo periodos estrictos:
*   A motor (avanzando): 1 larga/2 min.
*   A motor (detenido): 2 largas/2 min.
*   Privilegiados (Vela, Pesca, Restringido): 1 larga + 2 cortas / 2 min.

### Señales de Socorro (Anexo IV)
Exclusivas para peligro de vida: Bengalas rojas, llamas, humo naranja, SOS Morse, "MAYDAY" en Canal 16 VHF (156.800 MHz), brazos en cruz.

## Ejemplos Prácticos

**Problema 1: Cálculo Cinemático de Abordaje (CPA y TCPA)**
Navegamos en un buque propio (Own Ship, OS) a rumbo $R_1 = 045^\circ$ con una velocidad de $v_1 = 12 \text{ nudos}$. En nuestra pantalla de radar ARPA fijamos un blanco (Target, T) situado a una marcación inicial $\theta = 315^\circ$ (demora verdadera de $360^\circ$ o Norte directo) a una distancia inicial $d = 8 \text{ millas náuticas}$. El ARPA indica que el buque T navega a rumbo $R_2 = 135^\circ$ a una velocidad $v_2 = 15 \text{ nudos}$. 

Determine vectorialmente la velocidad relativa, el TCPA (Time to Closest Point of Approach) y la distancia del CPA, verificando si existe riesgo de abordaje inminente (Regla 7).

*Resolución:*
Establecemos un sistema de coordenadas cartesianas alineado con el Norte ($y$) y el Este ($x$).
Velocidad del buque propio $\mathbf{v}_1$:
$$ \mathbf{v}_1 = \langle 12 \sin(45^\circ), 12 \cos(45^\circ) \rangle = \langle 12 \times 0.707, 12 \times 0.707 \rangle = \langle 8.485, 8.485 \rangle \text{ nudos} $$

Velocidad del blanco $\mathbf{v}_2$:
$$ \mathbf{v}_2 = \langle 15 \sin(135^\circ), 15 \cos(135^\circ) \rangle = \langle 15 \times 0.707, -15 \times 0.707 \rangle = \langle 10.605, -10.605 \rangle \text{ nudos} $$

Vector de Velocidad Relativa $\mathbf{v}_{rel} = \mathbf{v}_2 - \mathbf{v}_1$:
$$ \mathbf{v}_{rel} = \langle 10.605 - 8.485, -10.605 - 8.485 \rangle = \langle 2.12, -19.09 \rangle \text{ nudos} $$
Magnitud de la velocidad relativa $\|\mathbf{v}_{rel}\| = \sqrt{2.12^2 + (-19.09)^2} \approx 19.2 \text{ nudos}$.

Vector de posición inicial relativa $\Delta\mathbf{p}_0$ (el blanco está al Norte a 8 millas):
$$ \Delta\mathbf{p}_0 = \langle 0, 8 \rangle \text{ millas} $$

Cálculo del TCPA:
$$ TCPA = - \frac{\Delta\mathbf{p}_0 \cdot \mathbf{v}_{rel}}{\|\mathbf{v}_{rel}\|^2} = - \frac{(0)(2.12) + (8)(-19.09)}{19.2^2} = - \frac{-152.72}{368.64} \approx 0.414 \text{ horas} $$
$$ TCPA = 0.414 \times 60 \approx 24.8 \text{ minutos} $$

Cálculo de la posición en el CPA y la distancia $D_{CPA}$:
$$ \Delta\mathbf{p}_{CPA} = \Delta\mathbf{p}_0 + \mathbf{v}_{rel} \times TCPA = \langle 0, 8 \rangle + \langle 2.12, -19.09 \rangle \times 0.414 $$
$$ \Delta\mathbf{p}_{CPA} = \langle 0 + 0.878, 8 - 7.903 \rangle = \langle 0.878, 0.097 \rangle \text{ millas} $$
$$ D_{CPA} = \sqrt{0.878^2 + 0.097^2} \approx 0.88 \text{ millas} $$

Dado que $D_{CPA}$ es menor de 1 milla náutica y el TCPA es positivo (ocurrirá en el futuro), se concluye que **HAY RIESGO DE ABORDAJE**. Según la Regla 15 (Cruce), nosotros vemos al blanco por babor y él nos ve por estribor, por lo que **el buque T debe ceder el paso**.

## Referencias Bibliográficas y Jurisprudencia

*   **Convenios Internacionales:**
    *   *Reglamento Internacional para Prevenir Abordajes (COLREGs 1972)*, enmendado. Organización Marítima Internacional.
*   **Textos Académicos:**
    *   *Farwell's Rules of the Nautical Road*, Craig H. Allen. El tratado fundamental sobre la aplicación legal y matemática del RIPA.
    *   *Marine Radar and ARPA*, A. Bole, A. Dineley. Para los cálculos cinemáticos rigurosos y tolerancia de sensores de a bordo.
*   **Jurisprudencia de Almirantazgo:**
    *   *The "Boleslaw Chrobry" [1974] 2 Lloyd's Rep. 308*: Estableció precedentes sobre la obligación de usar radar y trazar correctamente las posiciones relativas (TCPA/CPA), penalizando la mera observación en pantalla sin cálculo vectorial.
    *   *The "Volvox Hollandia" [1988] 2 Lloyd's Rep. 361*: Fallo sobre la Regla 2 (Negligencia y Agonía del Momento) donde se dictamina que la acción evasiva tardía por parte del buque con derecho de paso también constituye culpabilidad en la colisión.
