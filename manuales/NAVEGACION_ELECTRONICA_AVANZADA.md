# Navegación Electrónica Avanzada e Integración

La navegación electrónica ha pasado de ser una ayuda complementaria a convertirse en el núcleo del gobierno de cualquier embarcación moderna. Comprender cómo se comunican los equipos entre sí es vital para diagnosticar fallos y exprimir al máximo sus capacidades.

## 1. Protocolos de Comunicación NMEA

La NMEA (National Marine Electronics Association) define los estándares para que equipos de diferentes fabricantes (Garmin, Raymarine, B&G, Furuno, etc.) puedan hablar el mismo idioma.

### NMEA 0183
Es el estándar antiguo (creado en los años 80), pero que aún está muy presente.
*   **Funcionamiento:** Comunicación en serie (como el antiguo RS-232 o RS-422). Transmite datos a baja velocidad (4800 baudios estándar, o 38400 baudios para AIS de alta velocidad).
*   **Arquitectura:** Un transmisor ("Talker") puede enviar datos a varios receptores ("Listeners"), pero un receptor solo puede escuchar a un transmisor en cada puerto (arquitectura de un solo sentido o *daisy chain* simple).
*   **Problema común:** Para conectar múltiples "Talkers" (ej. GPS, Anemómetro y AIS) a un solo plotter, se requiere un equipo intermedio llamado **Multiplexor**.

### NMEA 2000 (N2K)
Es el estándar moderno, basado en la tecnología CAN Bus (Controller Area Network) utilizada en automoción.
*   **Funcionamiento:** Red de alta velocidad (250 kbps). Todos los equipos se conectan a un cable troncal principal (Backbone) mediante cables de derivación (Drop cables).
*   **Arquitectura:** Bidireccional y "Plug & Play". Cualquier equipo en la red puede hablar y escuchar a cualquier otro equipo simultáneamente.
*   **Alimentación:** La propia red transporta corriente (12V) para alimentar sensores pequeños (antenas GPS, anemómetros).
*   **Terminadores:** Requiere obligatoriamente un resistor de 120 ohmios en cada extremo del Backbone para evitar el rebote de la señal de datos.

## 2. El AIS (Automatic Identification System)

El AIS ha supuesto la mayor revolución en seguridad marítima desde la invención del radar. Utiliza dos canales de VHF dedicados (87B y 88B) para transmitir y recibir la posición, rumbo y velocidad de los buques cercanos.

### Tipos de AIS
*   **Clase A:** Obligatorio para buques comerciales. Transmite con mayor potencia (12.5W), con mayor frecuencia (hasta cada 2 segundos) y requiere integración directa con el girocompás.
*   **Clase B:** Diseñado para embarcaciones de recreo. Transmite con menor potencia (2W o 5W en Clase B/SO), con menor frecuencia (cada 30 segundos) y es "educado" (solo transmite si el canal está libre, cediendo siempre prioridad al Clase A).
*   **Receptor puro:** Solo escucha. Muy común en recreo básico, pero no hace visible a la embarcación propia.

### Integración Táctica del AIS
*   **CPA (Closest Point of Approach) / TCPA (Time to CPA):** El plotter calcula matemáticamente dónde y cuándo se producirá el máximo acercamiento entre tú y el otro barco. Si el CPA es cercano a cero, hay riesgo inminente de colisión.
*   **AIS SART y MOB:** Las balizas personales AIS-MOB de los chalecos salvavidas emiten una alerta que se muestra directamente en el plotter de nuestro barco (y de los de alrededor), facilitando enormemente la recuperación de un hombre al agua.

## 3. Multiplexores WiFi y Navegación con Tablets

Muchos patrones utilizan tablets (iPad, Android) o teléfonos como plotters principales o secundarios. Aplicaciones como **Navionics, OpenCPN, Orca o Aqua Map** ofrecen cartografía actualizada a un coste muy inferior al de un MFD (Multi Function Display) marino tradicional.

Para que la tablet tenga información real del barco (viento, profundidad, AIS):
1.  Se instala un **Multiplexor WiFi** (ej. Yakker, Roam, Shipmodul) conectado a la red NMEA 0183 o N2K.
2.  El multiplexor crea una red WiFi local.
3.  La tablet se conecta a ese WiFi y recibe, vía UDP o TCP, todas las sentencias (las "frases" NMEA) que circulan por la red del barco, integrándolas en la app de navegación.

## 4. Radares de Banda Ancha (Broadband / Estado Sólido)

A diferencia del radar tradicional de magnetrón (que emite pulsos de microondas de alta potencia y requiere tiempo de calentamiento), el radar de estado sólido (FMCW):
*   Emite continuamente a muy baja potencia.
*   Tiene un calentamiento instantáneo (ideal para encenderlo rápido en un banco de niebla repentino).
*   Ofrece una resolución asombrosamente nítida a corta distancia (incluso a menos de 10 metros), lo que lo hace perfecto para navegar en rías, canales o entrar a puerto con niebla cerrada, situación donde un radar de magnetrón clásico "cegaría" la pantalla por el ruido cercano (bang inicial).
*   Consume muchísima menos energía, vital para veleros en travesía.
