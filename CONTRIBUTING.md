# Guía de Contribución

¡Gracias por tu interés en mejorar **Náutica de Recreo**! Este repositorio solo tiene valor si la información que contiene es correcta y clara. Antes de abrir tu primer *pull request*, tómate cinco minutos para leer estas pautas: te ahorrarán idas y vueltas en la revisión.

---

## 1. Filosofía del proyecto

- **Contenido educativo, no normativo.** Este repositorio explica y resume la náutica de recreo (titulaciones, RIPA, balizamiento, meteorología, mecánica, etc.) con fines instructivos. **No sustituye a la normativa oficial** (BOE, Órdenes Ministeriales, resoluciones de la Dirección General de la Marina Mercante) ni a la formación reglada en una escuela homologada.
- **La precisión está por encima de todo.** Un dato náutico mal explicado (una prioridad de paso del RIPA, un color de boya, un número de preguntas de examen) puede inducir a un error real en el mar o en un examen oficial. Si tienes dudas sobre un dato, es mejor señalarlo como pendiente de verificar que darlo por bueno.
- **Tono didáctico, no un copia-pega de la ley.** El objetivo es que alguien que estudia para el PER, el PNB o cualquier otra titulación entienda el concepto, no solo que lo memorice. Usa ejemplos, analogías, tablas y diagramas siempre que ayuden a fijar la idea.
- El disclaimer del `README.md` (sección "Aviso de Responsabilidad") aplica a todo el contenido del repositorio, incluido el que tú añadas.

---

## 2. Estructura de directorios

El repositorio se organiza así:

```
Nautica/
├── README.md, CHANGELOG.md, BITACORA.md...   (archivos temáticos generales en la raíz)
├── titulaciones/
│   ├── CONSEJOS_EXAMEN.md, PRACTICAS.md       (archivos transversales a todas las titulaciones)
│   ├── PER/  PNB/  PY/  CY/  LN/
│   │   ├── INDEX.md
│   │   ├── tema_1_xxx.md, tema_2_xxx.md...
│   │   └── simulacro_examen.md
├── cartas_nauticas/   INDEX.md + archivos temáticos
├── faros/             INDEX.md + archivos temáticos
├── puertos/           INDEX.md + archivos por zona geográfica
├── nudos/             INDEX.md + archivos por categoría + img/
├── simulaciones/       README.md + notebooks .ipynb numerados
└── assets/images/      imágenes compartidas por varios documentos
```

### ¿Archivo nuevo o ampliar uno existente?

- **Amplía un archivo existente** cuando el contenido nuevo es una extensión natural de un tema ya tratado (por ejemplo, añadir un tipo de boya nuevo a `RIPA_Y_BALIZAMIENTO.md`, o un puerto nuevo a `puertos/MEDITERRANEO.md`).
- **Crea un archivo nuevo** cuando el contenido:
  - Corresponde a un tema/lección completo de una titulación (`titulaciones/<SIGLA>/tema_N_nombre.md`).
  - Abre una categoría temática que no encaja en ningún archivo actual (por ejemplo, un nuevo manual de a bordo tipo `MANIOBRAS_Y_FONDEO.md`).
  - Es tan extenso que mezclarlo con un archivo existente dificultaría la lectura (un archivo de más de ~500 líneas es buena señal de que toca dividir).
- En caso de duda, abre un *issue* describiendo el contenido que quieres añadir antes de escribir todo el texto; así evitas rehacer trabajo si la ubicación no encaja.

---

## 3. Convenciones de nombrado

