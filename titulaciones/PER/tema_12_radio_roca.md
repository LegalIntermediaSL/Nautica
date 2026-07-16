# PER - Tema 12: Curso de Radiooperador de Corto Alcance (ROCA)

Para expedir tu título de PER (o de PNB), además de aprobar el examen teórico y navegar las prácticas obligatorias de motor, es **estrictamente obligatorio por ley** realizar y superar este curso práctico en una escuela homologada frente a un simulador de equipos de radiocomunicaciones de la OMI.

Este temario avanzado te prepara para dominar la cabina de radio de cualquier yate moderno.

---

## 1. El Ecosistema Mundial de Socorro (SMSSM / GMDSS)

El *Global Maritime Distress and Safety System* (GMDSS) es la gigantesca red internacional diseñada en los años 90 para garantizar que ningún barco se hunda en silencio. Su principio fundamental es la **redundancia automática**: las llamadas de auxilio deben llegar a los centros de salvamento en tierra y a todos los barcos cercanos de forma autónoma, sin depender de la voz humana.

### Las Zonas Marítimas Geográficas del GMDSS
La Tierra no se divide por paralelos, sino por la cobertura electromagnética de las antenas:
*   **Zona A1:** Cobertura ininterrumpida de las estaciones costeras (torres terrestres) operando en **VHF con DSC**. Suele alcanzar unas 20-30 millas desde la costa (línea visual). *Esta es la zona genérica de examen y atribución del PER (12-25 millas).*
*   **Zona A2:** Cobertura de las potentes estaciones costeras de Onda Media (MF) con DSC. Llega hasta unas 150 millas (ideal para cruces a Baleares o Canarias).
*   **Zona A3:** Cobertura satelital geoestacionaria de la red INMARSAT (cubre todo el globo terrestre desde la latitud $70^\circ N$ a $70^\circ S$).
*   **Zona A4:** Zonas polares remotas (los satélites no llegan bien), cubiertas solo por la ruidosa radio de Onda Corta (HF) que rebota en la ionosfera.

## 2. La Emisora VHF y el Módem LSD (Canal 70)

El transceptor VHF (Very High Frequency) es el pulmón del barco. Es obligatorio en Zona 4, y emite en FM marina (frecuencias de 156 MHz a 174 MHz). Funciona por **propagación directa (línea de visión)**: la onda de radio viaja en línea recta y se estrella contra la curvatura del planeta o las montañas. Por eso la antena debe ir instalada en la punta del mástil más alto posible (cuanto más alta la antena, más lejos llega la onda).

### 2.1 El Canal 16 Fonía (156.800 MHz)
Es el canal internacional de voz para **Socorro, Urgencia, Seguridad y Llamada Inicial**.
*   **Silencio Radio Obligatorio:** Durante los primeros 3 minutos de cada media hora (ej: 10:00 a 10:03, y 10:30 a 10:33) hay que guardar mutismo total. Es el momento en el que el Centro de Salvamento pega la oreja al altavoz para escuchar a náufragos con baterías bajas.
*   **Uso:** Sirve solo para llamar a otro barco o a la costera y decirle: *"Yate Fortuna, Yate Fortuna, soy el Yate Brisa. Pasamos a trabajar al Canal 06"*. **Jamás se mantiene una conversación en el Canal 16.**

### 2.2 Llamada Selectiva Digital (LSD / DSC) y el Canal 70
Todas las radios modernas integran un módem digital acoplado a un GPS. Este sistema envía "WhatsApp náuticos" codificados en el **Canal 70**. 
*(¡ATENCIÓN! Está prohibidísimo coger el micrófono y hablar por voz en el Canal 70).*

La radio tiene un **Botón rojo protegido por una tapa plástica**. Si sufres un peligro inminente y letal:
1. Levantas la tapa.
2. Pulsas el botón DISTRESS sin soltarlo durante 5 segundos (la radio pitará y contará marcha atrás).
3. La radio dispara en el Canal 70 un paquete de datos hiper-comprimido, que será captado instantáneamente por los centros de Salvamento de la costa y por todos los radares y radios de los mercantes en 30 millas a la redonda, disparando una alarma atronadora en sus puentes de mando.
4. Ese paquete transmite mágicamente tu **MMSI** (Número de identidad de 9 cifras de tu barco, tu matrícula electrónica), tus **Coordenadas GPS exactas**, la Hora Universal UTC y la Naturaleza del Peligro (si tuviste tiempo de seleccionarla en la pantalla de cristal líquido).

## 3. Jerga y Protocolos de Fonía en Emergencias

Una vez se ha mandado el DSC en el Canal 70, hay que coger el micrófono del VHF, pasarlo al Canal 16, y dar la cara explicando por voz qué pasa. Los mensajes tienen prioridad estricta:

1.  **Prioridad 1 (Socorro Letal): "MAYDAY, MAYDAY, MAYDAY"**
    *   *Uso:* Peligro grave e inminente (Hundimiento, fuego sin control, infarto a bordo).
    *   *Señal:* *"Mayday, Mayday, Mayday, aquí Yate Tritón, MMSI xxx. Posición xxx. Tenemos vía de agua incontrolable, nos hundimos. Solicito asistencia inmediata. 4 personas a bordo. Cambio."*
2.  **Prioridad 2 (Urgencia): "PAN-PAN, PAN-PAN, PAN-PAN"**
    *   *Uso:* Seguridad del barco comprometida o herido a bordo que requiere atención pero sin muerte inminente (Motor gripado a la deriva sin rocas cerca, brazo roto).
3.  **Prioridad 3 (Seguridad): "SECURITÉ, SECURITÉ, SECURITÉ"**
    *   *Uso:* Avisos generales a la navegación (Troncos grandes flotando, temporal inminente, faros apagados). Lo suelen usar los mercantes y Salvamento Marítimo.

## 4. Baterías y Dispositivos de Supervivencia Automáticos

El GMDSS exige que la cabina de radio siga emitiendo aunque el barco se quede a oscuras. Las radios están conectadas a una **batería independiente de servicios (o de radio)**, separada de la batería de arranque del motor.
*   **Voltaje crítico:** Una batería de Plomo-Ácido sana a motor parado debe marcar unos 12.6V - 12.8V. Si baja por debajo de 11.5V, la batería está frita y el VHF no tendrá amperaje para emitir a su potencia máxima (25 W), reduciéndose a la potencia baja local (1 W).

### Radiobaliza EPIRB (Emergency Position Indicating Radio Beacon)
Si el barco zozobra brutalmente y no da tiempo a usar la radio VHF:
*   Va montada en el exterior (junto a la balsa). Lleva una **Zafa Hidrostática** (un muelle y una cuchilla sensible a la presión).
*   Si el barco se hunde a 4 metros, la presión revienta la zafa, y el cilindro amarillo de la EPIRB sale flotando a la superficie como un cocho.
*   Al tocar el agua del mar, unos sensores de humedad la encienden solita. Empieza a emitir a los **satélites polares a 406 MHz**, enviando el MMSI y tu posición satelital directamente al cuartel de Salvamento Marítimo. Batería mínima garantizada: 48 horas parpadeando en la mar brava.
