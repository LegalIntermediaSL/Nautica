# Capitán de Yate - Tema 4: Cálculos Astronómicos

El bloque de cálculo del Capitán de Yate es la prueba definitiva de navegación astronómica. Requiere un manejo fluido del sextante (teórico), del Almanaque Náutico y de las tablas de resolución trigonométrica.

---

## 1. Correcciones de la Altura del Sextante

Cuando medimos el ángulo vertical de un astro sobre el horizonte con el sextante, obtenemos la **Altura Instrumental ($ai$)**. Esta medida está sujeta a varios errores físicos que debemos corregir para obtener la **Altura Verdadera ($av$)**.

Fórmula general:
\[ av = ai + ei + Dp + C_{ref} + C_{par} + C_{SD} \]

1.  **Error de Índice ($ei$):** Desajuste mecánico de los espejos del sextante. Puede ser aditivo o sustractivo (+ o -). Nos da la *Altura Observada ($ao$)*.
2.  **Depresión del Horizonte ($Dp$):** Como el ojo del observador está elevado (ej. 3 metros sobre el mar), vemos un horizonte aparente más bajo que el real. Siempre se resta (-). Se busca en la Tabla C del Almanaque.
3.  **Refracción ($C_{ref}$):** La luz del astro se curva al atravesar las capas de la atmósfera (más densas abajo). El astro parece estar más alto de lo que realmente está. Siempre se resta (-).
4.  **Paralaje ($C_{par}$):** Diferencia de ángulo si observáramos desde la superficie frente al centro de la Tierra. Muy notable en la Luna. Siempre se suma (+).
5.  **Semidiámetro ($C_{SD}$):** Si observamos el limbo inferior del Sol, debemos sumar su radio para hallar el centro del astro. (+ o - según el limbo observado).

> En el Almanaque Náutico hay unas tablas conjuntas (Correcciones de Altura para Sol, Estrellas y Planetas) que agrupan Refracción y Semidiámetro.

## 2. Cálculo de la Situación por Rectas de Altura (Método de Marcq St. Hilaire)

El método más elegante y preciso para situarse en medio del océano.

### Pasos de la resolución
1.  **Situación de Estima ($le, Le$):** El lugar donde *creemos* que estamos en el momento de la observación.
2.  **Cálculo del Horario del Astro en Greenwich ($hG$):** Usamos la hora UTC exacta de la observación y entramos en las páginas diarias del Almanaque Náutico.
3.  **Ángulo Horario Local ($hL$):**
    \[ hL = hG + Le \quad \text{(Sumar si la Longitud es Este, Restar si es Oeste)} \]
4.  **Obtención de la Declinación ($Dec$) del astro** del Almanaque Náutico.
5.  **Resolución del Triángulo de Posición:** Con la Latitud ($le$), la Declinación ($Dec$) y el Ángulo Horario ($hL$), usamos fórmulas trigonométricas esféricas para calcular:
    *   **Altura Estimada ($ae$):** La altura que el astro *debería* tener si estuviéramos exactamente en la situación de estima.
    *   **Zimut ($Z$):** El rumbo hacia el astro.
6.  **Diferencia de Alturas ($\Delta a$):**
    \[ \Delta a = av - ae \]
    *   Si $\Delta a$ es **positivo**, estamos más cerca del astro de lo que pensábamos (vamos en dirección al Azimut).
    *   Si $\Delta a$ es **negativo**, estamos más lejos del astro (vamos en dirección opuesta al Azimut).

### Trazado en la Carta
Desde la situación de estima, trazamos la línea del Azimut. Sobre esa línea, medimos la distancia $\Delta a$ (en millas náuticas, ya que 1 minuto de arco = 1 milla). En ese punto trazamos una recta perpendicular. Esa es nuestra **Recta de Altura**. El barco está en algún lugar de esa recta.

## 3. Situación por Dos Rectas de Altura
Para obtener nuestra Latitud y Longitud precisas, necesitamos el corte de dos Rectas de Altura.

*   **Observación simultánea (Crepúsculo estelar):** Se miden dos estrellas con una diferencia de pocos minutos. Las dos rectas se cruzan directamente.
*   **Observación no simultánea (Sol por la mañana y Meridiana):** Al no poder ver dos Soles a la vez, se traslada la recta obtenida por la mañana utilizando el Rumbo y Velocidad del barco, hasta cortarla con la recta de la altura Meridiana al mediodía.

## 4. La Latitud por la Altura Meridiana del Sol
Es el método más sencillo y clásico. Ocurre exactamente al mediodía verdadero local, cuando el Sol cruza nuestro meridiano superior (su altura es la máxima del día y su azimut es exactamente Norte o Sur).

Fórmula:
\[ l = Z + Dec \]
*Donde Z es la distancia cenital ($90^\circ - av$). Hay que tener extremo cuidado con los signos (Latitudes y Declinaciones del mismo nombre o distinto nombre).*
