# Cálculos de Navegación (PER, PY y CY)

La navegación costera y de altura requiere pasar de la teoría a las matemáticas. El trazado en la carta náutica (usando el transportador de ángulos, el compás y las reglas paralelas) se basa en vectores y trigonometría plana (Loxodromia) o esférica (Ortodromia). 

En esta guía desglosamos las fórmulas y problemas clásicos de examen y de la vida real.

---

## 1. El Triángulo de Velocidades: Deriva y Corrientes

El mar no es estático. Cuando un barco navega, el agua sobre la que flota puede estar moviéndose. A este movimiento del agua lo llamamos **Corriente**.

*   **Rumbo Verdadero (Rv):** Hacia dónde apunta la proa del barco respecto al fondo del mar.
*   **Velocidad de Máquina (Vb):** La velocidad que marca nuestra corredera (la velocidad del barco sobre el agua).
*   **Rumbo de la Corriente (Rc):** Hacia dónde va la corriente.
*   **Intensidad Horaria de la Corriente (Ihc):** La velocidad de la corriente (en nudos).
*   **Rumbo Efectivo (Ref):** La suma vectorial del Rv y la Corriente. Es por donde *realmente* transita el barco sobre el fondo del océano.
*   **Velocidad Efectiva (Vef):** Nuestra velocidad real respecto a tierra firme.

Para hallar el Rumbo Efectivo (lo que te piden en los exámenes de Patrón de Yate), se traza el vector de nuestro barco (Rv y Vb), y desde la punta de esa flecha, se engancha el vector de la corriente (Rc y Ihc). La línea que une nuestro origen con el final de la corriente es el vector efectivo.

---

## 2. El Abatimiento (El Viento nos empuja)

A diferencia de la corriente (que empuja todo el barco en masa), el viento choca contra la obra muerta (el casco fuera del agua y las velas) y empuja el barco lateralmente. A esto se le llama **Abatimiento (Ab)**.

*   Si el viento nos da por Estribor (nos empuja hacia Babor), el abatimiento es **Negativo (-)**.
*   Si el viento nos da por Babor (nos empuja hacia Estribor), el abatimiento es **Positivo (+)**.

**Fórmula de Corrección:**
`Rumbo de Superficie (Rs) = Rumbo Verdadero (Rv) + Abatimiento (Ab)`

*Nota de examen PY:* Si hay corriente y abatimiento a la vez, el orden de cálculo es: primero aplicas el viento al Rv para hallar el Rs. Luego usas el Rs y la Vb como vector propio para sumarle la corriente y hallar el Rumbo Efectivo final.

### Ejemplo Resuelto: Cálculo de Deriva por Viento (Abatimiento)

**Enunciado:** Un velero navega a un Rumbo Verdadero $Rv = 090°$ (Este puro). El viento sopla con fuerza constante desde el Norte, entrándole al barco por su costado de Babor, y el patrón estima, por la escora y el tipo de aparejo, un abatimiento de $Ab = 6°$.

**Resolución:**
1. El viento entra por Babor → empuja el barco hacia Estribor → el abatimiento es **positivo**, según la regla de signos de este apartado.
2. Aplicamos la fórmula de corrección:
   $$ Rs = Rv + Ab = 090° + 6° = 096° $$
3. **Conclusión:** Aunque la proa apunte a $090°$, el barco se está deslizando lateralmente y su rumbo de superficie real es $096°$. Si no se corrige, el barco terminará más al Sur de lo previsto en la carta (si no hay corriente adicional que combinar).

*Nota:* Si a este resultado se le sumara además una corriente, el Rs de $096°$ pasaría a usarse como el rumbo del vector propio del barco para la composición vectorial con la corriente (ver apartado 1), nunca al revés.

---

## 3. Navegación Loxodrómica (Estima Analítica)

Cuando no podemos situarnos por referencias visuales en la costa ni tenemos GPS, debemos usar la Navegación por Estima (Dead Reckoning).
Consiste en calcular nuestra posición sabiendo de dónde salimos, a qué rumbo hemos ido y durante cuánto tiempo.

Se usan fórmulas trigonométricas (Loxodromia) asumiendo que navegamos cortando los meridianos con el mismo ángulo (rumbo constante).

**Datos necesarios:**
*   Latitud y Longitud de Salida ($l_s$, $L_s$).
*   Rumbo (R) (convertido a formato cuadrantal, ej: S 45 E).
*   Distancia navegada ($D = Velocidad \times Tiempo$).

