# PER - Tema 8: Emergencias en la Mar (Protocolos SAR Avanzados, GMDSS y Termodinámica)

Las emergencias marítimas combinan un medio hostil (el agua salada a baja temperatura) y el aislamiento de servicios de emergencia. Un Patrón de Yate asume legal y moralmente la labor de *Coordinador de Escena (OSC)* en un naufragio.

---

## 1. Hombre al Agua (MOB - Man Overboard) y Maniobras Cinemáticas

Un MOB es una crisis contrarreloj. En aguas frías, el tiempo de supervivencia viene dado por la Ley del Enfriamiento de Newton para la hipotermia severa:

$$
T(t) = T_a + (T_0 - T_a)e^{-kt}
$$

Donde la transferencia de calor en el agua es 25 veces superior que en el aire. El colapso cardíaco o ahogamiento reflejo ocurre en menos de 20 minutos en aguas por debajo de 10ºC.

### Procedimiento de Crisis Inicial
1.  **Gritar y señalar:** "MOB Estribor!". Lanzar el aro salvavidas con luz automática y rabiza.
2.  **Apartar la hélice:** Timón metido *violentamente hacia la banda de caída* para que la popa derrape alejándose del náufrago.
3.  **Marcación GMDSS/GPS:** Pulsar el botón **MOB** (Man Overboard) en el Plotter para fijar las coordenadas GPS instantáneas y emitir llamada selectiva digital si procede.
4.  **Vigía Humano (Dead Reckoning):** Alguien debe apuntar ininterrumpidamente sin parpadear.

### Curvas de Búsqueda y Recuperación
*   **Curva de Boutakov (Williamson Turn):** Garantiza volver sobre la propia estela.
    1.  Caer 60º a la banda de caída.
    2.  Meter timón opuesto a fondo.
    3.  Acuartelar rumbo recíproco ($R_0 \pm 180^\circ$).
*   **Curva de Scharnow:** Para rescates donde el MOB lleva tiempo en el agua y ha quedado muy atrás de la popa. Se cae 240º y luego rumbo opuesto.

---

## 2. Operaciones SAR (Search and Rescue) y GMDSS

El GMDSS (Global Maritime Distress and Safety System) elimina el factor humano de escuchar radios estáticas, usando telemetría.
*   **DSC (Digital Selective Calling):** Canal 70 VHF. Envía una ráfaga de módem digital inaudible a todas las estaciones costeras en 20 millas, inyectando tu número MMSI (9 dígitos identificativos) y tus coordenadas GPS exactas, además del tipo de emergencia ("Sinking", "Fire", "MOB").
*   **Radiobaliza EPIRB (406 MHz):** Al flotar libre y mojarse, transmite al satélite COSPAS-SARSAT. El satélite usa la desviación Doppler de la señal (Efecto Doppler) para calcular matemáticamente la latitud y longitud antes de retransmitir al MRCC (Centro Coordinador de Salvamento).
*   **Respondedor de Radar SART (9 GHz):** Pinta una línea de 12 puntos en las pantallas de radar de todos los buques de la zona (en Banda X, 3 cm).

### Patrones de Búsqueda Aérea y Marítima (IAMSAR)
*   *Sector Search (Búsqueda por Sectores):* Patrón de estrella de 3 puntas, cruzando el "Datum" (punto cero) continuamente, útil para hombre al agua localizado.
*   *Expanding Square (Cuadrado Expansivo):* Espiral rectangular con tramos que crecen $d, d, 2d, 2d, 3d, 3d...$, barriendo una gran área asumiendo deriva.

---

## 3. Lucha contra Incendios: Termodinámica y Control

El fuego es una oxidación exotérmica súbita (Pirólisis).
*   **Clase A (Sólidos):** Requiere ENFRIAMIENTO (bajar energía de activación con Agua).
*   **Clase B (Líquidos):** Hidrocarburos. Requiere SOFOCACIÓN (corte de $O_2$ con Espuma AFFF o Polvo). ¡El agua vaporizada explota al tocar aceite hirviendo!
*   **Clase E (Eléctrico):** Usar gas CO2 puro por su naturaleza dieléctrica, que elimina el oxígeno e inhibe la electrocución.

---

## 4. Inundación y Control de Daños (Dinámica de Hundimiento)

Una grieta bajo la línea de flotación no gotea, *escupe agua a presión* según el Teorema de Torricelli. La velocidad de entrada de agua $v$ depende de la presión de la columna de agua $h$ sobre la grieta y la gravedad $g$:

$$
v = \sqrt{2gh}
$$

El caudal de inundación será $ Q = v \cdot Area $. Una grieta a 1.5 metros de profundidad puede inyectar cientos de litros por segundo, superando a las bombas eléctricas instantáneamente.
**Protocolo:**
1.  Encender motores (para dotar de amperaje infinito a las bombas de sentina).
2.  Machetear espiches cónicos de madera en pasacascos reventados, que se hinchan por capilaridad.
3.  Pre-estiba del *Grab Bag* (documentación, VHF pórtatil resistente al agua IPX8 y agua).
4.  Orden de abandono solo si la borda entra bajo el agua.

