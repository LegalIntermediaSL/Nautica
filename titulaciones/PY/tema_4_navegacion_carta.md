# Patrón de Yate - Tema 4: Navegación de Altura (Carta y Estima Analítica)

El bloque de Navegación del Patrón de Yate (PY) es el filtro principal y más temido del examen oficial. Requiere precisión milimétrica, limpieza en el trazado de la carta (Carta 105 del Estrecho de Gibraltar) y una fluidez absoluta con la trigonometría plana.

---

## 1. La Navegación por Estima Analítica (El Sistema Matemático)

La Estima (Dead Reckoning) es el método matemático para calcular en qué coordenadas estás sumando al punto de partida el rumbo y la distancia navegada, sin mirar fuera del barco. Es fundamental si hay niebla espesa o de noche sin costa a la vista.

En Patrón de Yate, la estima no se dibuja en la carta si excede las distancias cortas, sino que **se calcula analíticamente usando fórmulas trigonométricas de la Loxodrómica (Navegación Plana)**. Asumimos la curvatura de la Tierra como un plano para trayectos menores de 300 millas.

### El Triángulo de Estima (Las Fórmulas Base)
Si conocemos nuestra situación de salida ($l_s$, $L_s$), el Rumbo Verdadero ($Rv$) y la Distancia navegada por la corredera ($D$), el viaje forma un triángulo rectángulo virtual en el mapa.

1.  **Diferencia de Latitud ($\Delta l$):** Distancia Norte-Sur recorrida.
    $$ \Delta l = D \cdot \cos(Rv) $$
    *(El resultado sale en minutos de grado, que equivalen a millas. Se suma algebraicamente a la $l_s$ para hallar la Latitud de llegada).*

2.  **Apartamiento ($A$):** La distancia física real Este-Oeste navegada (en millas náuticas). No es la Longitud.
    $$ A = D \cdot \sin(Rv) $$

3.  **Latitud Media ($l_m$):** El promedio exacto de las latitudes de salida y llegada. Necesaria porque los meridianos de la Tierra convergen en los polos, estrechando el grado de Longitud.
    $$ l_m = \frac{l_{salida} + l_{llegada}}{2} $$

4.  **Diferencia de Longitud ($\Delta L$):** Distancia Este-Oeste en grados angulares de la Tierra.
    $$ \Delta L = \frac{A}{\cos(l_m)} $$
    *(Se suma algebraicamente a la $L_s$ para hallar la Longitud de llegada).*

### Cálculo Inverso (Rumbo Directo a un Rescate)
Si recibes un Mayday con unas coordenadas de destino, y conoces las tuyas, debes hallar tu Rumbo y Distancia directos.

1.  **Rumbo:**
    $$ \tan(Rv) = \frac{A}{\Delta l} $$
    *(Atención: La calculadora te da un ángulo entre 0º y 90º. Debes aplicar el cuadrante. Si vas hacia el SW, el rumbo será $180º + \text{ángulo}$.)*

2.  **Distancia Directa:**
    $$ D = \frac{\Delta l}{\cos(Rv)} \quad \text{o bien} \quad D = \frac{A}{\sin(Rv)} $$

---

## 2. Abatimiento (El Efecto del Viento)

El viento empuja el caso (obra muerta) lateralmente. La proa apunta hacia un lado, pero el barco resbala hacia otro.

*   **Abatimiento ($Ab$):** El ángulo de resbalamiento lateral.
    *   Si el viento sopla por Babor, te empuja hacia Estribor: **$Ab$ Positivo (+)**.
    *   Si el viento sopla por Estribor, te empuja hacia Babor: **$Ab$ Negativo (-)**.

*   **Rumbo de Superficie ($Rs$):** Es la estela real que dejas en el agua.
    $$ Rs = Rv + Ab $$

Cuando quieres trazar tu rumbo real en la carta bajo el viento, dibujas el $Rs$. Cuando quieres saber qué Rumbo de Aguja poner en el timón para conseguir ese $Rs$:
    $$ Ra = Rs - Ab - Ct $$

---

## 3. Deriva (El Efecto de las Corrientes Marinas)

La corriente es el río de agua en movimiento dentro del mar. Se lleva al barco entero consigo. A diferencia del viento (que desvía la estela), la corriente traslada el barco pero el agua de su alrededor se mueve con él.

