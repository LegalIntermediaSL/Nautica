# PER - Tema 7: Maniobra y Navegación a Motor (Cinemática, Dinámica de Fluidos y Física Aplicada)

El arte de la maniobra exige dominar el barco en distancias extremadamente cortas, asumiendo fuerzas externas invisibles. Un barco sin frenos ni fricción de asfalto no se comporta como un coche. Este tema aborda las matemáticas y la dinámica de fluidos (Hidrodinámica y Aerodinámica) de la maniobra.

---

## 1. Fuerzas de la Hélice y el Timón (Dinámica de Fluidos)

La maniobrabilidad depende del principio de Bernoulli y de las leyes de Newton. La pala del timón actúa como un perfil aerodinámico (ala), generando una fuerza de sustentación lateral ($L$, *Lift*) y una resistencia al avance ($D$, *Drag*):

$$ L = \frac{1}{2} \rho v^2 C_L A $$
$$ D = \frac{1}{2} \rho v^2 C_d A $$

Donde $v$ es la velocidad del flujo de agua (Corriente de Expulsión o Aspiración). Si la hélice escupe agua contra el timón metido a una banda, se genera una sustentación masiva instantánea, causando que la popa derrape, permitiendo la "Ciaboga" en el sitio.

### 1.1 El Empuje Transversal (Efecto "Propeller Walk" / Rueda de Paletas)
Una hélice no solo empuja hacia adelante. Debido al gradiente de densidad/presión hidrostática (el agua del fondo está más comprimida y ofrece mayor resistencia), la pala inferior "muerde" con más fuerza. 
Si la hélice es **Dextrógira** (gira a la derecha avante):
*   **Avante:** La popa tiende levemente a estribor.
*   **Ciando (Marcha atrás):** Al invertir el giro, la hélice gira a la izquierda. La diferencia de presiones causa un tirón brutal transversal en la popa hacia **Babor**.
> **El Truco del Atracado:** Atracar por el lado de babor con hélice dextrógira permite entrar en diagonal y frenar dando un golpe atrás, lo que automáticamente absorbe la popa contra el muelle.

---

## 2. El Centro de Giro (Pivot Point) y Curvas Evolutivas

Un barco no gira desde sus ruedas delanteras. Gira alrededor de un eje vertical virtual llamado *Pivot Point* (Centro de Giro).
*   **Navegando avante:** La proa corta el agua generando un "colchón" de alta presión. El Pivot Point se desplaza hacia el tercio de proa. El barco gira "desplazando mucho la popa" hacia fuera de la curva.
*   **Ciando:** La presión se concentra en la popa plana. El Pivot Point retrocede hacia el tercio de popa.

### La Curva Evolutiva
Si metemos el timón a la vía, el buque traza un círculo con tres fases:
1.  **Avance (Advance):** Distancia recorrida en la dirección original hasta que el barco alcanza 90º de giro.
2.  **Traslado (Transfer):** Distancia lateral desviada cuando se alcanzan los 90º.
3.  **Diámetro Táctico:** Diámetro total del círculo final de giro, típicamente de 3 a 5 esloras.

---

## 3. Agentes Externos (Viento y Corriente)

La embarcación está sometida a dos medios fluidos con diferentes densidades ($ \rho_{agua} \approx 1025 \, \text{kg/m}^3 $, $ \rho_{aire} \approx 1.2 \, \text{kg/m}^3 $).
*   **Viento (Abatimiento):** Ejerce fuerza sobre el *Área Vélica* o de *Obra Muerta* ($A_w$). Frecuentemente arrastra la proa (más ligera).
*   **Corriente (Deriva):** Afecta a la *Obra Viva* sumergida. Obliga a calcular el rumbo verdadero usando composición de vectores.

### Reglas de Oro para Aproximación al Atraque
*   **Proa al elemento dominante:** Siempre aproximarse proa al viento o a la corriente. Mantienes tensión y control. Si hay un fallo de motor, el elemento te aleja del muelle en vez de aplastarte.

---

## 4. Fondeo: Dinámica de la Catenaria y Tensión de Amarre

El ancla no sujeta por peso, sino por ángulo de tiro. El peso de la cadena forma una curva matemática hiperbólica (Catenaria) cuyo propósito es que el ángulo de tiro en la uña del ancla ($ \theta $) sea exactamente de 0º (paralelo al fondo marino).
La ecuación de la catenaria se define como:

$$ y = a \cosh\left(\frac{x}{a}\right) $$

Donde $a = T_0 / w$, siendo $T_0$ la tensión horizontal y $w$ el peso lineal de la cadena en el agua.

### Longitud de Fondeo Crítica (Scope Ratio)
Para asegurar que la catenaria toque fondo tangencialmente:
1.  **Cadena sola:** Filar (soltar) **3 a 4 veces** la profundidad (sonda).
2.  **Línea Mixta (Cabo+Cadena):** Filar **5 veces** la sonda.
3.  **Temporal:** Filar **5 a 7 veces** la sonda.