## Ejemplos Prácticos

**Problema 1: Ecuación de Enfriamiento de Newton en un MOB**
Un tripulante cae por la borda en las frías aguas del Mar Cantábrico en invierno, donde la temperatura del agua es constante a $T_a = 12^\circ\text{C}$. La temperatura corporal inicial del tripulante en su núcleo es $T_0 = 37^\circ\text{C}$. Las observaciones médicas navales han determinado empíricamente que para un humano de complexión media con ropa normal saturada de agua salada, la constante de transferencia de calor es $k = 0.045 \text{ min}^{-1}$.

La hipotermia clínica grave con fibrilación ventricular inminente y pérdida de conciencia ocurre cuando la temperatura central desciende a $T_c = 28^\circ\text{C}$. Calcule el tiempo crítico ($t$) del que dispone el equipo de rescate antes de llegar a este estado letal.

*Resolución:*
Usamos la Ley del Enfriamiento de Newton:

$$
T(t) = T_a + (T_0 - T_a)e^{-kt}
$$

Sustituyendo los valores conocidos:

$$
28 = 12 + (37 - 12)e^{-0.045t}
$$

$$
28 = 12 + 25 e^{-0.045t}
$$

Despejamos la exponencial:

$$
16 = 25 e^{-0.045t}
$$

$$
e^{-0.045t} = \frac{16}{25} = 0.64
$$

Aplicamos logaritmo neperiano a ambos lados:

$$
\ln(0.64) = -0.045t
$$

$$
-0.44628 = -0.045t
$$

$$
t = \frac{0.44628}{0.045} \approx 9.91 \text{ minutos}
$$

El tripulante dispone de **menos de 10 minutos** antes de alcanzar la hipotermia severa, demostrando la extrema urgencia de aplicar el botón MOB y la maniobra de Williamson inmediatamente.

**Problema 2: Dinámica de Hundimiento (Teorema de Torricelli)**
Tras una colisión con un OFNI (Objeto Flotante No Identificado), se produce un desgarro en la obra viva del yate. La brecha tiene un área efectiva de $A = 0.02 \text{ m}^2$ (aprox. 14x14 cm) y está situada a una profundidad de $h = 1.2 \text{ m}$ bajo la línea de flotación. Considere la aceleración de la gravedad $g = 9.81 \text{ m/s}^2$ y asuma un coeficiente de descarga para un orificio irregular $C_d = 0.65$.

Calcule la velocidad de ingreso del agua ($v$) y el caudal masivo ($Q$) en litros por minuto.

*Resolución:*
Aplicamos el Teorema de Torricelli con el coeficiente de descarga:

$$
v = C_d \sqrt{2gh}
$$

$$
v = 0.65 \sqrt{2 \times 9.81 \times 1.2}
$$

$$
v = 0.65 \sqrt{23.544} \approx 0.65 \times 4.852 \approx 3.15 \text{ m/s}
$$

Calculamos el caudal volumétrico:

$$
Q = v \times A = 3.15 \text{ m/s} \times 0.02 \text{ m}^2 = 0.063 \text{ m}^3\text{/s}
$$

Convertimos a litros por minuto:

$$
0.063 \text{ m}^3\text{/s} = 63 \text{ litros/s}
$$

$$
Q = 63 \times 60 = 3780 \text{ litros/minuto}
$$

Una bomba de sentina eléctrica comercial de alta capacidad puede evacuar típicamente unos 100-150 litros/minuto. La tasa de ingreso es unas 25 veces superior a la capacidad máxima de achique, haciendo obligatoria la obturación de la brecha desde el exterior mediante un espiche o vela de colisión, y justificando la activación del EPIRB/DSC inmediatamente.

## Referencias Bibliográficas y Jurisprudencia

*   **Convenios Internacionales y Manuales:**
    *   *IAMSAR Manual (International Aeronautical and Maritime Search and Rescue Manual)*. Publicado conjuntamente por OMI y OACI. Referencia absoluta para patrones de búsqueda y coordinación OSC.
    *   *GMDSS Master Plan*, OMI. Normativa sobre operación, telemetría y alcance de la llamada selectiva digital, EPIRB y SART.
*   **Textos Técnicos Médicos y Termodinámicos:**
    *   *Hypothermia, Frostbite, and Other Cold Injuries*, Giesbrecht & Wilkerson. Referencia clínica sobre enfriamiento convectivo en agua y colapso cardiovascular.
    *   *Fluid Mechanics*, Frank M. White. Análisis de hidrodinámica clásica, Teorema de Torricelli aplicado a perfiles irregulares de fractura.
*   **Jurisprudencia de Almirantazgo:**
    *   *The "Marques" Inquiry (1984)*: Investigación oficial sobre el hundimiento que redefinió los estándares legales en evacuación en mar abierta y la obligatoriedad del equipo EPIRB automático flotante libre y zafas hidrostáticas.
    *   *Hooper v. M/T African Comet (1993)*: Jurisprudencia sobre la obligación moral y legal del capitán actuando como On-Scene Coordinator, confirmando la responsabilidad por abandono negligente de maniobras de búsqueda (Man Overboard Williamson Turn failure).