| Ubicación | Convención | Ejemplo |
| :--- | :--- | :--- |
| Raíz del repositorio | `MAYUSCULAS_CON_GUIONES_BAJOS.md` | `RIPA_Y_BALIZAMIENTO.md`, `SEGURIDAD.md` |
| Dentro de subcarpetas (`cartas_nauticas/`, `faros/`, `puertos/`, `nudos/`, `titulaciones/<SIGLA>/`) | `minusculas_con_guiones_bajos.md` | `simbologia.md`, `atlantico.md` |
| Índice de cada subcarpeta/titulación | Siempre `INDEX.md` (mayúsculas, es la excepción) | `titulaciones/PER/INDEX.md` |
| Temas de una titulación | `tema_N_nombre_descriptivo.md`, numerado en el orden del temario oficial | `tema_5_balizamiento.md` |
| Simulacro de examen de una titulación | `simulacro_examen.md` (o `simulacro_modulo_xxx.md` si el examen se divide en módulos, como en CY) | `titulaciones/CY/simulacro_modulo_navegacion.md` |
| Notebooks de `simulaciones/` | Prefijo numérico de dos dígitos + nombre descriptivo | `05_ortodromica_vs_loxodromica.ipynb` |
| Imágenes | `minusculas_con_guiones.jpg/png`, alojadas en `assets/images/` (si son de uso general) o en un `img/` local a la subcarpeta (como `nudos/img/`) | `assets/images/sloop.jpg` |

No mezcles convenciones: un archivo temático nuevo en la raíz va en mayúsculas; el mismo archivo, si viviera dentro de `titulaciones/PER/`, iría en minúsculas.

---

## 4. Estilo de escritura

- **Idioma:** español, con la terminología náutica española estándar (babor/estribor, no *port/starboard*; RIPA, no *COLREG*, salvo que compares ambos a propósito).
- **Tono:** didáctico y cercano, como quien explica el tema a un alumno que se examina en unas semanas. Se admite algún truco mnemotécnico o analogía (el repo ya usa varios, p. ej. "Rojo sobre Rojo, capitán piojo").
- **Negrita** para resaltar términos clave, nombres técnicos y cifras importantes la primera vez que aparecen (`**RIPA**`, `**12 millas náuticas**`).
- **Tablas Markdown** para cualquier comparativa (luces de buques, atribuciones por titulación, plazos, etc.). Sigue el formato ya usado en el repositorio:

  ```markdown
  | Tipo de Buque | Luces de Noche (Mástil) | Marcas de Día (Negras) |
  | :--- | :--- | :--- |
  | **Sin Gobierno** | Roja sobre Roja | Dos bolas verticales |
  ```

- **Diagramas Mermaid** cuando ayuden a visualizar un proceso, una jerarquía o un flujo de decisión (por ejemplo, qué maniobra tomar según el tipo de cruce, o la estructura de un canal balizado). No abuses de ellos: solo cuando aporten claridad real sobre un párrafo de texto. Ejemplo mínimo de sintaxis usada en el repositorio:

  ```markdown
  ```mermaid
  graph TD;
      Entrada[Entrada al Canal] -->|Verde a Estribor| Marca_Verde[Cono Verde];
      Entrada -->|Rojo a Babor| Marca_Roja[Cilindro Rojo];
      Marca_Verde --> Canal_Seguro[Canal Principal];
      Marca_Roja --> Canal_Seguro;
  ```
  ```

- Usa listas numeradas para procedimientos con un orden estricto (una maniobra, los pasos de una prueba) y listas con viñetas para enumeraciones sin orden obligatorio.
- Puedes usar fórmulas en LaTeX (`$...$` o `

$$
...
$$

`) para cálculos de navegación, como ya se hace en `titulaciones/CY/` y en `cartas_nauticas/CALCULOS_DE_NAVEGACION.md`.

---

## 5. Cómo añadir un nuevo tema a una titulación

1. Crea el archivo `titulaciones/<SIGLA>/tema_N_nombre.md` siguiendo el número que le corresponde en el temario oficial de esa titulación.
2. Escribe el contenido siguiendo el estilo de la sección 4 (negrita para términos clave, tablas para comparativas, Mermaid si aporta claridad).
3. **Actualiza `titulaciones/<SIGLA>/INDEX.md`**: añade el enlace al nuevo tema en la lista numerada del temario, respetando el número de preguntas y las eliminatorias si las conoces con certeza (ver sección 9 sobre datos normativos).
4. Si la titulación tiene un `simulacro_examen.md` (o módulos de simulacro, como en CY), valora si el tema nuevo debería tener alguna pregunta de repaso allí. No es obligatorio en cada contribución, pero es bienvenido.
5. Si el tema nuevo es relevante también para otra titulación con temario compartido (por ejemplo, los temas 1–6 de PNB son iguales a los de PER), añade el enlace cruzado correspondiente en el `INDEX.md` de esa otra titulación en vez de duplicar el contenido.
6. Comprueba que el enlace desde `README.md` a esa titulación sigue siendo correcto si has cambiado la estructura general del índice.

