# PER - Tema 12: Física y Operación de Radiocomunicaciones (ROCA)

Para expedir tu título de PER (o de PNB), además de aprobar el examen teórico y navegar las prácticas, es **estrictamente obligatorio por ley** superar el curso de Radiooperador de Corto Alcance (ROCA). Esta formación te prepara para operar de forma responsable la cabina de comunicaciones de un yate basándose en los principios de la radiación electromagnética y los protocolos de la OMI.

---

## 1. El Ecosistema GMDSS y Propagación de Ondas

El *Global Maritime Distress and Safety System* (GMDSS) es una arquitectura automatizada de auxilio global. Su eficacia se cimienta en las propiedades físicas de las ondas de radio y la ionosfera, definiendo las zonas marítimas en función del comportamiento de la propagación electromagnética (frecuencia, refracción atmosférica, refracción ionosférica y pérdida de espacio libre).

### Zonas Marítimas Geográficas
*   **Zona A1:** Cobertura de las ondas métricas en la banda VHF (30 MHz - 300 MHz). La propagación es puramente por **onda espacial (línea de visión)**. Las ondas VHF penetran la ionosfera y no rebotan; viajan rectilíneas. Su alcance $d$ depende geométricamente del radio de curvatura terrestre y la altura de las antenas, modulado por un ligero factor de refracción atmosférica ($K \approx 1.33$):
    $$ d (\text{millas}) \approx 2,22 \left( \sqrt{h_{\text{transmisor}}} + \sqrt{h_{\text{receptor}}} \right) $$
    *(Donde $h$ está en metros. Usualmente confinado a 20-30 millas).*
*   **Zona A2:** Cobertura de las bandas MF (Onda Media, 300 kHz - 3 MHz). Aquí actúa la propagación por **onda de superficie (ground wave)**, que por difracción viaja pegada a la conductividad salina del mar, alcanzando unas 150-400 millas sin importar si es de día o noche.
*   **Zona A3:** Cobertura vía enlaces de microondas con satélites Inmarsat geoestacionarios (Latitudes $70^\circ N$ a $70^\circ S$).
*   **Zona A4:** Zonas polares. Fuera del campo de los geoestacionarios, se requiere HF (Onda Corta, 3 MHz - 30 MHz). Las ondas rebotan en las capas F1 y F2 de la ionosfera excitada por los rayos solares (**onda ionosférica** o *skywave*), permitiendo comunicaciones transoceánicas gracias a múltiples saltos, aunque sometidas a la atenuación de la capa D diurna y desvanecimientos (*fading*).

## 2. El Transceptor VHF y el Estándar DSC (Canal 70)

El VHF (Very High Frequency) naval opera en Modulación de Frecuencia (FM) o Modulación de Fase (PM) dentro del espectro 156.000 MHz a 174.000 MHz. A diferencia del AM, la FM proporciona excelente relación señal/ruido e inmunidad a la interferencia por descargas eléctricas.

### 2.1 Fonía: Canal 16 (156.800 MHz)
Es la frecuencia de guardia internacional prioritaria.
*   **Silencio Radio:** Exigido por protocolo en los minutos del $00 \rightarrow 03$ y del $30 \rightarrow 33$ de cada hora para facilitar la escucha de señales débiles.
*   **Potencia de Emisión:** Las radios tienen salidas de impedancia a 50 ohmios. Se operan típicamente a máxima potencia para socorro ($25 \text{ W}$, High Power), atenuando por exigencia legal a ($1 \text{ W}$, Low Power) para maniobras en el interior de puertos (Canales 9, 12, etc.) para evitar el cegado del receptor por saturación de radiofrecuencia (RF).

### 2.2 Módem DSC / LSD: Canal 70 (156.525 MHz)
Las telecomunicaciones modernas usan *Llamada Selectiva Digital* (Digital Selective Calling). Se codifica un flujo de datos binarios usando FSK (Frequency Shift Keying) a una tasa de 1200 baudios, insertando corrección de errores (FEC - Forward Error Correction).
*   Al pulsar el botón **DISTRESS**, la ráfaga DSC transmite automáticamente:
    *   Tu **MMSI** (Identificación de 9 cifras programada en ROM).
    *   Coordenadas de lat/lon precisas (proporcionadas vía NMEA 0183 / NMEA 2000 desde el GPS).
    *   Formato de socorro y timestamp UTC.
    *   La radio sintoniza automáticamente ambos (buque y costera) en el Canal 16 a la espera del seguimiento por fonía.

## 3. Jerga y Protocolos de Modulación de Voz

Al pasar al Canal 16, la comunicación en banda base de voz (aproximadamente $300 \text{ Hz} - 3000 \text{ Hz}$) exige un estricto protocolo legal para economizar el tiempo en el aire:

1.  **Prioridad 1 (Socorro - Vida en Peligro Letal): "MAYDAY, MAYDAY, MAYDAY"**
    *   Se pronuncia la palabra clave tres veces (del francés *venez m'aider*).
    *   Estructura: *Mayday x3. Aquí [Nombre del buque] x3, MMSI. Mayday [Nombre], MMSI. Posición por lat/lon o demora a costa. Naturaleza (fuego, explosión, sumersión). Número de personas y tipo de auxilio.*
2.  **Prioridad 2 (Urgencia): "PAN-PAN, PAN-PAN, PAN-PAN"**
    *   Buque a la deriva por fallo mecánico pero estanco, hombre al agua en rescate activo sin ahogo, asistencia médica a bordo.
3.  **Prioridad 3 (Seguridad): "SECURITÉ, SECURITÉ, SECURITÉ"**
    *   Para retransmitir la presencia de objetos flotantes letales a 25 nudos (UFOs), cetáceos, temporales u obstrucción de señales de balizamiento marítimo.

## 4. Hardware de Supervivencia: EPIRB y SART

### EPIRB (Radiobaliza)
El GMDSS exige hardware que sobreviva al fallo total de tensión general de corriente continua de a bordo:
*   Módulo estanco operando a **406 MHz**. Emite pulsos modulados digitalmente que portan MMSI y coordenadas al sistema global satelital **COSPAS-SARSAT**.
*   Simultáneamente activa un oscilador de bajísima potencia a **121.5 MHz** para usar *radiogoniometría (homing)* por parte de los helicópteros SAR durante el último kilómetro de aproximación.
*   Zafa Hidrostática: Un diafragma de presión de fluido tarado que, al descender el buque 4 metros bajo el nivel del mar ($\sim 0.4 \text{ bar}$ de presión hidrostática), libera un muelle percutor y corta el perno, lanzando el dispositivo a flote.

### Respondedor Radar (SART)
Transpondedor activo de Radar operando en la banda X ($9.2 - 9.5 \text{ GHz}$). Cuando es barrido por el haz magnético pulsante del radar de un carguero mercante, la antena receptora del SART genera un trigger (disparo) que excita su oscilador Gunn interno y responde emitiendo una ráfaga modulada en frecuencia. Esta se pinta en la pantalla CRT/LCD del barco de rescate como una línea recta de 12 puntos intensos indicando la demora exacta al naufragio.
