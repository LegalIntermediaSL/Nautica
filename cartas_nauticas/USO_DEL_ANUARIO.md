# El Anuario y Publicaciones Oficiales a Bordo

Navegar exige anticipación. Para poder calcular la profundidad del agua (mareas) o posicionarnos en medio del océano (astronomía), es obligatorio llevar a bordo publicaciones oficiales que predicen el comportamiento de la naturaleza. 

Dependiendo de tu zona de navegación y titulación, utilizarás el **Anuario de Mareas** o el **Almanaque Náutico**. A continuación, explicamos cómo se usan.

---

## 1. El Anuario de Mareas (IHM)

Publicado anualmente por el **Instituto Hidrográfico de la Marina (IHM)**, es el libro que te salvará de encallar al entrar en un puerto con poco calado. Contiene las predicciones de pleamares y bajamares para todos los puertos de España.

### Estructura del Anuario de Mareas
El anuario se divide en dos grandes bloques:
1.  **Puertos Patrón (Principales):** Ciudades costeras grandes (ej. Cádiz, Bilbao, Vigo). Tienen una página propia por mes con datos diarios calculados minuto a minuto.
2.  **Puertos Secundarios:** Puertos pequeños o calas. No tienen tabla propia diaria; en su lugar, el libro te da una "diferencia" (ej: $+00\text{h } 15\text{m}$, $-0.2\text{m}$) que debes sumar o restar a un Puerto Patrón de referencia.

### Cómo usar las Tablas de un Puerto Patrón
Si abres la página de tu mes y día actual, verás filas con horas y sondas (alturas).
*   **Adelanto de Hora:** ¡Atención! La hora del anuario de mareas suele venir en **Hora Oficial de Greenwich (Hz/UTC)**. En España peninsular, en invierno debes sumar +1 hora y en verano +2 horas a lo que leas en el libro para saber la hora real en tu reloj (Hora Civil del Lugar).
*   **Pleamar (PM):** La hora a la que el agua alcanza su nivel máximo y la altura en metros.
*   **Bajamar (BM):** La hora a la que el agua alcanza su nivel mínimo y la altura en metros.
*   **Coeficiente de Marea:** Un número que va del 20 al 120. Un coeficiente alto (ej: 110) significa "Mareas Vivas": el agua subirá muchísimo y bajará muchísimo, creando fuertes corrientes. Un coeficiente bajo (ej: 30) significa "Mareas Muertas": apenas habrá diferencia entre la PM y la BM.

### El Cálculo Práctico (Sonda en el Momento 'T')
Si quieres saber cuánta agua hay a una hora intermedia (ej. 14:00h, entre la PM y la BM), debes usar la tabla de mareas que viene en las últimas páginas del anuario. Entras con la Amplitud (diferencia de altura entre PM y BM) y el intervalo de tiempo transcurrido desde la última pleamar/bajamar para obtener la corrección aditiva.

### Ejemplo Numérico Resuelto: La Regla de los Doceavos

Cuando no se dispone de la tabla de corrección del anuario a mano, existe un método rápido y muy usado en los exámenes de Patrón de Yate y Capitán de Yate para estimar la altura de marea en un instante intermedio: la **Regla de los Doceavos (Rule of Twelfths)**.

**Fundamento:** se asume que la curva de marea (una sinusoide) sube o baja repartiendo la Amplitud total en 12 partes iguales ("doceavos"), distribuidas de forma no lineal a lo largo de las 6 horas que dura el ciclo BM→PM (o PM→BM), siguiendo la proporción **1 - 2 - 3 - 3 - 2 - 1** doceavos por cada hora sucesiva (la marea sube/baja despacio al principio y al final, y rápido en las horas centrales).

**Datos del problema:**
*   Bajamar (BM) a las **08:00h**, con una sonda de **1,20 m**.
*   Pleamar (PM) a las **14:00h**, con una sonda de **5,40 m**.
*   Duración BM→PM: 6 horas.
*   **Pregunta:** ¿Qué altura de marea habrá a las **12:00h**?

**Resolución paso a paso:**

1.  **Amplitud (A):** diferencia entre PM y BM.
    `A = 5,40 - 1,20 = 4,20 m`

2.  **Valor de 1 doceavo:**
    `1/12 de A = 4,20 / 12 = 0,35 m`

