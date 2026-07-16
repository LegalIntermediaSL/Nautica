# PER - Tema 10: Teoría de Navegación Cartográfica

Este tema es el cimiento absoluto. Asienta las bases matemáticas, geográficas y magnéticas sin las cuales es físicamente imposible resolver posteriormente un solo ejercicio de trazado sobre la carta de navegación. Todo buen patrón debe entender el mundo en el que navega.

---

## 1. Geometría de la Esfera Terrestre

Aunque nuestro planeta está ligeramente achatado por los polos (Elipsoide), a efectos de navegación clásica básica y cartas Mercator, lo consideramos una esfera perfecta.

*   **Eje Terrestre:** Es la varilla imaginaria que atraviesa el planeta y sobre la cual la Tierra da una vuelta cada 24 horas. Los puntos donde esta varilla sale al exterior son el Polo Norte (Pn) y el Polo Sur (Ps) geográficos.
*   **Ecuador:** Si cortamos la Tierra por la mitad con un plano perpendicular al Eje Terrestre, obtenemos el círculo más grande posible: el Ecuador. Divide el planeta en Hemisferio Norte y Hemisferio Sur.
*   **Paralelos:** Son cortes paralelos al Ecuador. Son "anillos" cada vez más pequeños a medida que nos acercamos a los polos.
*   **Meridianos:** Son grandes círculos verticales que cortan la Tierra de Norte a Sur, pasando siempre por ambos Polos. Es como los gajos de una naranja. Todos los meridianos miden lo mismo y **se cruzan en los polos**. El meridiano elegido por la humanidad como "Cero" es el Meridiano de Greenwich (Londres).

## 2. Coordenadas Geográficas (El DNI de una posición)

Para clavar un punto exacto en la inmensidad del océano, usamos un eje de coordenadas basado en los paralelos y los meridianos, medido en Grados ($^\circ$), Minutos (') y décimas de minuto.
*(Nota: Un grado tiene 60 minutos. $1^\circ = 60'$)*.

*   **Latitud ($l$):** Nos dice lo arriba o abajo que estamos en el globo. Es el arco medido desde el Ecuador hasta el paralelo del barco.
    *   Se mide de **$0^\circ$ (Ecuador) a $90^\circ$ (Polos)**.
    *   Debe indicar siempre si es **Norte (N)** o **Sur (S)**.
    *   *Propiedad mágica:* **1 minuto de Latitud equivale exactamente a 1 Milla Náutica (1852 metros)** en la superficie del planeta.
*   **Longitud ($L$):** Nos dice lo a la derecha o izquierda que estamos. Es el arco medido por el Ecuador desde el Meridiano de Greenwich hasta el meridiano del barco.
    *   Se mide de **$0^\circ$ (Greenwich) a $180^\circ$ (Antimeridiano)**.
    *   Debe indicar siempre si es **Este (E)** u **Oeste (W - West)**.
    *   *(En la costa española peninsular, casi siempre navegaremos en Longitud Oeste y Latitud Norte).*

## 3. Direcciones, Rumbos y Magnetismo Terrestre

La **Rosa de los Vientos** está dividida en 360 grados, comenzando en el Norte ($000^\circ$) y contando siempre en el sentido de las agujas del reloj (Este=$090^\circ$, Sur=$180^\circ$, Oeste=$270^\circ$).
El **Rumbo ($R$)** es el ángulo físico que forma la línea central (crujía) de nuestro barco con un "Norte" de referencia. Pero el problema histórico de la navegación es que existen TRES Nortes diferentes:

### 3.1 Los Tres Nortes
1.  **Norte Verdadero ($N_v$):** Es el norte geográfico real, el Polo Norte físico, el de los osos polares. Es la línea vertical negra que está **impresa en las cartas náuticas de papel**.
2.  **Norte Magnético ($N_m$):** El núcleo de hierro líquido de la Tierra genera un campo magnético colosal. Este campo atrae las brújulas hacia un Polo Norte Magnético, pero este punto NO coincide con el Polo Norte geográfico (está en Canadá y se mueve cada año).
3.  **Norte de Aguja ($N_a$):** Es hacia donde apunta torcidamente la aguja de la brújula (el compás) **instalada a bordo de TU barco**. Está afectada por el campo magnético de la Tierra Y ADEMÁS por el hierro del motor de tu barco, tu emisora VHF y los altavoces de tu cubierta.

## 4. Cálculo de Errores: Declinación, Desvío y Corrección Total

Para trazar una línea recta en el mapa (Norte Verdadero) basándote en la lectura de la brújula de plástico de tu timón (Norte de Aguja), tienes que calcular y aplicar matemáticamente dos errores.

### Error 1: Declinación Magnética ($dm$)
Es el ángulo geológico entre el Norte Verdadero y el Norte Magnético. 
Es culpa del planeta. Viene impresa en la rosa de los vientos de todas las cartas náuticas indicando un año base y lo que varía anualmente (ya que el magma terrestre se mueve).
*   *Regla de Signos:* Si apunta hacia el **Este (E)** es matemática **Positiva (+)**. Si apunta hacia el **Oeste (W)** es matemática **Negativa (-)**.

### Error 2: Desvío de Aguja ($\Delta$)
Es el ángulo mecánico entre el Norte Magnético y el Norte de Aguja. 
Es culpa exclusiva de tu barco (de sus hierros). **Varía dependiendo de hacia dónde estés apuntando la proa**. El instalador del compás te entrega un papel llamado "Tablilla de Desvíos" que te dice qué error tienes en cada rumbo.
*   *Regla de Signos:* Igual que arriba. **Este (+) / Oeste (-)**.

### La Corrección Total ($C_t$)
Es simplemente sumar algebraicamente (respetando los signos menos) los dos errores para convertirlos en un solo paquete de error corregible.
$$ C_t = d_m + \Delta $$

### Ecuaciones Fundamentales de Conversión
Si estás en la bitácora mirando la brújula y quieres llevar esa lectura al mapa de papel:
$$ R_v = R_a + C_t $$
*(Rumbo Verdadero = Rumbo de Aguja + Corrección Total)*

Si has trazado una línea perfecta en tu mapa de papel hacia tu destino y necesitas decirle al timonel qué número poner en la brújula para no estrellarse:
$$ R_a = R_v - C_t $$
*(Rumbo de Aguja = Rumbo Verdadero - Corrección Total)*
