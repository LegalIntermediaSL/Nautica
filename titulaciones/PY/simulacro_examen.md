# Simulacro de Examen: Patrón de Yate (PY)

El examen de Patrón de Yate se centra intensamente en el cálculo de mareas y la estima analítica (trigonometría plana). Aquí tienes algunas preguntas clásicas de examen.

---

### Pregunta 1 (Navegación Carta / Corriente)
**Nos encontramos en L = 35º 50' N y L = 005º 15' W. Navegamos al Ra = 120º con Vb = 8 nudos. (Ct = -2º). Existe una corriente conocida de Rc = 180º e Ih (Intensidad horaria) = 3 nudos. ¿Cuál será nuestro Rumbo Efectivo (Ref) y Velocidad Efectiva (Vef) sobre el fondo?**
a) Ref = 145º, Vef = 10.5 nudos.
b) Ref = 138º, Vef = 9.8 nudos.
c) Ref = 118º, Vef = 8 nudos.
d) Ref = 133º, Vef = 9.2 nudos.

<details>
<summary><b>Ver Solución (Aproximada)</b></summary>
<b>Respuesta Correcta: B (Aproximación gráfica).</b><br>
1. Convertimos el Ra a Rv: Rv = 120 + (-2) = 118º.<br>
2. Dibujamos nuestro vector de Rumbo y Velocidad del barco: Origen en nuestra situación, dirección 118º y longitud 8 millas.<br>
3. Dibujamos el vector de la Corriente: Desde el final del vector anterior, trazamos una línea hacia el Sur (180º) con longitud 3 millas.<br>
4. El vector resultante (uniendo el origen con el final del vector corriente) es nuestro movimiento real. Al medirlo, dará aproximadamente 138º de rumbo y casi 10 nudos de velocidad (9.8).
</details>

### Pregunta 2 (Cálculo de Mareas)
**El Anuario de Mareas indica para el puerto de Cádiz: Bajamar a las 10:00h (sonda 1.0m) y Pleamar a las 16:15h (sonda 3.5m). Queremos salir de puerto pasando sobre un bajío que marca una sonda en la carta de 1.5m. Nuestro barco cala 2.0m y queremos un margen de seguridad de 0.5m. ¿A qué hora podremos salir?**
a) A las 12:45
b) A las 14:15
c) A las 13:02
d) A las 11:30

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta Correcta: C.</b><br>
1. Sonda necesaria = Calado (2.0) + Margen (0.5) = 2.5m de agua total necesaria.<br>
2. Sonda en carta = 1.5m. Nos falta 1.0m de agua, que nos lo tiene que dar la marea.<br>
3. Duración de la marea = 06h 15m (375 min). Amplitud = 2.5m.<br>
4. Aplicando la fórmula de mareas o tabla de interpolación, calculamos el tiempo que tarda la marea en subir ese 1.0m desde la bajamar. Aproximadamente tarda 3h 02m. <br>
5. 10:00 + 03h 02m = 13:02h.
</details>

### Pregunta 3 (Meteorología)
**La diferencia clave entre la Niebla de Advección y la Niebla de Radiación es:**
a) La de radiación se forma en alta mar y la de advección en la costa.
b) La de radiación requiere viento fuerte, la de advección requiere calma chicha.
c) La de advección se forma cuando aire cálido y húmedo se desplaza sobre un mar frío, mientras que la de radiación se forma por el enfriamiento del suelo terrestre durante la noche.
d) No hay diferencia, son lo mismo.

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta Correcta: C.</b><br>
La niebla de advección (muy común en el mar, ej. bancos de Terranova) es un desplazamiento horizontal del aire, que al chocar con agua muy fría, se condensa. La de radiación es típica de tierra adentro en invierno (los valles).
</details>

### Pregunta 4 (Estabilidad)
**Si estando el buque adrizado trasladamos un peso desde el centro de la eslora hacia la proa manteniéndolo en la misma cubierta (sin variar su cota vertical), ¿qué efecto tendrá sobre el Centro de Gravedad (G) y el calado?**
a) El G se desplazará hacia proa, el calado de proa aumentará y el de popa disminuirá.
b) El G se desplazará hacia arriba, disminuyendo la estabilidad transversal.
c) El G no variará porque el peso es el mismo.
d) El G se desplazará hacia proa y ambos calados aumentarán por igual.

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta Correcta: A.</b><br>
Al trasladar un peso longitudinalmente, el Centro de Gravedad del barco (G) se desplaza en esa misma dirección y sentido (hacia proa). Esto genera un momento de asiento que hace sumergir más la proa (aumenta el calado de proa) y emerger la popa (disminuye el calado de popa).
</details>