3.  **Reparto horario según la Regla de los Doceavos** (creciente, de BM a PM):

    | Hora | Horas desde BM | Doceavos de esa hora | Doceavos acumulados | Altura (m) |
    | :--- | :---: | :---: | :---: | :---: |
    | 08:00 (BM) | 0h | — | 0/12 | 1,20 |
    | 09:00 | 1h | 1 | 1/12 | 1,55 |
    | 10:00 | 2h | 2 | 3/12 | 2,25 |
    | 11:00 | 3h | 3 | 6/12 | 3,30 |
    | **12:00** | **4h** | **3** | **9/12** | **4,35** |
    | 13:00 | 5h | 2 | 11/12 | 5,05 |
    | 14:00 (PM) | 6h | 1 | 12/12 | 5,40 |

4.  **Cálculo directo para las 12:00h** (4 horas después de la BM, doceavos acumulados = 1+2+3+3 = 9/12):
    `Altura = Sonda BM + (doceavos acumulados × valor de 1 doceavo)`
    `Altura(12:00h) = 1,20 + (9 × 0,35) = 1,20 + 3,15 = 4,35 m`

**Resultado:** a las 12:00h habrá una altura de marea de **4,35 metros** sobre el Nivel de Reducción de Sondas. Sumando este valor a la sonda impresa en la carta en ese punto se obtiene la profundidad real de agua disponible en ese instante.

*Nota de examen:* si la duración real entre BM y PM no es exactamente de 6 horas (lo habitual, suele rondar las 6h 12min), cada intervalo de la tabla debe calcularse como Duración/6 en lugar de asumir una hora exacta, mantenimiento la misma proporción de doceavos 1-2-3-3-2-1.

---

## 2. El Almanaque Náutico (ROA)

Publicado por el **Real Instituto y Observatorio de la Armada (ROA)**, es el libro sagrado de los Capitanes de Yate (CY). Mientras que el anuario de mareas mira hacia abajo (al fondo del mar), el Almanaque Náutico mira hacia arriba (a las estrellas). 

Es obligatorio en navegaciones transoceánicas donde el GPS podría fallar. Te dice exactamente dónde está cada astro (Sol, Luna, Planetas y Estrellas) en cada segundo del año, visto desde el centro de la Tierra.

### ¿Qué datos se extraen de las "Páginas Diarias"?
Cada vez que abres el libro, ves dos páginas que cubren tres días del año (ej: 1, 2 y 3 de Marzo).

*   **Horario en Greenwich (hG):** Es la longitud celestial del astro. Te dice sobre qué meridiano de la Tierra está pasando el Sol exactamente en esa hora UTC.
*   **Declinación ($\delta$):** Es la latitud celestial del astro. Te dice en qué paralelo está el astro (ej. si el Sol está en el hemisferio Norte o Sur en esa época del año).

### Cómo se usa para situarse (Recta de Altura)
1.  **Observación:** Sales a cubierta con tu Sextante y mides la altura angular del Sol sobre el horizonte del mar, apuntando exactamente a qué hora UTC lo hiciste (con un cronómetro marino preciso al segundo).
2.  **Extracción de Datos:** Abres el Almanaque Náutico en ese día y hora exacta. Si lo hiciste a las 14:15:30 UTC, buscas la fila de las 14h, y luego vas a las "Tablas de Partes Proporcionales" (al final del libro) para sumar los minutos y segundos (15m 30s).
3.  **Resolución:** Ahora sabes la Altura Verdadera observada y las coordenadas exactas del astro. Con la fórmula de la Secante de Marcq St. Hilaire (Simulación 09), cruzas la altura observada con la altura calculada matemáticamente para obtener un "Determinante", que te permitirá trazar una línea en tu carta náutica. ¡Estás en algún punto de esa línea!

---

## Resumen Normativo a Bordo

*   **Zonas 1 y 2 (Navegación de Altura / Oceánica):** Es obligatorio llevar la publicación del Anuario de Mareas y, para Zona 1 (Vuelta al Mundo sin límites), el Almanaque Náutico y Tablas Náuticas.
*   **Zona 3 y 4 (Hasta 25 y 12 millas):** Aunque no es estrictamente obligatorio llevar el "libro de papel", como Patrón es tu deber ineludible **conocer el estado de la marea** antes de cruzar la bocana del puerto, ya sea usando apps móviles autorizadas (ej. Puertos del Estado), plotters integrados o el Anuario físico.
