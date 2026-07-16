# %% [markdown]
# # Simulación 1: Cálculo de Rumbo Verdadero y Corrección Total
# 
# En navegación costera, el rumbo que marca nuestro compás (Rumbo de Aguja o Ra) casi nunca coincide con el rumbo real sobre la carta náutica (Rumbo Verdadero o Rv). 
# Esto se debe a dos errores magnéticos que, sumados, forman la **Corrección Total (Ct)**:
# 1. **Declinación Magnética (dm):** Diferencia entre el Norte Geográfico y el Norte Magnético terrestre.
# 2. **Desvío de Aguja (Δ):** Error magnético propio de nuestro barco (hierros, electrónica).
# 
# La fórmula fundamental es: **Rv = Ra + Ct** (donde **Ct = dm + Δ**)

# %%
import numpy as np
import matplotlib.pyplot as plt

def calcular_rumbo_verdadero(ra, dm, desvio):
    """
    Calcula el Rumbo Verdadero dados el Rumbo de Aguja, Declinación y Desvío.
    Los valores Hacia el ESTE (E) o Norte (+) son POSITIVOS.
    Los valores Hacia el OESTE (W) o Sur (-) son NEGATIVOS.
    """
    ct = dm + desvio
    rv = (ra + ct) % 360  # %360 asegura que el rumbo se mantenga entre 0 y 359
    return rv, ct

# --- VARIABLES DEL PROBLEMA ---
rumbo_aguja = 45.0  # Vamos navegando al 045º
declinacion_magnetica = -2.5 # 2.5º Oeste (Negativo)
desvio = 1.0 # 1.0º Este (Positivo)

# %%
# Realizamos el cálculo
rv, ct = calcular_rumbo_verdadero(rumbo_aguja, declinacion_magnetica, desvio)

print(f"--- RESULTADOS ---")
print(f"Rumbo de Aguja (Ra): {rumbo_aguja}º")
print(f"Corrección Total (Ct): {ct}º")
print(f"Rumbo Verdadero (Rv): {rv}º")

# %% [markdown]
# ## Visualización Polar (Rosa de los Vientos)
# Vamos a visualizar gráficamente la diferencia entre hacia dónde apunta la proa (Rv) y hacia dónde apunta la aguja magnética (Ra).

# %%
# Configuración del gráfico polar
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_theta_zero_location("N") # El Norte arriba (0 grados)
ax.set_theta_direction(-1) # Sentido horario (como una brújula)

# Convertir grados a radianes para matplotlib
ra_rad = np.radians(rumbo_aguja)
rv_rad = np.radians(rv)

# Dibujar vectores
ax.annotate('', xy=(ra_rad, 1), xytext=(0, 0),
            arrowprops=dict(facecolor='red', edgecolor='red', width=2, headwidth=10))
ax.annotate('', xy=(rv_rad, 1), xytext=(0, 0),
            arrowprops=dict(facecolor='blue', edgecolor='blue', width=2, headwidth=10))

# Leyendas y formato
ax.set_yticklabels([]) # Ocultar anillos de radio
ax.set_title("Rosa de los Vientos: Ra (Rojo) vs Rv (Azul)\n", va='bottom')
ax.set_xticks(np.radians([0, 45, 90, 135, 180, 225, 270, 315]))
ax.set_xticklabels(['N (0º)', 'NE (45º)', 'E (90º)', 'SE (135º)', 'S (180º)', 'SW (225º)', 'W (270º)', 'NW (315º)'])

plt.figtext(0.15, 0.15, f"Ct: {ct}º", color='purple', weight='bold')
plt.show()
