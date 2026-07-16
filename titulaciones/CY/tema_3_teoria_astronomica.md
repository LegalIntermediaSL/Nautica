# Capitán de Yate - Tema 3: Teoría Astronómica

Para poder realizar los cálculos astronómicos mecánicos, el Capitán de Yate debe primero interiorizar y visualizar mentalmente la geometría esférica del universo observable desde la Tierra.

---

## 1. La Esfera Celeste y el Observador

Se asume el sistema geocéntrico (ptolemaico) para la navegación, ya que resulta práctico y matemáticamente idéntico a los efectos de cálculo visual. La Tierra es el centro de una esfera de radio infinito.

### Puntos y Planos de Referencia
*   **Eje del Mundo:** La prolongación del eje de rotación terrestre. Corta a la esfera celeste en el Polo Norte Celeste y Polo Sur Celeste.
*   **Ecuador Celeste:** La proyección del ecuador terrestre hacia el infinito. Divide el cielo en Hemisferio Norte y Hemisferio Sur celestes.
*   **La Vertical del Observador:** Una línea recta imaginaria que pasa por el centro de la Tierra y por el observador. Corta la esfera en dos puntos: el **Cenit** (arriba) y el **Nadir** (abajo).
*   **Horizonte Astronómico:** El plano perpendicular a la Vertical del Observador que pasa por el centro de la Tierra.

## 2. Sistemas de Coordenadas

Para ubicar un astro (por ejemplo, la estrella Sirio) en la bóveda celeste, la navegación utiliza diferentes sistemas de coordenadas que hay que saber transformar.

### 2.1. Coordenadas Horizontales (Basadas en el Observador)
Sirven para apuntar el sextante.
*   **Altura (a):** Ángulo vertical desde el horizonte hasta el astro (de 0º a 90º).
*   **Azimut (Z):** Ángulo horizontal medido desde el Norte (000º) hacia el Este u Oeste hasta la vertical del astro.

### 2.2. Coordenadas Ecuatoriales (Basadas en la Tierra)
Las coordenadas "absolutas" que vienen en el Almanaque Náutico, equivalentes a la Latitud y Longitud terrestres.
*   **Declinación (Dec):** Distancia angular desde el Ecuador Celeste hasta el astro. Positiva (Norte) o Negativa (Sur). Análoga a la Latitud.
*   **Ángulo Horario Local (hL):** Ángulo medido en el Ecuador Celeste desde el meridiano superior del observador hasta el meridiano del astro (siempre hacia el Oeste, de 0º a 360º).
*   **Ángulo Horario en Greenwich (hG):** Lo mismo que el hL, pero medido desde el Meridiano de Greenwich.

### 2.3. Coordenadas Ecuatoriales Absolutas (Basadas en las Estrellas)
*   **Ascensión Recta (AR):** Ángulo medido desde el **Punto de Aries** (el punto donde el Sol cruza el Ecuador en primavera) hacia el Este a lo largo del Ecuador Celeste.

## 3. El Triángulo de Posición Astronómico

Es la pieza angular de la navegación. Al resolver este triángulo esférico, vinculamos las coordenadas de la Tierra con las del cielo.

Sus tres **vértices** son:
1.  El Polo Elevado (Pn o Ps).
2.  El Cenit del Observador (Z).
3.  El Astro observado (A).

Sus tres **lados** (medidos en grados) son:
*   **Colatitud (90º - Latitud):** La distancia del Polo al Cenit.
*   **Codeclinación (90º - Declinación):** La distancia del Polo al Astro (Distancia Polar).
*   **Distancia Cenital (90º - Altura):** La distancia del Cenit al Astro.

Sus **ángulos** internos más importantes:
*   El ángulo en el Polo es el **Ángulo Horario Local (hL)**.
*   El ángulo en el Cenit es el **Azimut (Z)**.

> Mediante las fórmulas de la trigonometría esférica de Borda o de la Cosenusa, si conocemos la Declinación, el Ángulo Horario y una Latitud estimada, podemos calcular matemáticamente qué Altura debería tener el astro.

## 4. El Movimiento Aparente de los Astros
*   **Ortos y Ocasos:** Salida (orto) y puesta (ocaso) de los astros por el horizonte.
*   **El Crepúsculo:** El periodo previo a la salida del Sol (matutino) o posterior a la puesta (vespertino) donde hay luz ambiental pero el Sol está por debajo del horizonte.
    *   *Crepúsculo Civil:* El Sol está entre 0º y -6º bajo el horizonte. Ya no se ven las estrellas.
    *   *Crepúsculo Náutico:* El Sol está entre -6º y -12º bajo el horizonte. **Es el único momento útil para situarse por estrellas**, ya que se ven las estrellas brillantes (para apuntar) y aún hay suficiente luz ambiental para perfilar el horizonte en el sextante.
