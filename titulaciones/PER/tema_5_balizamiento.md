# PER - Tema 5: Balizamiento Marítimo (Sistema IALA Completo y Avanzado)

El balizamiento es el código de circulación de las carreteras del mar. Utiliza boyas flotantes, castilletes, espeques y balizas fijas para indicar los canales de navegación seguros, advertir de peligros invisibles bajo el agua y delimitar zonas de uso especial. Un patrón de yate debe tener una reacción instantánea e intuitiva al ver una marca o su luz en la oscuridad.

El examen del PER exige conocer a la perfección la normativa internacional **IALA** (Asociación Internacional de Autoridades de Señalización Marítima). El mundo se divide en dos regiones (A y B). **España y Europa pertenecen a la Región A**. (América, Japón, Corea y Filipinas usan la Región B, donde los colores laterales están invertidos).

---

## 1. Fundamentos Físicos y Ópticos del Balizamiento

### 1.1 Hidrodinámica y Estabilidad de Boyas
Las boyas no son meros objetos flotantes; su diseño responde a estrictos principios hidrodinámicos para garantizar su verticalidad y visibilidad en estados de la mar adversos (alta energía del oleaje). La fuerza de arrastre hidrodinámico ($F_d$) ejercida por las corrientes se modela mediante la ecuación:

$$ F_d = \frac{1}{2} \rho v^2 C_d A $$

Donde:
*   $\rho$ es la densidad del agua de mar ($\approx 1025 \, \text{kg/m}^3$).
*   $v$ es la velocidad de la corriente.
*   $C_d$ es el coeficiente de arrastre de la geometría de la boya.
*   $A$ es el área proyectada sumergida (obra viva).

Para evitar que la boya se sumerja por la tensión de la cadena (efecto "garreo" vertical), su volumen de reserva de flotabilidad debe contrarrestar la suma del peso muerto, la tensión de catenaria del fondeo y las fuerzas hidrodinámicas de abatimiento.

### 1.2 Óptica, Alcance Luminoso y Rango Nominal
En navegación nocturna, la capacidad de avistar una baliza depende de su intensidad luminosa y de la transmisividad atmosférica. El Alcance Luminoso se calcula a través de la Ley de Allard:

$$ E = \frac{I}{D^2} e^{-\sigma D} $$

Donde:
*   $E$ es la iluminancia en el ojo del observador (umbral de visión $\approx 2 \times 10^{-7} \, \text{lux}$).
*   $I$ es la intensidad luminosa de la fuente (candelas).
*   $D$ es la distancia.
*   $\sigma$ es el coeficiente de extinción atmosférica, directamente relacionado con la visibilidad meteorológica ($V$) mediante la Ley de Koschmieder: $V = \frac{3.912}{\sigma}$.

El Sistema IALA establece que el "Alcance Nominal" de una luz de balizamiento es aquel que corresponde a una visibilidad meteorológica homogénea de 10 millas náuticas ($T \approx 0.74$).

---

## 2. Estructura del Sistema IALA

El sistema se compone de seis tipos de marcas. Para cada una de ellas es obligatorio memorizar cuatro atributos exactos:
1.  **Significado:** Qué nos está indicando (aguas seguras, canal, peligro).
2.  **Color del Cuerpo:** El color de la boya o castillete de día (coordenadas de cromaticidad CIE 1931 estandarizadas).
3.  **Marca de Tope:** La figura geométrica montada en su parte más alta.
4.  **Ritmo y Color de la Luz:** El parpadeo característico para navegación nocturna.

---

## 3. Marcas Laterales (El Canal Navegable)

Se utilizan para señalizar los lados (babor y estribor) de los canales balizados. La clave es el **"Sentido Convencional de Balizamiento"**: las marcas se definen asumiendo que **entramos** al puerto viniendo desde alta mar.

### 3.1 Marca Lateral de Estribor (Entrando)
*   *Color:* **Verde**. (Longitud de onda dominante: 500-530 nm).
*   *Forma:* Cónica (terminada en punta), castillete o espeque.
*   *Marca de tope:* Un **cono verde** con el vértice hacia arriba.
*   *Luz (Noche):* **Verde**. Puede tener cualquier ritmo EXCEPTO el ritmo Gp(2+1).

