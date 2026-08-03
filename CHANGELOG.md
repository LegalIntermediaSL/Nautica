# Changelog

Todos los cambios notables de este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).

## [Unreleased]

### Añadido (Ampliación Ronda 9: Laboratorio Computacional Náutico)
- **Simulaciones (31-40):** Creación de 10 nuevos simuladores Python orientados a Ingeniería Naval, Logística y SAR.
  - Diseño y Teoría del buque: `36_calculo_areas_velicas_ce_cv.ipynb` (Centro Vélico/Deriva), `40_calculo_velocidad_maxima_casco.ipynb` (Hull Speed/Froude), `33_calculo_calados_carga_estiba.ipynb` (TPC e inmersión), `34_simulador_esfuerzo_jarcia_firme.ipynb` (Fatiga del mástil).
  - Logística y Operaciones: `32_simulador_coste_combustible_ruta.ipynb` (Optimización económica de crucero), `38_calculo_consumo_agua_dulce.ipynb` (Autonomía y potabilizadora).
  - Seguridad y Reglamentos (RIPA/GMDSS): `35_simulador_senales_acusticas_niebla.ipynb`, `39_simulador_frecuencias_vhf_gmdss.ipynb` (Zonas A1-A4).
  - Búsqueda y Navegación Visual: `37_simulador_rescate_hombre_al_agua.ipynb` (Patrón SAR Expanding Square), `31_calculo_distancia_horizonte_visual.ipynb` (Alcance faros).

### Añadido (Ampliación Ronda 8: Gran Expansión de Simuladores Jupyter)
- **Simulaciones (22-30):** Inyección masiva de 9 nuevos simuladores interactivos en Python en el directorio `simulaciones/`.
  - Cinemática y Vectores: `25_calculo_deriva_abatimiento.ipynb` (Rumbo Efectivo) y `23_navegacion_ortodromica_derrotero.ipynb` (Círculo Máximo).
  - Reglamentos: `28_simulador_luces_ripa.ipynb` (identificación cruzada de sectores).
  - Mareas y Física: `29_prediccion_mareas_armonicas.ipynb` (modelo M2/S2) y `30_calculo_calado_aguas_someras.ipynb` (Efecto Squat).
  - Maniobra y Sistemas: `24_simulador_fuerza_viento_velas.ipynb` (fuerza aerodinámica y rizos), `26_simulador_baterias_lifepo4.ipynb` (curva SOC y efecto Peukert), `27_maniobra_fondeo_calculo_cadena.ipynb` (Catenaria), `22_calculo_desvio_aguja.ipynb`.

### Añadido (Ampliación Ronda 7: SOPs médicos, mecánica de supervivencia y meteorología local)
- **Medicina avanzada:** nuevo `MEDICINA_Y_PRIMEROS_AUXILIOS.md` (SOPs para RCP en mar, evacuación aeromédica Helimer, gestión de botiquines según zona, hipotermia y mareo severo).
- **Mecánica de emergencia:** nuevo `MECANICA_DIESEL_MARINO.md` (SOPs para purgado del circuito de gasoil, cambio del rodete de refrigeración/impeller y diagnóstico rápido por color de humo).
- **Meteorología Local:** nuevo `METEOROLOGIA_LOCAL_IBERICA.md` (Vientos característicos de la península, brisas térmicas terral/virazón, e interpretación del barómetro y el cielo para predecir turbonadas).

### Añadido (Ampliación Ronda 4: profundización, nuevos huecos y auditoría de calidad)
- **Averías en travesía:** nuevo `AVERIAS_EN_TRAVESIA.md` (checklist de decisión en el momento ante fallo total de electrónica/instrumentos, rotura de jarcia o vela, vía de agua no localizada y fallo de gobierno/timón, con navegación de respaldo y criterios para desviarse a puerto o pedir asistencia), enlazado desde `README.md`.
- **Drones:** nuevo `NORMATIVA_DRONES.md` (categorías de operación AESA/UE, registro de operador, restricciones en el entorno marino, consejos de vuelo desde cubierta, seguro de RC específico).
- **Táctica de regata:** nuevo `TACTICA_METEOROLOGICA_REGATA.md` (rachas persistentes vs. oscilantes, regla favorable/desfavorable en ceñida, efecto de costa, sesgo de línea de salida, efecto táctico de corrientes).
- **Titulación PY:** los 4 temas ampliados a nivel intermedio entre PER y CY (supervivencia en balsa, corrientes oceánicas, Regla de los Doceavos, problema completo de estima analítica y gráfica).
- **Seguridad y sanidad:** `SEGURIDAD.md` ampliado (abandono de buque, supervivencia en balsa, grab bag); `PRIMEROS_AUXILIOS.md` ampliado (fracturas/esguinces, ahogamiento y semi-ahogamiento, botiquín mínimo recomendado).
- **Puertos:** `puertos/MEDITERRANEO.md` y `puertos/ATLANTICO.md` ampliados con una sección de calas y fondeos de interés (Macarelleta, Es Vedrà, Cíes, Ons...), remitiendo a `MEDIOAMBIENTE.md` para la normativa de acceso restringido.
- **Imágenes:** diagrama de configuración de luces de navegación de un buque de motor (dominio público) en `RIPA_Y_BALIZAMIENTO.md`.
- **Auditoría de calidad y coherencia:** revisión cruzada de los ~105 archivos Markdown del repositorio. Corregidos 6 enlaces de temario de `titulaciones/PNB/INDEX.md` que apuntaban por error a `PER/` en vez de a los archivos propios de PNB; enlazados 2 archivos huérfanos de `titulaciones/LN/`; añadido enlace de temario completo desde `TITULOS_NAUTICOS.md` a cada `INDEX.md` de titulación; corregida una contradicción legal en `TITULOS_NAUTICOS.md` sobre la atribución del PER en Baleares (el PER base permite saltos entre islas del archipiélago, no el cruce Península-Baleares, que exige el "PER Ampliado"); unificada la terminología de las marcas cardinales Este/Oeste entre `RIPA_Y_BALIZAMIENTO.md`/PNB y PER (rombo/huevo, reloj de arena/copa de vino).
- README.md y CHANGELOG.md actualizados.

