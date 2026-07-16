# Patrón de Yate - Tema 3: Teoría de Navegación (Viento y Mareas)

Este tema exige dominar el cálculo de mareas para no quedarse varado al entrar a puerto, y comprender la cinemática del viento para gobernar la embarcación con eficacia.

---

## 1. Teoría y Cálculo de Mareas

Las mareas son el movimiento vertical del nivel del mar producido por la atracción gravitatoria de la Luna (principalmente) y del Sol. En puertos del Atlántico (como Cádiz, en la zona de examen del Estrecho), la marea puede variar varios metros en unas horas.

### Conceptos Clave
*   **Pleamar (PM):** Nivel máximo que alcanza el agua en un ciclo.
*   **Bajamar (BM):** Nivel mínimo.
*   **Amplitud de Marea (A):** Diferencia de altura entre la Pleamar y la Bajamar ($A = Alt_{PM} - Alt_{BM}$).
*   **Duración de la vaciante/creciente (D):** Tiempo que transcurre entre una pleamar y la bajamar siguiente (o viceversa). Suele ser de unas 6 horas (mareas semidiurnas).
*   **Sonda de la Carta (Sc):** La profundidad que marca la carta náutica. Está referida al nivel mínimo histórico posible (Bajamar Escorada).
*   **Sonda en el Momento (Sm):** La profundidad real que hay bajo la quilla en un momento concreto.
    $$ Sm = Sc + Altura_{marea} $$

### Cálculo de la Altura de la Marea en un Instante Cualquiera
El *Anuario de Mareas* nos da la hora y altura exacta de la PM y la BM. Si llegamos a puerto a una hora intermedia, debemos calcular el nivel del agua.

1.  Calculamos la Amplitud (A) y la Duración (D) de esa marea en concreto.
2.  Calculamos el Intervalo (I): Tiempo transcurrido desde la última pleamar/bajamar hasta la hora deseada.
3.  Aplicamos la **Fórmula Universal (Método Analítico):**
    $$ Correcci\acute{o}n = A \cdot \sin^2\left(\frac{90^\circ \cdot I}{D}\right) $$
4.  Si calculamos desde la Bajamar, sumamos la Corrección a la altura de la BM. Si calculamos desde la Pleamar, restamos la Corrección a la altura de la PM.

---

## 2. Viento Real y Viento Aparente (Cinemática)

El movimiento del barco crea un flujo de aire. Las velas (o nosotros mismos en cubierta) no sienten el viento atmosférico, sino la resultante matemática del viento real y el de nuestra propia velocidad.

*   **Viento Real (Vr):** El viento atmosférico (medido desde tierra).
*   **Velocidad del Buque (Vb):** Nuestro movimiento de avance. Esto genera un **Viento Relativo** de igual intensidad pero de dirección contraria a nuestro rumbo.
*   **Viento Aparente (Va):** Es la suma vectorial del Viento Real más el Viento Relativo. Es el viento que marca el anemómetro del barco.

### Resolución Gráfica (Triángulo de Velocidades)
1.  Trazamos un vector que represente el Rumbo y Velocidad del barco.
2.  Desde el ORIGEN de ese vector, trazamos el vector del Viento Aparente.
3.  Unimos las puntas de ambos vectores. Ese vector resultante nos da la intensidad y dirección del **Viento Real**.

> [!TIP]
> Recuerda que el Viento Aparente siempre entra más por la proa que el Viento Real. A medida que aceleras, el viento se "aproa".

---

## 3. Cinemática de Radar (Nociones de Punteo)

El radar ARPA permite rastrear otros barcos para saber si colisionaremos.
*   **Movimiento Relativo:** En la pantalla del radar, nuestro barco está quieto en el centro. El eco del otro barco se mueve con un "Rumbo Relativo".
*   Si trazamos la estela del eco en la pantalla y la línea cruza nuestro centro, hay colisión inminente (Demora Constante).
*   **CPA (Closest Point of Approach):** Punto de mínima distancia al que pasará el otro barco.
*   **TCPA (Time to CPA):** Tiempo restante hasta alcanzar ese punto crítico.
