# Patrón de Yate - Tema 1: Seguridad y Estabilidad

En travesías lejos de costa, la supervivencia del buque y la tripulación recae 100% sobre las decisiones del patrón. 

---

## 1. Estabilidad Transversal

Un barco flota gracias al **Principio de Arquímedes**: el agua desplazada por el casco genera una fuerza de Empuje hacia arriba igual al Peso del barco hacia abajo.

### Puntos Críticos de la Estabilidad
*   **Centro de Gravedad (G):** El punto donde se aplica todo el Peso del barco (hacia abajo). Su posición depende de la carga. Si cargamos pesos en cubierta, G sube. Si vaciamos el depósito de agua en la quilla, G sube.
*   **Centro de Carena (C):** El centro geométrico de la parte sumergida del casco. Es donde se aplica el Empuje (hacia arriba). Al escorar (inclinarse) el barco, la forma sumergida cambia, por lo que C se desplaza hacia la banda de escora.
*   **Metacentro (M):** Es la intersección entre el eje de simetría del barco y la vertical trazada desde el nuevo Centro de Carena (C) cuando el barco escora un ángulo pequeño.

### El Par de Estabilidad (Brazo Adrizante)
Cuando el barco escora, G (hacia abajo) y el nuevo C (hacia arriba) ya no están en la misma línea vertical. Estas dos fuerzas paralelas y de sentido contrario crean un "Par de Fuerzas" que hace rotar al barco.

*   **Brazo Adrizante (GZ):** Es la distancia horizontal entre G y la vertical de C.
*   **Condición de Equilibrio Estable:** El Metacentro (M) debe estar **POR ENCIMA** del Centro de Gravedad (G). Así, el par de fuerzas generado empuja al barco a adrizarse (ponerse derecho).
*   **Condición de Equilibrio Inestable (Vuelco):** Si G sube demasiado (mucho peso arriba) y se coloca por encima de M, el par de fuerzas empujará al barco a escorar aún más, provocando la zozobra (vuelco).

> [!WARNING]
> La regla de oro del Patrón de Yate frente a temporales: **Bajar el Centro de Gravedad**. Trincar pertrechos abajo, vaciar depósitos altos y evitar gente en la cubierta superior.

## 2. Supervivencia y Abandono de Buque

**¡El barco es el mejor salvavidas!** El abandono del buque a la balsa salvavidas solo se ordena cuando el hundimiento es absolutamente irremediable o el fuego está fuera de control. El frío y el agua matan mucho más rápido que un barco desarbolado a la deriva.

### Zafas Hidrostáticas
La balsa salvavidas y la radiobaliza (EPIRB) deben llevar un mecanismo de liberación hidrostática. Si el barco se hunde y no hay tiempo de lanzarlas manualmente, este mecanismo corta la trinca automáticamente al sumergirse unos 2-4 metros por la presión del agua, liberándolas para que floten hacia la superficie.

### La Bolsa de Supervivencia (Grab Bag)
Un petate estanco que siempre debe estar a mano junto a la escalera de la cabina. Debe contener:
*   Radio VHF portátil estanca y de respeto.
*   Documentación (Pasaportes, papeles del barco).
*   Medicinas específicas de la tripulación y pastillas antimareo.
*   Gafas de repuesto.
*   Agua adicional y raciones de supervivencia extra.
*   Mantas térmicas y espejo de señales.

## 3. Dispositivos del GMDSS (SMSSM)

El Sistema Mundial de Socorro y Seguridad Marítimos es la red de comunicaciones oficial.

*   **EPIRB (Radiobaliza de Localización de Siniestros):** Al activarse (manual o por el agua), emite una señal a la red de satélites COSPAS-SARSAT en 406 MHz, enviando la identidad del barco (MMSI) y sus coordenadas GPS al Centro Coordinador de Salvamento Terrestre (MRCC).
*   **SART (Respondedor de Radar):** Dispositivo portátil que se lleva a la balsa. Cuando recibe la onda del radar de un barco que nos está buscando (banda X de 9 GHz), responde emitiendo una señal que dibuja **12 puntos** en la pantalla del radar del buque de rescate, indicando el rumbo exacto hacia nosotros.
*   **VHF - Llamada Selectiva Digital (LSD/DSC):** En el Canal 70 (uso exclusivo digital, prohibida la fonía). El botón rojo de "DISTRESS" envía una alerta codificada a todos los barcos en unas 30 millas con nuestra posición, identidad y, opcionalmente, la naturaleza del peligro.
