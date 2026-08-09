# Comunicaciones Satelitales y GMDSS

La era moderna ha transformado drásticamente las comunicaciones oceánicas. Ya no dependemos exclusivamente de la incierta propagación ionosférica de las Radios BLU (SSB), sino que contamos con redes de internet de banda ancha globales y sistemas de socorro instantáneos, bajo el amparo del **GMDSS** (Global Maritime Distress and Safety System).

> [!WARNING]
> Aviso Legal: Toda la información contenida en este repositorio se suministra "tal cual" (as is) y tiene una finalidad única y exclusivamente educativa. La información contenida en este repositorio ha sido recopilada de diversas fuentes, entre ellas internet, no se garantiza la exactitud ni fiabilidad de ella. El autor, los colaboradores y la empresa Legal Intermedia declinan expresamente cualquier responsabilidad frente a posibles errores, omisiones, daños materiales, lesiones, accidentes o sanciones legales que pudieran derivarse, directa o indirectamente, del uso o interpretación de la información contenida en este repositorio o sus simulaciones.

## 1. El Ecosistema GMDSS (SMSSM en español)

El GMDSS es un sistema mundial que garantiza que ninguna embarcación, en ninguna parte del globo, pueda desaparecer sin dejar rastro (en teoría) al automatizar y redundar las alertas de socorro.

### Componentes Clave:
*   **VHF con DSC (Digital Selective Calling):** Presionando un simple botón rojo protegido, la radio transmite digitalmente la identidad del buque (MMSI), sus coordenadas GPS y la naturaleza del peligro a todos los barcos en 30-50 millas a la redonda y estaciones costeras. Funciona de barco a barco y de barco a costa.
*   **EPIRB (Radiobaliza de Localización de Siniestros):** Un dispositivo que, al activarse manual o automáticamente por inmersión, emite en 406 MHz hacia los satélites Cospas-Sarsat. Transmite el MMSI y posición GPS directa a los centros de coordinación de salvamento (MRCC).
*   **SART (Transpondedor de Búsqueda y Rescate):** Emite una señal cuando es "barrido" por el radar de banda X de un barco o avión de rescate, dibujando puntos concéntricos en su pantalla para guiar la aproximación final a la balsa salvavidas.
*   **Navtex:** Receptor que imprime o muestra en pantalla alertas meteorológicas, avisos a navegantes e información de seguridad marítima (MSI) de forma automática.

## 2. Satélites Clásicos: Inmarsat e Iridium

Hasta la llegada del internet de baja órbita (LEO), la navegación se apoyaba en dos grandes pilares:

### Inmarsat (Red Geoestacionaria)
*   **Pros:** Cobertura estable y sistemas integrados directamente en GMDSS (Inmarsat-C). Fiabilidad extrema.
*   **Contras:** Velocidad de datos extremadamente lenta (y carísima) para los estándares modernos. Los satélites geoestacionarios (sobre el ecuador) no dan cobertura en los polos.

### Iridium (Red de Órbita Baja - LEO)
*   **Pros:** Cobertura verdaderamente global (incluyendo polos). Sistemas portátiles (teléfonos satelitales) y dispositivos como Iridium GO! que permiten mandar emails, descargar GRIBs meteo y llamadas de voz en cualquier océano.
*   **Contras:** Datos lentos comparados con VSAT o Starlink. Costes elevados por suscripción.

## 3. La Revolución: Starlink Maritime

La constelación Starlink de SpaceX (Línea Maritime o Roam) ha supuesto un cambio de paradigma en la navegación de recreo oceánica, llevando la banda ancha al medio del Pacífico.

### Ventajas (Game Changer):
*   **Ancho de banda ilimitado y barato:** Permite ver Netflix, hacer videollamadas con médicos, teletrabajar o descargar modelos meteorológicos masivos en segundos.
*   **Seguridad:** Poder consultar vídeos de reparaciones de motores o compartir imágenes con técnicos de tierra salva vidas.

### Peligros de Depender Únicamente de Starlink:
> [!CAUTION]
> **Starlink NO es GMDSS.** Es un servicio comercial de internet. Si hay un apagón del sistema, corte de luz en el barco o fallan sus componentes móviles/antenas, te quedarás aislado. Nunca se debe confiar en Starlink como sistema principal de socorro. Debe usarse en conjunto con una EPIRB certificada, teléfono satelital o VHF DSC. Además, consume una cantidad significativa de energía eléctrica comparado con Iridium GO!, lo cual es crítico si fallan los generadores.
