# Radiocomunicaciones y SMSSM (GMDSS)

El **Sistema Mundial de Socorro y Seguridad Marítimos** (SMSSM, o GMDSS por sus siglas en inglés) es un conjunto internacional de procedimientos de seguridad, equipos y protocolos de comunicación diseñados para aumentar la seguridad y facilitar el rescate de embarcaciones en peligro.

Es materia obligatoria de examen para Patrón de Yate (PY) y Capitán de Yate (CY).

## Conceptos Fundamentales

El SMSSM se basa en el principio de que **cualquier buque en peligro debe poder alertar de forma automática y fiable a las autoridades de búsqueda y salvamento (SAR)** en tierra, así como a los buques cercanos.

### Las Zonas Marítimas SMSSM
El equipamiento obligatorio depende de la zona por la que se navegue:

*   **Zona A1:** Área cubierta por la cobertura radiotelefónica de al menos una estación costera VHF que dispone de alerta continua de Llamada Selectiva Digital (LSD/DSC). (Aprox. 20-30 millas de la costa).
*   **Zona A2:** Área cubierta por cobertura de estación costera en MF (Onda Media) con DSC. (Aprox. 100-150 millas). Excluye la Zona A1.
*   **Zona A3:** Área cubierta por los satélites geoestacionarios de Inmarsat (entre los 70ºN y 70ºS), excluyendo las zonas A1 y A2.
*   **Zona A4:** Zonas polares por encima de los 70ºN y 70ºS (sin cobertura Inmarsat). Requiere equipos de HF (Onda Corta).

## Equipos del SMSSM

### 1. VHF con Llamada Selectiva Digital (DSC)
El canal **70 de VHF (156.525 MHz)** está reservado exclusivamente para alertas DSC (digitales). No se puede transmitir voz en él. Al presionar el botón rojo de socorro ("Distress") durante 3-5 segundos, el equipo emite una ráfaga de datos que incluye:
*   El **MMSI** (Identidad del Servicio Móvil Marítimo, 9 dígitos) de la embarcación.
*   La **posición GPS** exacta (si está conectado).
*   La **naturaleza del peligro** (opcional, si el operador tuvo tiempo de seleccionarla en el menú).

Tras la alerta digital, se debe pasar al **Canal 16 de VHF (156.800 MHz)** para iniciar el mensaje por fonía (voz).

### 2. Radiobaliza EPIRB (COSPAS-SARSAT)
Dispositivo que emite señales en la frecuencia de **406 MHz** hacia una red de satélites en órbita polar y geoestacionaria. 
*   Transmiten la identidad del barco y la posición.
*   Disponen de un transpondedor secundario en **121.5 MHz** (frecuencia aeronáutica) para que los aviones de rescate y barcos cercanos puedan radiolocalizar físicamente la baliza ("honing").
*   Suelen contar con una **zafa hidrostática**: un mecanismo que libera la baliza automáticamente si el barco se hunde (al alcanzar los 2-4 metros de profundidad) y se activa al contacto con el agua.

### 3. Respondedor Radar (SART)
*Search and Rescue Transponder*. Cuando es interrogado por el radar de banda X (9 GHz) de un buque cercano, el SART emite una señal que se dibuja en la pantalla del radar del buque de rescate como una línea de 12 puntos dirigidos hacia la posición del náufrago o la balsa salvavidas.

### 4. NAVTEX
Receptor automático de información sobre seguridad marítima (MSI: *Maritime Safety Information*). Recibe boletines meteorológicos, avisos a los navegantes e información de socorro en formato de texto impreso o en pantalla. Transmite en **518 kHz** (internacional, en inglés) y **490 kHz** (local, idioma del país).

## Protocolos de Fonía en Emergencias (Canal 16)

Existen tres niveles de prioridad en las comunicaciones de voz:

### 1. Socorro (DISTRESS) - Peligro Inminente y Grave
Se requiere asistencia inmediata.
*   **Señal de alarma:** `MAYDAY` (repetido tres veces).
*   **Estructura del mensaje:**
    *   MAYDAY, MAYDAY, MAYDAY.
    *   Aquí la embarcación [Nombre] (3 veces), indicativo de llamada [XX], MMSI [9 dígitos].
    *   MAYDAY [Nombre del barco].
    *   Posición (Lat/Lon o demora y distancia a un punto conocido).
    *   Naturaleza del peligro (Ej: Hundiéndonos, fuego a bordo).
    *   Tipo de asistencia requerida.
    *   Número de personas a bordo (POB).
    *   Cualquier otra información útil (Ej: Abandonando barco a balsa salvavidas).
    *   Cambio.

### 2. Urgencia (URGENCY) - Peligro Potencial
Situación que afecta a la seguridad del buque o personas, pero que no justifica un mensaje de socorro inmediato (ej: fallo de motor a la deriva cerca de costa, necesidad de consejo médico).
*   **Señal de alarma:** `PAN PAN` (repetido tres veces).

### 3. Seguridad (SAFETY) - Información Crítica
Avisos meteorológicos graves, contenedores a la deriva, faros apagados.
*   **Señal de alarma:** `SECURITE` (pronunciado SÉCURITÉ, tres veces).

## Silencio de Radio
Durante un MAYDAY, el canal 16 queda **exclusivamente reservado** para la emergencia. Si otra embarcación interfiere, la estación de control (Salvamento Marítimo) puede imponer silencio absoluto diciendo:
**"SILENCE MAYDAY"** o **"SEELONCE MAYDAY"**.

Cuando la emergencia ha terminado, la autoridad costera transmite:
**"SILENCE FEENEE"** (Seelonce Fini).