### 3.2 Marca Lateral de Babor (Entrando)
*   *Color:* **Rojo**. (Longitud de onda dominante: 610-630 nm).
*   *Forma:* Cilíndrica (terminada plana), castillete o espeque.
*   *Marca de tope:* Un **cilindro rojo**.
*   *Luz (Noche):* **Roja**. Cualquier ritmo EXCEPTO el Gp(2+1).

> [!TIP]
> **Regla Mnemotécnica (Solo Región A):** Si entras a puerto de noche, la luz verde de la boya de estribor coincidirá con la luz verde de tu barco. Entras como por un pasillo verde-verde y rojo-rojo. (En América/Región B es "Red Right Returning").

### 3.3 Marcas de Bifurcación (Canal Principal)
Si un canal se divide, se coloca una marca modificada que indica el canal "principal" (mayor batimetría).
*   **Canal Principal a Estribor:** Marca lateral de Babor (Roja) con **banda horizontal Verde**. Luz: Roja, ritmo **Gp(2+1)**.
*   **Canal Principal a Babor:** Marca lateral de Estribor (Verde) con **banda horizontal Roja**. Luz: Verde, ritmo **Gp(2+1)**.

---

## 4. Marcas Cardinales (Navegación en Mar Abierto)

Indican dónde están las aguas seguras basándose en los puntos cardinales, rodeando un peligro (escollos, pecios). Todas usan colores **Amarillo (Y) y Negro (B)**, tope de **dos conos negros** y luz **Blanca**.

### 4.1 Cardinal Norte (Pasa por mi Norte)
*   *Marca de tope:* Dos conos negros con **vértices hacia ARRIBA**.
*   *Colores:* **Negro sobre Amarillo**.
*   *Luz Blanca:* Centelleo Rápido (Q) o Muy Rápido (VQ) **continuo**.

### 4.2 Cardinal Sur (Pasa por mi Sur)
*   *Marca de tope:* Dos conos negros con **vértices hacia ABAJO**.
*   *Colores:* **Amarillo sobre Negro**.
*   *Luz Blanca:* Grupo de **6 centelleos cortos + 1 destello largo** (VQ(6)+LFl) cada 10/15s.

### 4.3 Cardinal Este (Pasa por mi Este)
*   *Marca de tope:* Dos conos opuestos por sus bases (**rombo**).
*   *Colores:* **Negro - Amarillo - Negro**.
*   *Luz Blanca:* Grupo de **3 centelleos rápidos** (Q(3)). *(Truco: las 3 del reloj).*

### 4.4 Cardinal Oeste (Pasa por mi Oeste)
*   *Marca de tope:* Dos conos opuestos por sus vértices (**reloj de arena**).
*   *Colores:* **Amarillo - Negro - Amarillo**.
*   *Luz Blanca:* Grupo de **9 centelleos rápidos** (Q(9)). *(Truco: las 9 del reloj).*

---

## 5. Marca de Peligro Aislado
Colocada fondeada exactamente encima de un peligro de poca extensión rodeado de aguas navegables.
*   *Color:* **Negro** con bandas anchas horizontales **ROJAS**.
*   *Marca de tope:* **Dos esferas negras superpuestas**.
*   *Luz (Noche):* **Blanca**, Grupo de **2 destellos** (Fl(2)).

## 6. Marca de Aguas Navegables
Indica aguas seguras en todo el entorno (eje de canal, recalada).
*   *Color:* Rayas **verticales Rojas y Blancas**.
*   *Marca de tope:* Una **esfera ROJA**.
*   *Luz (Noche):* **Blanca**. Ritmos largos: Iso, Oc, LFl.10s o **Morse "A"** (punto-raya).

## 7. Marcas Especiales y Nuevos Peligros
*   **Especiales:** Indican zonas reguladas (tuberías, campos de tiro, regatas). Color: **Amarillo**. Tope: **"X"**. Luz: **Amarilla**.
*   **Nuevos Peligros:** Fondeadas de emergencia ante naufragios recientes. Rayas verticales **Amarillas y Azules**, cruz amarilla, luz destellos Amarillo/Azul alternados.
