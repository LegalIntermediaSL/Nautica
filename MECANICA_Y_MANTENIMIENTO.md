# Manual de Mecánica Naval y Mantenimiento a Bordo

La supervivencia de una embarcación en alta mar depende críticamente de la fiabilidad de su propulsión y de su integridad eléctrica y estanca. A diferencia de un automóvil, un barco no puede detenerse en el arcén. El armador/patrón debe ser su propio mecánico de primera intervención.

---

## 1. El Motor Diésel Marino (Intraborda)

El motor diésel es el estándar en náutica por su robustez, seguridad (el gasoil no emite vapores explosivos a temperatura ambiente como la gasolina) y eficiencia térmica.

### Funcionamiento Básico
Es un motor de **combustión interna por compresión**. No tiene bujías de chispa. El aire entra en el cilindro, el pistón lo comprime brutalmente (elevando su temperatura a más de $600^\circ\text{C}$), y en el punto crítico el inyector pulveriza gasoil, que se autoinflama instantáneamente, empujando el pistón hacia abajo.

### Subsistemas Críticos y Mantenimiento
1.  **Circuito de Combustible:** El mayor enemigo del diésel marino es el **agua** y el "moco" (bacterias que crecen en la interfaz agua-gasoil en el depósito).
    *   **Mantenimiento:** Purgar periódicamente el filtro decantador de agua (pre-filtro). Si entra aire en el circuito (por ejemplo, por agotar el depósito), el motor no arrancará. Hay que purgar el circuito abriendo la tuerca de los inyectores y usando la bomba manual hasta que salga gasoil sin burbujas.
2.  **Sistema de Lubricación:** El aceite reduce la fricción. Un aceite blanquecino/lechoso (mayonesa) indica agua en el cárter (junta de culata rota), lo cual es una emergencia mecánica crítica.
    *   **Mantenimiento:** Comprobar nivel con varilla antes de zarpar. Cambio anual de aceite y filtro.

---

## 2. El Circuito de Refrigeración Marino

Los motores marinos generan calor extremo y se enfrían con el agua sobre la que navegan. Existen dos sistemas:

### Refrigeración Directa (Abierta)
El agua de mar (salada y corrosiva) entra por un pasacascos (grifo de fondo), pasa directamente por los canales del bloque motor (camisas de los cilindros) para absorber el calor, y se expulsa junto con los gases de escape.
*   **Problema:** Alta corrosión. Requiere **ánodos de sacrificio** internos (piezas de zinc que se oxidan ellas mismas en lugar del metal del motor por acción galvánica) que deben cambiarse anualmente.

### Refrigeración Indirecta (Cerrada por Intercambiador)
Es el sistema más moderno y seguro. Tiene dos circuitos:
1.  **Circuito Cerrado (Agua Dulce + Anticongelante):** Baña el motor por dentro, protegiéndolo de la corrosión.
2.  **Circuito Abierto (Agua de Mar):** Recoge agua fría del mar, la pasa por un radiador (intercambiador de calor) donde enfría el circuito cerrado sin mezclarse con él, y se expulsa por el escape.

### El Corazón del Sistema: El Impeller (Rodete)
El agua de mar es bombeada por una bomba cuyo núcleo es un **Rodete de goma o neopreno (Impeller)**. Es la pieza que más falla a bordo. Si el impeller gira en seco (por ejemplo, una bolsa de plástico tapa la toma de agua bajo el casco), se desintegra por fricción en segundos, el motor se sobrecalienta, y colapsa fundiendo la junta de la culata.
*   **Protocolo de Zarpe:** Inmediatamente tras arrancar el motor, el patrón debe asomarse por la popa y comprobar que el barco "escupe" agua junto al humo del escape a intervalos regulares. Si no escupe agua, apagar el motor instantáneamente.

---

## 3. Instalación Eléctrica Naval (12V vs 220V)