### Añadido (Ampliación Ronda 3: nuevos huecos temáticos)
- **Nudos:** nuevo `nudos/EMPALMES.md` (splicing en cabo de 3 cordones y trenzado moderno/Dyneema, forrado), enlazado desde `nudos/INDEX.md`.
- **Motos de agua:** nueva guía `MOTOS_DE_AGUA.md` (clasificación por clase de potencia y titulación exigida, normativa de navegación, cabo de hombre muerto, riesgo del chorro a presión, protocolo de vuelco), enlazada desde `README.md` y `titulaciones/LN/INDEX.md`.
- **Regatas y clubes:** nuevo `REGATAS_Y_CLUBES.md` (RFEV, licencia federativa, clases Optimist/ILCA/420/470/Snipe/ORC, club náutico, Comité de Regatas/Protestas, grandes regatas oceánicas).
- **Mantenimiento de velamen:** nuevo `MANTENIMIENTO_DE_VELAS_Y_JARCIA.md` (materiales de vela, cuidado e invernaje, cabo moderno Dyneema/Nylon, jarcia firme, winches).
- **Titulación LN:** ampliada con glosario básico ilustrado, consejos del curso y "las 3 cosas que debes saber del RIPA" para un principiante absoluto.
- **Comunicaciones:** `COMUNICACIONES_Y_BANDERAS.md` ampliado con DSC/tecla DISTRESS, protocolo de uso del Canal 16 y gestión de falsas alarmas MMSI.
- **Meteorología:** imágenes de la escala de Beaufort completa y de los símbolos estándar de frentes (Wikimedia Commons, con atribución).
- README.md y CHANGELOG.md actualizados.

### Añadido (Ampliación Fases 1-5)
- **Fase 1 (Fundamentos):** `GLOSARIO.md` (glosario náutico ES-EN de 150+ términos), nuevo itinerario `titulaciones/PPER/` (Patrón Profesional de Embarcaciones de Recreo, construido sobre CY según normativa vigente), `titulaciones/BANCO_PREGUNTAS.md` (repaso cruzado por materia de todos los simulacros) y auditoría/corrección de enlaces externos rotos en `RECURSOS.md` y `cartas_nauticas/INDEX.md`.
- **Fase 2 (Profundización):** Ampliación de `SEGURIDAD.md` (lucha contraincendios, vías de agua) con nuevo manual `PROTOCOLO_HOMBRE_AL_AGUA.md`; ampliación de `MECANICA_Y_MANTENIMIENTO.md` (diagnóstico de averías, energía solar/eólica/watermaker, gas GLP); ampliación de `ELECTRONICA_NAVAL.md` (EPIRB/PLB/AIS-SART, Starlink/Iridium, NMEA 2000); ampliación de `METEOROLOGIA.md` (lectura de GRIB, mapas isobáricos, ciclones tropicales); ampliación de `VELA.md` (Reglamento de Regatas RRV) y `VELA_TIPOS_Y_APAREJOS.md` (spinnaker/gennaker, multicascos).
- **Fase 3 (Nuevas secciones transversales):** `CHARTER.md`, `FISCALIDAD_Y_MATRICULACION.md`, `MEDIOAMBIENTE.md`, `PESCA_RECREATIVA.md`, `FAQ.md`.
- **Fase 4 (Laboratorio):** Notebooks `14_lectura_grib.ipynb`, `15_consumo_combustible_autonomia.ipynb`, `16_curva_polar_velero.ipynb` y `17_generador_test_aleatorio.ipynb`.
- **Fase 5 (Calidad):** `CONTRIBUTING.md` con las convenciones de estilo del repositorio.
- **Imágenes libres de derechos (Wikimedia Commons):** cartas estelares de navegación (Bowditch, dominio público) y tabla de las 57 estrellas de navegación en `titulaciones/CY/tema_3_teoria_astronomica.md`; mapa de regiones IALA A/B en `RIPA_Y_BALIZAMIENTO.md`; Código Internacional de Señales completo (banderas, semáforo, Morse) en `COMUNICACIONES_Y_BANDERAS.md`; tipos de ancla en `MANIOBRAS_Y_FONDEO.md`; esquema de sextante en `titulaciones/CY/tema_4_calculos_astronomicos.md`. Todas con atribución de autor y licencia junto a la imagen.
- **Stellarium:** referencia al planetario de código abierto en `RECURSOS.md` y en `titulaciones/CY/tema_3_teoria_astronomica.md` como herramienta de estudio para identificación de estrellas de navegación.
- README.md actualizado enlazando todo el contenido nuevo.

