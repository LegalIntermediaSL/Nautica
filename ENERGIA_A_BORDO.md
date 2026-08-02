# Sistemas de Energía a Bordo: La Central Flotante

La navegación moderna depende intrínsecamente de la electricidad. Pilotos automáticos, plotters, potabilizadoras, neveras y bombas de achique; sin energía, un yate moderno retrocede al siglo XIX en cuestión de horas.

## 1. El Banco de Baterías (El Corazón del Barco)

Todo buque cuenta con al menos dos bancos separados:
*   **Banco de Motor:** Diseñado para dar un pico brutal de amperios durante unos segundos para arrancar el motor diésel (baterías de arranque tipo CCA). NUNCA deben conectarse a los servicios de a bordo.
*   **Banco de Servicios:** Diseñado para entregar energía de forma lenta y constante (Ciclo Profundo). 

### La Revolución del Litio (LiFePO4) vs Plomo (AGM / Gel)
Durante décadas, la náutica ha dependido de las baterías de plomo ácido (AGM o Gel). Hoy, la tecnología dominante es el **Litio Ferro-Fosfato (LiFePO4)**, que es extremadamente segura (no arde como el litio de los móviles) y ofrece ventajas demoledoras:

| Característica | AGM / GEL (Plomo) | LiFePO4 (Litio) |
| :--- | :--- | :--- |
| **Profundidad de Descarga (DoD)** | Máx. 50%. (Si bajas del 50%, destruyes la batería) | Hasta 95%. Tienes casi el doble de energía útil. |
| **Peso** | Extremadamente pesadas (ej. 60 kg por 200Ah). | 3 veces más ligeras (ej. 20 kg por 200Ah). |
| **Carga Máxima** | Tardan horas en absorber el último 20% (carga lenta). | Absorben toda la energía que les des hasta el 99%. |
| **Caída de Voltaje** | Si enciendes algo potente (ej. molinete), la luz parpadea. | Voltaje plano y constante hasta que se vacían. |

> [!WARNING]
> **Cuidado con los Alternadores**
> Las baterías de Litio tragan tanta energía tan rápido que pueden sobrecalentar y quemar el alternador estándar de tu motor diésel. Se requiere instalar un alternador de alto rendimiento o un cargador DC-DC intermedio que limite el amperaje.

## 2. Auditoría de Consumos (Balance Energético)

Para saber cuánta energía necesitas, debes sumar el consumo diario en **Amperios-hora (Ah)** (asumiendo un sistema de 12V).

**Consumos Clásicos en un Velero de 12m (24 horas):**
1.  **Nevera:** ~60 Ah/día (Es el enemigo silencioso #1. Arranca y para continuamente).
2.  **Piloto Automático:** ~50 a 100 Ah/día (Depende muchísimo del estado de la mar. Con oleaje cruzado, trabaja el triple).
3.  **Electrónica (Plotter, AIS, VHF):** ~30 Ah/día.
4.  **Iluminación LED y Bombas:** ~10 Ah/día.
5.  **Inversor 220V (Cafetera, PC):** ~20 Ah/día.
**Total Diario Estimado:** ~170 a 220 Ah a 12V (aprox. 2.5 kWh).

## 3. Generación de Energía Autónoma

Si tu banco de baterías es de 400Ah (LiFePO4), tienes unos 380Ah útiles. Consumiendo 200Ah al día, te quedarás a oscuras en menos de 2 días. Necesitas generar energía:

### Paneles Solares
Es la fuente reina en los trópicos y el Mediterráneo.
*   **Reguladores MPPT vs PWM:** El MPPT es obligatorio hoy en día. Convierte el voltaje extra del panel en amperios extra para la batería de forma inteligente (hasta un 30% más eficiente).
*   **Sombras (El asesino solar):** Un panel solar náutico sufre mucho por las sombras de la jarcia y las velas. Si un cabo hace sombra sobre una sola célula del panel, la producción del panel completo puede caer un 50% o más. Por eso se instalan en paralelo o en puentes de popa (arcos radar) lejos del mástil.

### Hidrogeneradores
Es un "pequeño molino de viento" pero sumergido en el agua por la popa del barco. 
*   **Ventaja:** Cuando el velero navega a vela por encima de 5 nudos, la hélice gira arrastrada por el agua y genera una cantidad brutal de energía (puede dar más de 300Ah al día sin problemas).
*   **Desventaja:** Frena el barco en torno a 0.2 - 0.5 nudos debido a la resistencia hidrodinámica (drag).

### Generadores Eólicos
*   Son ruidosos y vibran, pero generan energía de noche (cuando no hay sol) y fondeados (cuando el hidrogenerador no sirve). Hoy en día, han perdido popularidad frente a la brutal bajada de precios y aumento de eficiencia de los paneles solares.

## 4. Inversores y Corriente Alterna (220V / 110V)

En el mar todo va a 12V o 24V (Corriente Continua). Si quieres usar un portátil, un microondas o una máquina Nespresso, necesitas un Inversor que convierta 12V CC a 220V CA.

*   **Pico de Arranque:** Una cafetera Nespresso de 1200W funcionando a 220V, chupará ¡100 Amperios! de tu batería de 12V. Los cables deben ser gruesos como pulgares para no incendiarse.
*   **Inversores de Onda Pura:** Solo compra inversores de onda senoidal pura (Pure Sine Wave). Los baratos (onda modificada) destruirán los cargadores de tus ordenadores portátiles.