### Pregunta 5 (Loxodrómica - Cálculo Analítico)
**Navegamos desde A (l = 30º 00' N) hasta B (l = 32º 30' N). Sabiendo que el Apartamiento (A) ha sido de 150 millas hacia el Este, ¿cuál ha sido el Rumbo Verdadero aproximado de nuestra derrota loxodrómica?**
a) 045º
b) 030º
c) 060º
d) 120º

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta Correcta: A.</b><br>
1. Calculamos la Diferencia de Latitud ($\Delta l$) = 32º 30' - 30º 00' = 2º 30' hacia el Norte.<br>
2. Pasamos la $\Delta l$ a millas (minutos): 2º = 120' + 30' = 150 millas (N).<br>
3. Usamos la fórmula de la Loxodrómica: $\tan(Rv) = \frac{A}{\Delta l}$<br>
4. $\tan(Rv) = \frac{150}{150} = 1$<br>
5. $\arctan(1) = 45º$. Como vamos hacia el Norte y el Este (N E), el Rumbo es 045º.
</details>

### Pregunta 6 (Seguridad - Balsa Salvavidas)
**Una vez a bordo de la balsa salvavidas tras abandonar el yate, ¿cuál es la secuencia correcta de acciones inmediatas?**
a) Cortar la boza, lanzar el ancla flotante, cerrar la balsa y repartir el agua.
b) Cortar la boza, alejarse del buque que se hunde, lanzar el ancla flotante, cerrar la balsa y atender a los heridos.
c) Esperar a que el barco se hunda para que la zafa hidrostática libere la balsa automáticamente.
d) Remar inmediatamente hacia la costa más cercana.

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta Correcta: B.</b><br>
La secuencia vital es: 1. Cortar la boza (para no ser arrastrados por el barco al fondo). 2. Alejarse del peligro inmediato (vórtice, fuego, escombros). 3. Lanzar el ancla de capa (flotante) para evitar derivar a gran velocidad y estabilizar la balsa frente al viento. 4. Cerrar las aberturas para protegerse del frío/mar. 5. Atender heridos y tomar el mando. (El agua no se reparte en las primeras 24 horas).
</details>

### Pregunta 7 (Meteorología - Frentes)
**Tras el paso de un frente frío activo en el Hemisferio Norte, ¿qué cambios meteorológicos bruscos cabe esperar?**
a) El viento rola a la izquierda (hacia el Sur), la presión baja bruscamente y la temperatura sube.
b) El viento rola bruscamente a la derecha (hacia el NW), la presión sube de golpe, la temperatura cae y el cielo se aclara con cúmulos.
c) Nieblas persistentes y vientos en calma.
d) Llovizna continua durante varios días sin cambios en la presión.

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta Correcta: B.</b><br>
El paso de un frente frío se caracteriza por una rolada brusca del viento hacia la derecha (generalmente del SW al NW en el hemisferio norte), un ascenso brusco del barómetro (ya que la masa de aire frío es más densa y pesada), un descenso acusado de la temperatura y la sustitución de nubes estratificadas por nubes de desarrollo vertical (cúmulos/cumulonimbos) seguidas de claros.
</details>

### Pregunta 8 (Navegación - Viento Aparente)
**Si nuestro yate navega a 10 nudos con rumbo Norte (000º) y existe un viento real soplándonos exactamente desde el Este (090º) a 10 nudos, ¿desde qué dirección sentiremos el viento aparente y con qué intensidad aproximada?**
a) Lo sentiremos desde el Este (090º) a 10 nudos.
b) Lo sentiremos desde el Sureste (135º) a 14.1 nudos.
c) Lo sentiremos desde el Noreste (045º) a 14.1 nudos.
d) Lo sentiremos de proa (000º) a 20 nudos.

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta Correcta: C.</b><br>
El viento aparente es la resultante vectorial de sumar el Viento Real y el Viento Relativo (generado por nuestra marcha, que sopla directo de proa hacia popa).<br>
- Viento Real: Vector hacia el Oeste (viene del Este, 090º) de módulo 10.<br>
- Viento Relativo (Marcha): Vector hacia el Sur (viene del Norte, 000º) de módulo 10.<br>
- Resultante: La diagonal del cuadrado, que viene del Noreste (045º).<br>
- Módulo: Teorema de Pitágoras $\sqrt{10^2 + 10^2} = \sqrt{200} = 14.1$ nudos.
</details>
