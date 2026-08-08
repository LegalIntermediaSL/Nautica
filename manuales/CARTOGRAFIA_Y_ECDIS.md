# Cartografía Electrónica y Sistemas ECDIS

La transición del papel a la electrónica ha revolucionado la navegación marítima. Sin embargo, no todos los sistemas electrónicos de cartas (ECS) son equivalentes. Para buques regulados por el convenio SOLAS, se exige un nivel de rigor técnico y legal muy estricto: el **ECDIS** (Electronic Chart Display and Information System).

## 1. Diferencia entre ECS y ECDIS

*   **ECS (Electronic Chart System):** Término genérico para cualquier sistema electrónico de visualización de cartas (ej. plotters comerciales, Navionics en una tablet). Puede usar cartografía no oficial (privada). **No** sustituye legalmente a la carta de papel para la navegación profesional regulada.
*   **ECDIS:** Un equipo informático de navegación específico, certificado por la OMI (Organización Marítima Internacional), que cumple con rigurosas normas de rendimiento y fiabilidad. Cuando un ECDIS utiliza Cartas Electrónicas de Navegación Oficiales (ENC) y cuenta con un sistema de respaldo adecuado, **tiene la misma validez legal que la carta de papel** bajo el convenio SOLAS.

## 2. Tipos de Cartas Electrónicas

### Raster Navigational Charts (RNC)
Son básicamente **fotocopias digitales** (escaneos de alta resolución) de las cartas de papel oficiales.
*   **Ventajas:** Exactamente el mismo aspecto que la carta de papel, el navegante está familiarizado con los símbolos.
*   **Desventajas:** Es una "imagen plana". El ordenador no sabe qué es un faro, un veril o una boya; solo ve píxeles. No se pueden configurar alarmas automáticas de profundidad basadas en la carta. Al hacer zoom, la imagen se pixela. Si se usa cartografía RNC en un ECDIS, el sistema funciona en modo RCDS (Raster Chart Display System), y **requiere llevar la cartera de papel correspondiente** como apoyo.

### Electronic Navigational Charts (ENC / Vectoriales)
Son bases de datos digitales. Cada elemento (faro, boya, línea de costa, veril) es un objeto informático (vector) con atributos asociados (color de la luz, altura, naturaleza del fondo).
*   **Ventajas:**
    *   **Inteligencia:** El sistema "entiende" los datos. Puede hacer sonar una alarma si la derrota planificada cruza un veril de seguridad o un área restringida.
    *   **Escalabilidad:** Al hacer zoom, los símbolos no se distorsionan, y se revela más o menos detalle según la escala seleccionada de forma dinámica.
    *   **Personalización:** El usuario puede ocultar información no relevante (ej. apagar sondas profundas) para desembarazar la pantalla (decluttering).
*   **Desventajas:** El aspecto puede ser muy distinto al papel tradicional (Simbología IHO S-52).
*   Las ENC oficiales, producidas por oficinas hidrográficas gubernamentales bajo las normas IHO S-57 y S-63 (encriptación), son el núcleo del sistema ECDIS.

## 3. Funciones Clave del ECDIS

*   **Monitorización de la Derrota:** Integra el GPS, Girocompás y Corredera sobre la carta vectorial, mostrando la posición real del buque y su vector de velocidad/rumbo.
*   **Gestión de Alarmas:** Genera alertas automáticas (Safety Contour, Safety Depth) si el barco se dirige hacia aguas poco profundas o áreas peligrosas.
*   **Superposición (Overlay):** Permite superponer la imagen del Radar/ARPA o del AIS directamente sobre la carta para comparar inmediatamente el entorno electrónico con el cartográfico.
*   **Planificación de Rutas (Route Planning):** Comprueba automáticamente (Route Check) si la ruta propuesta atraviesa algún peligro en todo su recorrido.
*   **Actualizaciones:** Permite la corrección automática de cartas (Notices to Mariners) mediante discos, USB o descargas satelitales.

## 4. Peligros y Precauciones en el uso de Cartografía Electrónica

El exceso de confianza en la electrónica es uno de los mayores riesgos modernos (Over-reliance).
*   **Datum:** Asegurar que el GPS y el sistema usan el mismo Datum (típicamente WGS84).
*   **Sobreescalado (Over-zooming):** Hacer demasiado zoom en una carta vectorial puede dar una falsa sensación de precisión. La exactitud de los datos subyacentes sigue siendo la de la escala original a la que se levantó la carta.
*   **Alarmas Desactivadas:** Por fatiga de alarmas (alarm fatigue), las tripulaciones a veces desactivan alarmas críticas de seguridad.
*   **Ataques Cibernéticos:** Al ser sistemas conectados, requieren protocolos de seguridad (USB controlados, redes segregadas).