**Fórmulas Básicas de Estima:**
1.  **Diferencia de Latitud ($\Delta l$):** $\Delta l = D \times \cos(R)$
2.  **Apartamiento (A):** $A = D \times \sin(R)$
3.  **Diferencia de Longitud ($\Delta L$):** $\Delta L = \frac{A}{\cos(l_m)}$ (donde $l_m$ es la latitud media entre la salida y la llegada).

Al sumar los diferenciales a nuestra posición de salida, obtenemos nuestra posición de llegada calculada analíticamente, sin mirar una carta.

### Ejemplo Resuelto: Estima Analítica Completa

**Enunciado:** Un barco sale de un punto situado en $l_s = 36° 00.0' N$, $L_s = 005° 30.0' W$, navega a un Rumbo $R = N 60° E$ (cuadrantal) a una velocidad constante $Vb = 8$ nudos durante $2h\ 30m$. Calcula la posición estimada de llegada.

**Resolución:**
1. **Distancia navegada:**
   $$ D = Vb \times t = 8 \text{ nudos} \times 2.5\text{ h} = 20 \text{ millas náuticas} $$
2. **Diferencia de latitud** (con $R = 60°$ respecto al Norte, cuadrante NE):
   $$ \Delta l = D \times \cos(R) = 20 \times \cos(60°) = 20 \times 0.5 = 10.0' \ (\text{hacia el N, mismo signo que la componente N del rumbo}) $$
3. **Apartamiento:**
   $$ A = D \times \sin(R) = 20 \times \sin(60°) = 20 \times 0.866 = 17.3' \ (\text{hacia el E}) $$
4. **Latitud de llegada:**
   $$ l_{llegada} = 36° 00.0' N + 10.0' = 36° 10.0' N $$
5. **Latitud media** (para corregir la convergencia de meridianos):
   $$ l_m = \frac{36°00.0' + 36°10.0'}{2} = 36° 05.0' N $$
6. **Diferencia de longitud:**
   $$ \Delta L = \frac{A}{\cos(l_m)} = \frac{17.3'}{\cos(36°05.0')} = \frac{17.3'}{0.8078} \approx 21.4' \ (\text{hacia el E, porque el rumbo tiene componente Este}) $$
7. **Longitud de llegada** (la longitud de salida es W, y avanzamos hacia el E, por lo que el valor W disminuye):
   $$ L_{llegada} = 005° 30.0' W - 21.4' = 005° 08.6' W $$

**Posición estimada de llegada:** $36° 10.0' N$, $005° 08.6' W$.

---

## 4. Navegación Ortodrómica (El Círculo Máximo)

Este bloque es exclusivo del temario de **Capitán de Yate (CY)**.
Para distancias cortas (costeras), la Tierra parece plana. Pero para cruzar un océano, la línea recta en una carta plana (loxodromia) **no es la distancia más corta**. La distancia más corta entre dos puntos en una esfera es un arco de círculo máximo (Ortodromia).

*   **Loxodromia:** Rumbo constante, línea curva en la esfera terrestre (derrochas millas).
*   **Ortodromia:** Rumbo continuamente variable, línea recta en la esfera terrestre (ahorras millas y combustible).

Para calcular el rumbo inicial ortodrómico y la distancia total a recorrer, se utiliza trigonometría esférica pesada mediante el **Cálculo de la Fórmulas de Euler** o mediante las tablas de cálculo astronómico (A.B.C).

---

## 5. El Cálculo de Mareas

Afecta vitalmente a los navegantes para no encallar al entrar en puerto. Las mareas suben y bajan siguiendo ciclos lunares.

*   **Pleamar (PM):** Momento de nivel más alto.
*   **Bajamar (BM):** Momento de nivel más bajo.
*   **Amplitud (A):** Diferencia en metros entre la PM y la BM.
*   **Duración (D):** Tiempo que tarda en pasar de BM a PM.

### Problema Directo
*Pregunta:* "Son las 10:30h, ¿Qué sonda (profundidad) tendré en este punto?"
Se soluciona entrando en el Anuario de Mareas para ver la BM y PM del día, interpolando la hora mediante las tablas de marea o la fórmula del cuarto de la duración.

### Problema Inverso
*Pregunta:* "Mi barco cala 2.5 metros. ¿A qué hora exacta de la tarde habrá suficiente agua para entrar al puerto sin encallar?"
Se calcula la sonda mínima requerida (Calado + Resguardo bajo la quilla - Sonda de la Carta) y se busca a qué hora la marea alcanza ese nivel específico ascendiendo.