### Corriente Continua (DC - 12V o 24V)
Es la "sangre" de los sistemas del barco navegando: instrumentos, VHF, bombas de achique, luces y motor de arranque. Todo barco serio tiene dos parques de baterías separados por un aislador/repartidor de carga:
1.  **Batería de Arranque:** Diseñada para entregar muchísimos amperios en 2 segundos (Cold Cranking Amps, CCA) para mover el motor. Si se descarga profundamente, muere.
2.  **Baterías de Servicios (Ciclo Profundo):** Diseñadas para una descarga lenta y prolongada (luces, nevera). Aguantan descargas fuertes repetidas (Deep Cycle).

*Carga:* Se cargan navegando mediante el **Alternador** impulsado por la correa del motor, o fondeados mediante paneles solares/eólicos.

### Corriente Alterna (AC - 220V)
Solo está disponible cuando el barco está enchufado a la torreta del puerto (Shore Power) mediante un cable amarillo grueso, o si el barco posee un inversor (Inverter) de alta potencia, o un generador diésel autónomo. Alimenta enchufes estándar (para cafeteras, secadores) y el cargador inteligente de baterías.
*   *Peligro Galvánico:* Dejar el barco enchufado a 220V en puerto constantemente acelera la corrosión galvánica destructiva en el casco o la hélice si no hay un aislador galvánico instalado en la línea de tierra.

---

## 4. Integridad del Casco y Bombas de Achique

El agua siempre intentará entrar. El barco tiene conductos por debajo de la línea de flotación (pasacascos).
*   **Grifos de Fondo:** Válvulas conectadas a los pasacascos (entrada de agua al WC, refrigeración, desagües). Deben cerrarse (palanca perpendicular al tubo) al abandonar el barco en puerto o al navegar con mal tiempo.
*   **Bocina y Prensaestopas:** El eje de la hélice tiene que salir del interior del casco hacia el mar, pero el agua no puede entrar. El "prensaestopas" sella este agujero. Los clásicos están diseñados para gotear ligeramente en marcha para refrigerarse (1 gota por minuto). Los modernos (sello seco Volvo) no deben gotear nunca, pero deben "purgarse" (apretarlos con la mano) para que entre agua a refrigerarlos antes de arrancar.
*   **Bombas de Achique (Bilge Pumps):** Ubicadas en la sentina (la parte más baja). Todo yate debe tener una bomba eléctrica conectada a un interruptor de flotador automático (directo a la batería sin pasar por el cuadro, para que funcione aunque quites el contacto), y una **bomba manual obligatoria** operativa desde la cubierta para achicar sin electricidad durante un siniestro.

---

## 5. Invernaje (Winterization)

Preparar el yate para la temporada baja evita costosas facturas por daños ocultos y congelación.
1.  **Motor:** Endulzar el circuito de agua salada (hacerle aspirar agua dulce de un cubo para limpiar la sal). Llenar el depósito de gasoil hasta el límite máximo (para evitar condensación de aire húmedo = agua en el diésel). Añadir biocida contra bacterias. 
2.  **Electricidad:** Desconectar bornes de baterías (primero siempre el negativo `-` negro, luego positivo `+` rojo) para evitar consumo parasitario.
3.  **Velas y Cabuyería:** Retirar velas, enjuagarlas con agua dulce (la sal absorbe humedad ambiental pudriendo la tela). Aflojar los cabos sometidos a tensión permanente.
4.  **Grifos de fondo:** Cerrar todos excepto los sumideros auto-vaciantes de la bañera.

---

## 6. Herramientas Mínimas a Bordo

El maletín de herramientas náuticas debe contener como mínimo:
*   Llaves fijas/carraca, destornilladores, alicates de presión y llaves Allen.
*   *Impeller* (Rodete) de repuesto y junta tórica, junto con el extractor de rodetes.
*   Correa del alternador de repuesto.
*   Filtros de aceite y combustible (y llave de filtros).
*   Cinta autovulcanizante (sella fugas de tuberías).
*   WD-40 / Centauro (desplazadores de humedad) y grasa de litio/Teflón marina.
*   Espiches de madera cónicos (para clavar en una tubería rota bajo la línea de flotación).
*   Multímetro digital (para buscar derivaciones de voltaje).