---

## 6. Cómo añadir imágenes

- Las imágenes deben ser de **dominio público** o tener una **licencia libre compatible** (CC0, CC-BY, CC-BY-SA o equivalente). **Nunca subas una imagen con copyright sin haber verificado su licencia.** Ante la duda, no la subas.
- Guarda la imagen en `assets/images/` si es de uso general, o en un subdirectorio `img/` local si pertenece a una sola sección temática (como `nudos/img/`).
- Nombra el archivo en minúsculas con guiones bajos, describiendo el contenido (`sloop.jpg`, `as_de_guia.jpg`).
- Indica la **atribución** (autor, fuente y licencia) junto a la imagen en el propio texto, o en una sección "Créditos de imágenes" al final del documento si insertas varias imágenes con distintos orígenes. Por ejemplo:

  ```markdown
  ![Balandro (Sloop)](assets/images/sloop.jpg)
  *Fuente: Wikimedia Commons, autor XYZ, licencia CC-BY-SA 4.0.*
  ```

- Si generas o dibujas la imagen tú mismo/a y quieres cederla al proyecto, indícalo también ("Ilustración propia").

---

## 7. Cómo actualizar `CHANGELOG.md`

El proyecto sigue el formato [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/). Al contribuir:

1. Añade una línea nueva bajo la sección `## [Unreleased]` → `### Añadido` (o `### Corregido` / `### Cambiado` si esa contribución modifica o arregla algo existente en lugar de añadir contenido nuevo).
2. Redacta la línea en pasado y en el mismo estilo breve y descriptivo que las entradas existentes, mencionando el archivo o directorio afectado. Por ejemplo:
   - `- Añadido tema 14 (Corrientes de Marea) al temario del PER.`
   - `- Corregidas las prioridades de paso entre veleros en RIPA_Y_BALIZAMIENTO.md.`
3. No renombres ni borres entradas anteriores del changelog salvo que estés corrigiendo un error evidente en ellas.

---

## 8. Pasos para contribuir

1. Haz un **fork** del repositorio (o crea una rama si tienes acceso directo).
2. Crea una **rama descriptiva** para tu cambio, por ejemplo `feature/tema-corrientes-marea-per` o `fix/prioridad-paso-ripa`.
3. Realiza tus cambios siguiendo las convenciones de esta guía (estructura, nombrado, estilo, `INDEX.md` y `CHANGELOG.md`).
4. Revisa tu propio texto: ortografía, coherencia con el resto del documento, enlaces internos funcionando.
5. Abre un **pull request** describiendo qué añades o corriges y, si aplica, la fuente oficial que respalda el dato.
6. Espera la **revisión**: se puede pedir que cites la fuente de un dato normativo, que ajustes el formato o que dividas el PR si mezcla temas no relacionados. Los PR pequeños y centrados en un solo tema se revisan más rápido.
7. Si prefieres proponer un contenido antes de escribirlo entero, abre un **issue** primero.

---

## 9. Verificación de datos normativos

Cualquier dato con implicación legal o de examen —horas de prácticas, número de preguntas, criterios eliminatorios, esloras y distancias máximas, plazos, importes— **debe poder verificarse en una fuente oficial** (BOE, Orden Ministerial correspondiente, web de la Dirección General de la Marina Mercante, escuela homologada).

- Si puedes verificar el dato, valora citar la fuente (aunque sea de forma informal, "según el BOE X" o un enlace en `RECURSOS.md`).
- **Si no puedes verificar el dato con certeza, no lo inventes ni lo redondees a ojo.** Márcalo explícitamente en el texto, por ejemplo:

  ```markdown
  *(Dato pendiente de verificar en fuente oficial: número exacto de preguntas eliminatorias.)*
  ```

- Esto es especialmente importante porque el repositorio se usa para preparar exámenes oficiales: un dato incorrecto sin advertencia puede llevar a alguien a estudiar mal un criterio eliminatorio real.

---

Gracias de nuevo por contribuir. Cualquier aportación —una corrección de una línea, una imagen bien atribuida o un tema completo nuevo— ayuda a que la comunidad náutica tenga mejor material de estudio.
