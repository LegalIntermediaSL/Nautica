# PER - Tema 8: Emergencias en la Mar (Protocolos SAR Avanzados, GMDSS y Termodinámica)

Las emergencias marítimas combinan un medio hostil (el agua salada a baja temperatura) y el aislamiento de servicios de emergencia. Un Patrón de Yate asume legal y moralmente la labor de *Coordinador de Escena (OSC)* en un naufragio.

---

## 1. Hombre al Agua (MOB - Man Overboard) y Maniobras Cinemáticas

Un MOB es una crisis contrarreloj. En aguas frías, el tiempo de supervivencia viene dado por la Ley del Enfriamiento de Newton para la hipotermia severa:

$$ T(t) = T_a + (T_0 - T_a)e^{-kt} $$

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

$$ v = \sqrt{2gh} $$

El caudal de inundación será $ Q = v \cdot Area $. Una grieta a 1.5 metros de profundidad puede inyectar cientos de litros por segundo, superando a las bombas eléctricas instantáneamente.
**Protocolo:**
1.  Encender motores (para dotar de amperaje infinito a las bombas de sentina).
2.  Machetear espiches cónicos de madera en pasacascos reventados, que se hinchan por capilaridad.
3.  Pre-estiba del *Grab Bag* (documentación, VHF pórtatil resistente al agua IPX8 y agua).
4.  Orden de abandono solo si la borda entra bajo el agua.