### Añadido (Ampliación Ronda 2: profundización y nuevas guías)
- **Faros:** `faros/FAROS_ESPAÑA.md` reescrito con un directorio real por Comunidad Autónoma (antes estaba prácticamente vacío).
- **Vela práctica:** `VELA_TUTORIAL_PRACTICO.md` ampliado con fondeo a vela, atraque a vela sin motor, ejecución física del MOB a vela y navegación segura en popa redonda.
- **Puertos:** `puertos/INTERNACIONALES.md` ampliado con Gibraltar y Azores/Cabo Verde como hubs oceánicos.
- **Cartas náuticas:** los 4 documentos de `cartas_nauticas/` ampliados con proyección Mercator, más simbología IALA/INT1, y problemas resueltos paso a paso de deriva por viento, estima analítica completa y Regla de los Doceavos.
- **Nudos:** añadido el As de Guía por Seno y ampliado uso práctico en `TOPE.md`/`AMARRE.md`; nuevo Nudo Zeppelin en `UNION.md`; nuevo Nudo Constrictor en `OTROS.md`.
- **Gestiones y seguros:** `GESTIONES_Y_DOCUMENTACION.md` ampliado (Rol de Despacho, Libreta de Inscripción Marítima, zarpe internacional); nuevo `SEGUROS_NAUTICOS.md`.
- **Nuevas guías:** `VIENTOS_LOCALES_ESPAÑA.md` (Tramontana, Mistral, Levante, Siroco, Terral, Galerna...), `COMPRA_VENTA_EMBARCACION.md` (survey, documentación, transmisión), `VIDA_A_BORDO.md` (agua, provisioning, guardias, convivencia), `HISTORIA_DE_LA_NAVEGACION.md` (de la estima primitiva al GPS).
- **Carta de examen PER:** `titulaciones/PER/tema_11_carta_navegacion.md` ampliado con 3 problemas completos resueltos paso a paso sobre la Carta 105 del Estrecho de Gibraltar.
- **Más imágenes Wikimedia Commons:** rosa de rumbos respecto al viento y diagrama numerado de partes de un velero en `VELA.md`/`VELA_TIPOS_Y_APAREJOS.md`, con atribución.
- README.md y CHANGELOG.md actualizados.

### Añadido
- Creación de la estructura básica del repositorio.
- Actualización del archivo `README.md` con descripción general y estructura del proyecto.
- Creación del archivo `CHANGELOG.md` para el registro de cambios.
- Creación del archivo `BITACORA.md` como plantilla de diario de navegación.
- Creación del archivo `TITULOS_NAUTICOS.md` como índice de las titulaciones de recreo en España.
- Creación del directorio `titulaciones/` con documentos específicos detallados para cada título (LN, PNB, PER, PY, CY).
- Inclusión de nuevo contenido general: `NUDOS_NAUTICOS.md`, `VELA.md`, `METEOROLOGIA.md` y `SEGURIDAD.md`.
- Creación de artículo sobre las [Tarjetas Náuticas de Legal Intermedia S.L.](TARJETAS_NAUTICAS.md) y añadido enlace en el README.
- Reestructuración profunda: Creación de directorios para `cartas_nauticas/` y `nudos/` (con imágenes y enlaces a vídeos).
- Reestructuración de `titulaciones/` creando una carpeta por título para albergar sus temarios completos.
- Añadidos primeros temas de ejemplo del PER (Nomenclatura, Amarre, Balizamiento).
- Añadidas secciones de `RECURSOS.md` y `FORMACION_Y_CURSOS.md`.
- Creación de base de datos automatizada de `faros/` con el listado de todos los faros de España y su señalización.
- Creación de directorio `puertos/` con un listado estructurado de los principales puertos deportivos por Comunidad Autónoma.
- **Gran Inyección de Diagramas (Mermaid)**: Inserción de organigramas y esquemas visuales en los principales documentos de teoría (Balizamiento, Seguridad, Nomenclatura, Nudos, Meteorología).
- Creación del laboratorio virtual en `simulaciones/` con scripts interactivos (estilo Jupyter) para cálculo vectorial náutico en Python (viento aparente y corrección total).
