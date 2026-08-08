# Navegación Astronómica Avanzada (Teoría del Capitán de Yate)

La navegación astronómica permite determinar la posición del buque observando los astros (Sol, Luna, planetas y estrellas) en combinación con la hora exacta y el almanaque náutico. Es el núcleo del temario de Capitán de Yate.

## 1. La Esfera Celeste
Imaginamos la Tierra en el centro de una esfera infinita sobre la que se proyectan los astros.
*   **Eje del mundo:** Prolongación del eje de rotación terrestre. Corta la esfera celeste en el Polo Norte Celeste (Pn) y el Polo Sur Celeste (Ps).
*   **Ecuador Celeste:** Proyección del ecuador terrestre sobre la esfera celeste.
*   **Cenit (Z):** El punto en la esfera celeste situado exactamente en la vertical del observador.
*   **Nadir (N):** El punto opuesto al Cenit.

## 2. Sistemas de Coordenadas

### Coordenadas Horizontales (Dependen del Observador)
Toman como plano fundamental el **Horizonte Verdadero** del observador.
*   **Altura (a):** Arco vertical medido desde el horizonte hasta el astro (0º a 90º). Es lo que se mide con el **sextante**.
*   **Acimut (Z):** Arco del horizonte medido desde el Norte hasta la vertical del astro (0º a 360º).

### Coordenadas Ecuatoriales (Dependen del Astro y del Tiempo)
Toman como plano fundamental el **Ecuador Celeste**.
*   **Declinación (d):** Ángulo entre el astro y el Ecuador Celeste (similar a la latitud terrestre). Va de 0º a 90º (Norte o Sur).
*   **Ángulo Horario (h):** Ángulo entre el meridiano de referencia y el meridiano del astro.
    *   **Ángulo Horario en Greenwich (hG):** Se mide desde el meridiano superior de Greenwich. Se obtiene directamente del Almanaque Náutico.
    *   **Ángulo Horario Local (hL):** Se mide desde el meridiano del observador. Relación: `hL = hG + Longitud` (Longitud Este es positiva, Oeste es negativa).

## 3. El Triángulo de Posición

Es un triángulo esférico formado en la esfera celeste por tres puntos clave:
1.  **Polo Elevado (Pn o Ps)**
2.  **Cenit (Z)** del observador
3.  **Astro (A)**

Los lados de este triángulo son arcos de círculo máximo:
*   **Colatitud (90º - l):** Distancia del Polo al Cenit.
*   **Codeclinación o Distancia Polar (90º - d):** Distancia del Polo al Astro.
*   **Distancia Cenital (90º - a):** Distancia del Cenit al Astro.

Resolviendo este triángulo esférico mediante trigonometría, podemos obtener la Altura Calculada (ac) y el Acimut (Z) de un astro para una posición estimada y un instante dado.

## 4. La Recta de Altura (Método de Marcq St. Hilaire)

El Almirante francés Marcq de Saint-Hilaire (1875) ideó el método que se utiliza hoy en día universalmente para posicionarse. No calcula directamente la latitud y longitud, sino una "Línea de Posición" o "Recta de Altura".

### El concepto de Círculo de Alturas Iguales
En un instante dado, un astro está exactamente en la vertical (Cenit) de un punto de la Tierra llamado **Polo de Iluminación** (o Punto Astral). Cualquier observador situado a la misma distancia de ese punto medirá la misma Altura del astro. Esto forma un inmenso círculo sobre la Tierra.

Como el radio de este círculo es inmenso, el pequeño segmento del círculo que pasa cerca del barco se considera una línea recta: la **Recta de Altura**.

### Pasos del Método Marcq St. Hilaire:
1.  **Observación:** Con el sextante se mide la altura del astro y se anota la hora exacta (HcG). Tras aplicar las correcciones del sextante (error de índice, refracción, paralaje), obtenemos la **Altura Verdadera (av)**.
2.  **Cálculo:** Asumiendo nuestra **Situación Estimada (Se)**, utilizamos las fórmulas del triángulo de posición y el Almanaque para calcular qué altura teórica debería tener el astro. Obtenemos la **Altura Calculada (ac)** y el **Acimut (Z)**.
3.  **Diferencia de Alturas (Diferencia = av - ac):**
    *   Si `av > ac`: Estamos más cerca del astro que nuestra posición estimada.
    *   Si `av < ac`: Estamos más lejos.
4.  **Trazado:** En la carta, desde nuestra posición estimada, trazamos la línea del Acimut. Sobre ella, medimos la Diferencia de Alturas (en millas náuticas). En ese punto, trazamos una línea perpendicular al acimut. Esa es nuestra **Recta de Altura**. El barco está en algún punto de esa recta.
5.  Para obtener un **Punto Verdadero (Situación)**, necesitamos cruzar dos o más Rectas de Altura de diferentes astros (observados simultáneamente o trasladando la primera recta según el rumbo y velocidad del barco).