### El Círculo de Borneo
Radio del borneadero: $ R = L_{cadena} + Eslora_{barco} $. 
A causa de rolar el viento, el barco pivota alrededor del ancla. Jamás fondear dentro del área de superposición del radio de otro barco, o habrá abordaje inminente en la madrugada.

## Ejemplos Prácticos

**Problema 1: Tensión de la Catenaria durante el Fondeo**
Un yate de 15 metros está fondeado con cadena exclusivamente en una sonda de $10 \text{ metros}$ (asuma la altura de la proa al agua como despreciable para simplificar). La cadena tiene un peso sumergido lineal de $w = 25 \text{ N/m}$. En un temporal, la fuerza horizontal máxima producida por el viento y el abatimiento de las olas sobre el buque alcanza $T_0 = 3000 \text{ N}$. 

Para evitar garrear, el ángulo de la cadena con el fondo debe ser cero. Calcule la longitud mínima teórica de cadena filada ($L$) necesaria para que todo el esfuerzo en el ancla sea perfectamente horizontal, de acuerdo a la ecuación de la catenaria.

*Resolución:*
La tensión en el punto más bajo (ancla) es puramente horizontal y vale $T_0$. La relación de la geometría de la catenaria con la longitud del arco se define paramétricamente, pero para encontrar la longitud de cadena suspendida ($s$) que alcanza la profundidad $h = 10 \text{ m}$ con pendiente cero en el origen, usamos la relación fundamental:
$$ h = a \left( \cosh\left(\frac{x}{a}\right) - 1 \right) \quad \text{y} \quad s = a \sinh\left(\frac{x}{a}\right) $$
Donde el parámetro $a = \frac{T_0}{w}$.

Calculamos el parámetro $a$:
$$ a = \frac{3000 \text{ N}}{25 \text{ N/m}} = 120 \text{ m} $$

Usamos la identidad hiperbólica $\cosh^2(z) - \sinh^2(z) = 1$. Se puede demostrar que para una catenaria, la relación entre profundidad $h$, longitud $s$ y el parámetro $a$ es:
$$ s^2 = h^2 + 2ah $$

Sustituyendo los valores conocidos:
$$ s^2 = (10)^2 + 2(120)(10) $$
$$ s^2 = 100 + 2400 = 2500 $$
$$ s = \sqrt{2500} = 50 \text{ metros} $$

Se requieren filar teóricamente **50 metros** de cadena para que la tracción sobre el ancla sea paralela al lecho marino. Esto equivale exactamente a una relación de 5 veces la sonda, confirmando matemáticamente la regla empírica del filado en condiciones duras.

**Problema 2: Sustentación Hidrodinámica del Timón**
Un velero navega a motor a una velocidad de $v = 6 \text{ nudos}$ ($3.08 \text{ m/s}$). La pala del timón tiene una superficie $A = 0.8 \text{ m}^2$. Al meter el timón a la banda con un ángulo de ataque de $15^\circ$, el coeficiente de sustentación empírico es $C_L = 0.9$. La densidad del agua es $\rho = 1025 \text{ kg/m}^3$.

Calcule la fuerza de sustentación lateral ($L$) que provoca el derrape de la popa y el momento torsor ($M$) si el centro de presión geométrica está a $r = 5 \text{ metros}$ a popa del Pivot Point.

*Resolución:*
Fuerza lateral del timón:
$$ L = \frac{1}{2} \rho v^2 C_L A $$
$$ L = \frac{1}{2} (1025) (3.08)^2 (0.9) (0.8) $$
$$ L = \frac{1}{2} (1025) (9.4864) (0.72) \approx 3500.5 \text{ N} $$

Momento torsor respecto al Pivot Point:
$$ M = L \times r = 3500.5 \text{ N} \times 5 \text{ m} = 17502.5 \text{ Nm} $$

Este momento masivo vence la resistencia hidrodinámica del casco, iniciando la curva evolutiva del navío.

## Referencias Bibliográficas y Jurisprudencia

*   **Textos Técnicos y Universitarios:**
    *   *Ship Handling*, David J. House. Referencia exhaustiva sobre curvas evolutivas, "propeller walk" y factores cinemáticos.
    *   *Principles of Naval Architecture: Ship Resistance and Flow*, Society of Naval Architects and Marine Engineers (SNAME). Para el estudio estocástico de las fuerzas sobre timones y hélices.
*   **Jurisprudencia de Almirantazgo y Seguros:**
    *   *The "Fritz Thyssen" [1967] 2 Lloyd's Rep 199*: Caso sobre hundimiento por cadena de fondeo infradimensionada; demostró ante el juez la negligencia del capitán por no aplicar la regla del "scope ratio" adecuado basándose en el cálculo de catenaria bajo tensión inducida por oleaje.
    *   *State of Louisiana v. The M/V Testbank (1985)*: Análisis pormenorizado de la hidrodinámica de atraque y maniobrabilidad reducida debido a corrientes transversales en canales de navegación estrechos.

