# Manual de Electrónica e Instrumentación Naval

La navegación moderna ha pasado de la era del sextante de bronce a la era del cristal (Glass Cockpit). Los modernos MFD (Multi-Function Displays) unifican todas las fuentes de datos del barco en una única pantalla. Sin embargo, depender ciegamente de la electrónica sin conocer sus limitaciones es letal.

---

## 1. El Protocolo de Red: NMEA 0183 vs NMEA 2000

Los instrumentos náuticos no hablan USB o Ethernet comercial. Utilizan estándares de la *National Marine Electronics Association*.

### NMEA 0183
*   Protocolo muy antiguo (años 80), basado en comunicación serie RS-422.
*   **Problema:** Es de "un solo hablante (Talker) y varios oyentes (Listeners)". Los cables se empalman a mano, siendo una pesadilla técnica si cruzas polaridades. Transmite datos a bajísima velocidad (4800 baudios, o 38400 para AIS).
*   *Formato:* Mensajes ASCII, ej. `$GPGGA,123519,4807.038,N,01131.000,E,1...`

### NMEA 2000 (N2K)
*   Basado en el bus **CAN (Controller Area Network)** de automoción.
*   **Arquitectura:** Es un bus troncal (Backbone) del que cuelgan todos los instrumentos mediante conectores en T (Drop Cables). Es *Plug-and-Play*.
*   **Ventaja:** Todos los equipos pueden "hablar" y "escuchar" simultáneamente a $250 \text{ kbps}$. El equipo de viento habla con el piloto automático, y el GPS habla con la radio VHF al mismo tiempo por un solo cable unificado de 5 pines.
*   *Requisito de red:* El backbone debe tener una resistencia terminal ($120 \Omega$) en cada extremo y ser alimentado a 12V.

---

## 2. Sistemas GNSS (GPS, Galileo, GLONASS)

El Sistema de Posicionamiento Global no sabe dónde estás, simplemente calcula distancias.

### Principio de Funcionamiento
El receptor de a bordo es un reloj atómico sincronizado pasivo. Recibe la señal de un satélite que dice "soy el satélite A, aquí están mis efemérides (mi posición en órbita) y emití esto a las 14:00:00.0000".
El receptor anota a qué hora exacta le llegó el paquete. La diferencia de tiempo multiplicada por la velocidad de la luz da la "Pseudodistancia".
*   Cruzando 3 satélites (Trilateración), obtenemos Latitud y Longitud 2D.
*   El 4º satélite corrige el error de tiempo del reloj de cuarzo del barco, otorgando 3D Fix (Altitud).

### Fuentes de Error y DOP
*   **Dilution of Precision (DOP):** Si los satélites visibles están todos "apelotonados" en una esquina del cielo, el error trigonométrico de corte geométrico (HDOP, Horizontal DOP) se dispara. Un HDOP $\le 2$ es excelente; $\ge 5$ es dudoso.
*   **WAAS / EGNOS:** Sistemas de aumentación. Estaciones de tierra miden el retraso de la señal al cruzar la ionosfera, y envían una corrección milimétrica a los satélites geoestacionarios para que la retransmitan al barco, logrando precisión sub-métrica.

---

## 3. AIS (Sistema de Identificación Automática)

El mayor avance en prevención de colisiones (antirumbos) desde el radar.

El AIS es un transceptor VHF (emite y recibe). Utiliza el GPS integrado del barco y emite periódicamente paquetes de datos por ondas de radio VHF a los barcos circundantes.
Tu pantalla pinta los barcos como triángulos. Si pinchas en ellos verás su nombre, rumbo (COG), velocidad (SOG), MMSI, dimensiones y su **CPA (Closest Point of Approach)**.

### Clases de AIS
1.  **Clase A:** Obligatorio en buques mercantes y pasaje (> 300 GT). Emite a 12W. Tienen prioridad y emiten datos cada 2-10 segundos en función de la velocidad y cambios de rumbo.
2.  **Clase B:** Para yates y veleros. Emite a solo 2W. Emite cada 30 segundos (o menos si es SOTDMA). *Aviso:* Algunos mercantes filtran los "Clase B" de su pantalla para reducir saturación en puertos, así que no asumas que te han visto.

---

## 4. Radares Náuticos

El radar es indispensable con niebla cerrada, operando típicamente en **Banda X (9 GHz, longitud de onda 3 cm)**. Gira escaneando la bahía.

### Funcionamiento Básico
Emite un pulso electromagnético brutalmente potente (magnetrón) que rebota en los metales y el agua. La distancia del "eco" se calcula por el tiempo de vuelo de retorno del microondas.

### Tecnologías
*   **Magnetrón (Clásico):** Gran consumo eléctrico, necesita calentamiento de 90 segundos y no ve muy bien blancos pequeños muy cercanos.
*   **Solid-State / Broadband (FMCW / Doppler):** Modelos modernos sin magnetrón (como Halo o Quantum). Emiten radiación de baja potencia continuada de frecuencia modulada. Ven palos flotando a 5 metros de la proa con resolución HD, consumen muy poco, se encienden instantáneamente, y detectan por efecto Doppler si un blanco se acerca (se pinta en rojo) o se aleja (verde).

---

## 5. Sondas Acústicas (Ecosondas)

El transductor situado bajo el casco emite "pings" de ultrasonidos hacia el fondo del mar.
*   **Frecuencias:** 
    *   **200 kHz (Alta Frecuencia):** Cono de sonido estrecho ($12^\circ - 20^\circ$). Gran resolución de detalle del fondo, ideal para poca profundidad y anclajes.
    *   **50 kHz (Baja Frecuencia):** Cono ancho ($40^\circ$). Las ondas largas penetran profundo (hasta mil metros), ideal para navegación oceánica, aunque la resolución se vuelve borrosa.

### Alarmas de Calado
Todos los plotters y sondas permiten configurar el *Keel Offset* (compensación de la quilla).
*   Sonda real bajo transductor vs. Sonda absoluta (hasta flotación) vs. **Profundidad Restante bajo la orza** (la más segura para recreo). Fija siempre una alarma de "Shallow Water" sonando a $2 \text{ metros}$ de margen bajo quilla.

---

## 6. Autopiloto (Piloto Automático)

No es una simple brújula. El ordenador de rumbo moderno utiliza algoritmos de "estado sólido" de un giróscopo de 9 ejes electromecánico o láser.
A diferencia de un humano, no mira la proa. El autopiloto mide la aceleración angular y "anticipa" que una ola está empujando la popa a estribor *antes* de que el barco empiece a caer significativamente, aplicando compensación de timón micrométrica a un brazo hidráulico.

*   **Rumbo Magnético (Auto):** Navega hacia $090^\circ$ M. No tiene en cuenta la deriva de la corriente.
*   **Navegación por Waypoint (Nav / Track):** Lee los mensajes NMEA 2000 del GPS y ajusta el rumbo para "cazar" la línea imaginaria (XTE - Cross Track Error), combatiendo viento y corriente activamente.
*   **Aleteo de Viento (Wind Vane):** Conectado al anemómetro del mástil, navega manteniendo, por ejemplo, el viento constante a $40^\circ$ de la amura (esencial para largas bordadas a vela).