*   **Rumbo de la Corriente ($Rc$):** Dirección hacia la que fluye el agua (Ej: $135^\circ$).
*   **Intensidad Horaria ($Ihc$):** Velocidad de la corriente en nudos.

### Problema Directo de Corrientes (¿Dónde acabaré?)
Dado tu Rumbo Verdadero, tu Velocidad de máquina, y los datos de la corriente:

```mermaid
graph TD
    A((Situación Inicial)) -- Rumbo y Vel. Buque (Rv, Vb) --> B((Punto Estimado sin Corriente))
    B -- Rumbo e Intens. Corriente (Rc, Ihc) --> C((Situación Efectiva P.E.))
    A -. Rumbo y Vel. Efectiva (Ref, Vef) .-> C
```

1. Desde tu situación inicial, traza tu vector (Rumbo Verdadero y longitud igual a Velocidad del barco).
2. Desde la punta de tu vector, engancha la cola del vector de corriente (Rumbo de Corriente y longitud igual a Intensidad Horaria).
3. Une la situación inicial con la punta del vector de corriente. ¡Ese es tu **Rumbo Efectivo (Ref)** sobre el fondo, y midiendo su longitud sacas tu **Velocidad Efectiva (Vef)** real!

### Problema Inverso de Corrientes (El Cálculo de Táctico)
Quieres ir directo al Puerto B, pero hay una fuerte corriente atravesada. Si apuntas a B, la corriente te mandará a las rocas. ¿Hacia dónde debes apuntar la proa para que la suma de tu motor + corriente te empuje exactamente en línea recta hacia B?

1. Une tu salida y B. Esa línea es tu **Rumbo Efectivo ($Ref$)** innegociable.
2. Desde tu salida, dibuja la corriente exactamente como es.
3. Desde la punta de la flecha de la corriente, abre un compás náutico con una medida igual a tu **Velocidad de Barco ($Vb$)**.
4. Traza un arco hasta cortar tu línea innegociable del $Ref$.
5. Une la punta de la corriente con ese corte. Traslada esa dirección al transportador de ángulos. ¡Ese es el **Rumbo Verdadero ($Rv$)** mágico al que debes poner tu proa de cangrejo!

---

## 4. Técnicas Avanzadas de Posicionamiento Costero

El Patrón de Yate no usa GPS en el examen. Usa geometría visual pura.

### Demoras Cruzadas Simultáneas
Si ves dos faros a la vez, mides su Demora de Aguja ($Da$) con tu compás de marcaciones, le aplicas la Corrección Total para sacar la Demora Verdadera ($Dv$), dibujas sus opuestas desde los faros en la carta, y donde se cruzan, estás tú.
*   **El Triángulo de Error (Somville):** Si tomas tres demoras simultáneas, rara vez se cortan en un punto por los errores de medición. Forman un triángulo. Tu posición más probable está en el interior de ese triángulo.

### Situación por Demoras No Simultáneas (El Traslado)
Solo tienes un faro visible y navegas. Tomas una demora. Navegas 2 horas y tomas otra demora al mismo faro.
1. Dibujas la 1ª Demora y la 2ª Demora.
2. Dibujas tu Rumbo y calculas las millas navegadas en esas 2 horas.
3. Escoges un punto cualquiera de la 1ª Demora, le sumas tu rumbo y distancia de esas 2 horas, y obtienes un "punto trasladado".
4. Trazas una paralela de la 1ª Demora que pase por ese punto trasladado.
5. Donde esa paralela (la "1ª Demora Trasladada") corta a la 2ª Demora original, estás tú.

### El Arco Capaz (Ángulo Horizontal)
El método más preciso y blindado a errores magnéticos (no requiere compás).
Mides con un sextante tumbado el ángulo físico que hay entre dos faros ($A$ y $B$). Ese ángulo te permite dibujar un inmenso círculo de probabilidad en el mar (Arco Capaz). Cualquier punto de ese círculo verá los dos faros bajo el mismo ángulo exacto.
Cortando el Arco Capaz con una sonda batimétrica, o con un segundo Arco Capaz de otros faros, hallas una situación perfecta sin tocar un compás magnético.
