# Simulaciones Interactivas (Laboratorio Python)

Este directorio contiene cuadernos interactivos (scripts de Python) diseñados para realizar cálculos náuticos complejos y simulaciones. Es un "laboratorio" digital ideal para preparar problemas de navegación y entender conceptos abstractos.

## ¿Por qué Python?

El cálculo de rumbos, mareas y vectores de viento es matemáticas pura. Usar Python (y librerías científicas como `numpy` y visualizaciones como `matplotlib`) permite:
*   Resolver problemas de la carta de forma programática.
*   Visualizar gráficos polares (rosas de los vientos) para entender rumbos.
*   Calcular trigonometría de vectores (viento aparente vs verdadero).

## Instalación y Uso

Los archivos de este directorio están en formato de **Script Interactivo de Python (`.py` con celdas `# %%`)**. Pueden ejecutarse de dos maneras:
1.  **Como un Jupyter Notebook en VSCode:** Simplemente abre el archivo `.py` en Visual Studio Code (con la extensión de Python y Jupyter instaladas) y haz clic en "Run Cell" encima de las marcas `# %%`.
2.  **Desde la terminal:** Ejecutando `python 01_calculo_rumbo_verdadero.py`.

### Requisitos
Para usar estos cuadernos, debes tener instalado Python y las dependencias indicadas:
```bash
pip install -r requirements.txt
```

## Simulaciones Disponibles

*   **[`01_calculo_rumbo_verdadero.py`](01_calculo_rumbo_verdadero.py):** Conversión de Rumbo de Aguja (Ra) a Rumbo Verdadero (Rv) aplicando Corrección Total (Declinación Magnética + Desvío). Incluye visualización en gráfico polar.
*   **[`02_viento_aparente.py`](02_viento_aparente.py):** Cálculo vectorial del viento aparente (el que sienten las velas) a partir del viento real y la velocidad/rumbo del barco.
