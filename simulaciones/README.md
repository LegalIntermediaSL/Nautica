# Simulaciones Interactivas (Laboratorio Python)

Este directorio contiene cuadernos interactivos (scripts de Python) diseñados para realizar cálculos náuticos complejos y simulaciones. Es un "laboratorio" digital ideal para preparar problemas de navegación y entender conceptos abstractos.

## ¿Por qué Python?

El cálculo de rumbos, mareas y vectores de viento es matemáticas pura. Usar Python (y librerías científicas como `numpy` y visualizaciones como `matplotlib`) permite:
*   Resolver problemas de la carta de forma programática.
*   Visualizar gráficos polares (rosas de los vientos) para entender rumbos.
*   Calcular trigonometría de vectores (viento aparente vs verdadero).

## Instalación y Uso

Los archivos de este directorio están en formato **Jupyter Notebook (`.ipynb`)**. Para utilizarlos:
1.  **En Visual Studio Code:** Simplemente abre el archivo `.ipynb` e instala la extensión "Jupyter" de Microsoft si el editor te lo pide. Podrás ejecutar las celdas una a una.
2.  **En el navegador:** Puedes instalar JupyterLab ejecutando `pip install jupyterlab` y luego `jupyter lab` en este directorio.

### Requisitos
Para usar estos cuadernos en tu entorno local, asegúrate de instalar las librerías matemáticas y gráficas:
```bash
pip install -r requirements.txt
```

## Simulaciones Disponibles

*   **[`01_calculo_rumbo_verdadero.ipynb`](01_calculo_rumbo_verdadero.ipynb):** Conversión de Rumbo de Aguja (Ra) a Rumbo Verdadero (Rv) aplicando Corrección Total (Declinación Magnética + Desvío).
*   **[`02_viento_aparente.ipynb`](02_viento_aparente.ipynb):** Cálculo vectorial del viento aparente (el que sienten las velas) a partir del viento real y la velocidad/rumbo del barco.
*   **[`03_estabilidad_transversal.ipynb`](03_estabilidad_transversal.ipynb):** Gráficos del par de adrizamiento (GZ) y comportamiento del centro de gravedad (G) y de carena (C) al escorar.
*   **[`04_triangulo_astronomico.ipynb`](04_triangulo_astronomico.ipynb):** Resolución trigonométrica del triángulo de posición esférico (Polo, Cenit, Astro).
*   **[`05_ortodromica_vs_loxodromica.ipynb`](05_ortodromica_vs_loxodromica.ipynb):** Comparación matemática y gráfica entre el rumbo constante y la distancia más corta (círculo máximo) para cruces oceánicos.
*   **[`06_latitud_polaris.ipynb`](06_latitud_polaris.ipynb):** Cálculo de la latitud del observador mediante la altura instrumental de la Estrella Polar (CY).
*   **[`07_cinematica_radar.ipynb`](07_cinematica_radar.ipynb):** Rosa de Maniobras, cálculo de CPA (Closest Point of Approach) y TCPA.
*   **[`08_generador_mareas.ipynb`](08_generador_mareas.ipynb):** Análisis armónico de mareas y cálculo de sondas en puertos (Problemas directos e inversos PY/CY).
*   **[`09_marcq_st_hilaire.ipynb`](09_marcq_st_hilaire.ipynb):** Cálculo del Determinante (Diferencia de Alturas y Azimut) para trazar la Recta de Altura (Navegación astronómica CY).
*   **[`10_identificacion_astros.ipynb`](10_identificacion_astros.ipynb):** Star Finder electrónico. Resuelve el triángulo esférico inverso para identificar estrellas desconocidas a partir de altura y azimut.
*   **[`11_triangulo_velocidades.ipynb`](11_triangulo_velocidades.ipynb):** Resolución vectorial del problema de corrientes. Calcula gráficamente el Rumbo Efectivo (Ref) y la Velocidad Efectiva (Vef) a partir del rumbo del barco y la corriente marina (PY).
*   **[`12_latitud_meridiana_sol.ipynb`](12_latitud_meridiana_sol.ipynb):** [NUEVO] Cálculo de la Latitud por la Altura Meridiana del Sol. La típica pregunta de examen de Capitán de Yate resuelta y graficada mostrando el corte del meridiano y las distancias cenitales.
*   **[`13_correccion_total_amplitud.ipynb`](13_correccion_total_amplitud.ipynb):** [NUEVO] Cálculo de la Corrección Total (Ct) mediante la observación de la Amplitud del Sol al Orto o al Ocaso (Navegación Astronómica CY). Incluye brújula polar visualizando Zv vs Za.
*   **[`14_lectura_grib.ipynb`](14_lectura_grib.ipynb):** [NUEVO] Aproximación didáctica a la lectura de mapas de viento tipo GRIB/Windy. Genera una rejilla sintética de isobaras y vectores de viento alrededor de una borrasca y los visualiza con `quiver`/`streamplot`.
*   **[`15_consumo_combustible_autonomia.ipynb`](15_consumo_combustible_autonomia.ipynb):** [NUEVO] Calculadora de autonomía a motor. A partir del depósito, la reserva de seguridad y la curva de consumo (l/h), calcula y grafica las millas náuticas de autonomía frente a la velocidad de crucero.
*   **[`16_curva_polar_velero.ipynb`](16_curva_polar_velero.ipynb):** [NUEVO] Curva polar de velocidad de un velero de crucero para distintos ángulos e intensidades de viento real, graficada en coordenadas polares, con cálculo del VMG óptimo al ceñir y al largo.
*   **[`17_generador_test_aleatorio.ipynb`](17_generador_test_aleatorio.ipynb):** [NUEVO] Generador de examen tipo test con un banco de preguntas de Balizamiento, RIPA y Nomenclatura. Selecciona preguntas aleatorias con `random.sample`, corrige y evalúa los criterios eliminatorios del PER.
*   **[`18_cpa_tcpa_radar.ipynb`](18_cpa_tcpa_radar.ipynb):** [NUEVO] Cinemática Radar (Cálculo Analítico de CPA y TCPA). Trazado vectorial de la línea de movimiento relativo de un contacto (blanco) para predecir tiempo y distancia de máxima aproximación.
*   **[`19_calculo_mareas_puerto_secundario.ipynb`](19_calculo_mareas_puerto_secundario.ipynb):** [NUEVO] Resolución del problema de mareas para Puertos Secundarios usando diferencias horarias y de amplitud del Anuario de Mareas, con gráfico sinusoidal de la regla de los doceavos.
