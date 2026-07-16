# Capitán de Yate - Tema 4: Cálculos Astronómicos

La parte más matemática del título. Exige saber tomar alturas de los astros con el sextante y usar el Almanaque Náutico.

## 1. El Sextante y la Medición de Alturas
*   **Sextante:** Instrumento óptico que mide el ángulo vertical entre el horizonte visible y un astro.
*   **Correcciones a la altura observada:** La altura leída en el sextante tiene errores físicos que hay que corregir:
    *   *Error de Índice:* Desajuste mecánico del sextante.
    *   *Depresión del Horizonte:* Por la altura del ojo del observador sobre el nivel del mar.
    *   *Refracción:* La luz se curva al atravesar la atmósfera.
    *   *Paralaje y Semidiámetro:* (Especialmente para el Sol y la Luna).

## 2. El Almanaque Náutico
Libro anual que contiene las coordenadas exactas (Declinación y Ángulo Horario) del Sol, la Luna, los 4 planetas visibles (Venus, Marte, Júpiter, Saturno) y 99 estrellas para cada segundo del año, referenciados al Tiempo Universal (UT).

## 3. La Recta de Altura (Método de Marcq St. Hilaire)
Una única observación de un astro no nos da una posición exacta (un punto), sino una **Línea de Posición (Recta de Altura)** sobre la que nos encontramos.
1.  Asumimos una posición estimada.
2.  Calculamos (con trigonometría) qué altura *deberíamos* haber medido si estuviéramos exactamente ahí (Altura Estimada).
3.  Comparamos la Altura Estimada con la Altura Verdadera (la medida con el sextante corregida).
4.  La diferencia nos da la **Diferencia de Alturas (Δa)**, indicando si estamos más cerca o más lejos del astro de lo que pensábamos.
5.  Se traza la recta perpendicular al acimut del astro.

## 4. Situación por Observación
Para hallar nuestro punto exacto de Latitud y Longitud, necesitamos cruzar **al menos dos rectas de altura**.
*   *Situación por rectas simultáneas:* Observar dos estrellas casi a la vez durante los crepúsculos (cuando se ven las estrellas y el horizonte).
*   *Situación por rectas no simultáneas:* Por ejemplo, tomar la altura del Sol por la mañana, navegar, y tomar la altura del Sol a mediodía (la Meridiana). Trasladando la primera recta con nuestro rumbo y velocidad, hallamos la situación al mediodía.
