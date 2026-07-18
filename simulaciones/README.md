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

*   **[`01_calculo_rumbo_verdadero.ipynb`](01_calculo_rumbo_verdadero.ipynb):** Conversión de Rumbo de Aguja (Ra) a Rumbo Verdadero (Rv) aplicando Corrección Total (Declinación Magnética + Desvío). Incluye visualización en gráfico polar.
*   **[`02_viento_aparente.ipynb`](02_viento_aparente.ipynb):** Cálculo vectorial del viento aparente (el que sienten las velas) a partir del viento real y la velocidad/rumbo del barco.
*   **[`07_cinematica_radar.ipynb`](07_cinematica_radar.ipynb)**: Rosa de Maniobras, cálculo de CPA y TCPA.
*   **[`08_generador_mareas.ipynb`](08_generador_mareas.ipynb)**: Análisis armónico de mareas y cálculo de sondas en puertos (PY/CY).
*   **[`09_marcq_st_hilaire.ipynb`](09_marcq_st_hilaire.ipynb)**: Cálculo del Determinante (Diferencia de Alturas y Azimut) para la Recta de Altura (CY).
