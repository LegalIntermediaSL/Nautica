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
