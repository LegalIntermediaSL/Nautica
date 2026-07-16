# %% [markdown]
# # Simulación 2: Cálculo del Viento Aparente (Vectores)
# 
# En un velero, el viento que sientes en la cara (**Viento Aparente, Va**) no es el mismo que el viento que sopla realmente en el mar (**Viento Real, Vr**). 
# El viento aparente es la suma vectorial del Viento Real más el "Viento Relativo" (el viento generado por la propia velocidad del barco al avanzar, que siempre viene directo de proa).
# 
# Esta simulación calcula la intensidad y ángulo del viento aparente.

# %%
import numpy as np
import matplotlib.pyplot as plt
import math

def calcular_viento_aparente(v_real_nudos, angulo_v_real, v_barco_nudos):
    """
    Calcula el Viento Aparente usando componentes de vectores.
    Ángulo de 0º = Proa. Ángulo de 180º = Popa.
    """
    # Convertir ángulo a radianes
    theta_rad = math.radians(angulo_v_real)
    
    # Descomponer el viento real en X (transversal) e Y (longitudinal)
    vr_x = v_real_nudos * math.sin(theta_rad)
    vr_y = v_real_nudos * math.cos(theta_rad)
    
    # El viento relativo (generado por el barco) siempre entra por proa (Y negativo respecto a nosotros)
    # Por tanto, el viento que sentimos se suma a nuestro avance frontal
    va_x = vr_x
    va_y = vr_y + v_barco_nudos
    
    # Recomponer vector de viento aparente
    v_aparente_nudos = math.sqrt(va_x**2 + va_y**2)
    angulo_va_rad = math.atan2(va_x, va_y)
    
    # Normalizar a grados positivos
    angulo_va = (math.degrees(angulo_va_rad)) % 360
    
    return round(v_aparente_nudos, 1), round(angulo_va, 1)

# --- VARIABLES ---
viento_real = 15.0 # Nudos (knots)
angulo_viento_real = 90.0 # Entra por el través (90º a estribor)
velocidad_barco = 8.0 # Nudos

# %%
va, angulo_va = calcular_viento_aparente(viento_real, angulo_viento_real, velocidad_barco)

print(f"--- RESULTADOS ---")
print(f"Viento Real: {viento_real} nudos por el {angulo_viento_real}º")
print(f"Velocidad Barco: {velocidad_barco} nudos")
print(f"Viento Aparente Sentido: {va} nudos por el {angulo_va}º")
# Verás que el viento aparente siempre 'se cierra' hacia la proa (es decir, el ángulo es menor que el real)
