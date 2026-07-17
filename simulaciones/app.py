import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador Náutico", layout="wide")

st.title("Laboratorio de Simulaciones Náuticas ⚓")
st.markdown("Herramientas interactivas para cálculos físicos y astronómicos avanzados.")

tab1, tab2, tab3 = st.tabs(["Estabilidad Transversal", "Navegación Astronómica", "Cinemática del Viento"])

with tab1:
    st.header("Cálculo de Estabilidad Transversal (GM)")
    st.markdown("Simulación del par adrizante y la altura metacéntrica.")
    
    col1, col2 = st.columns(2)
    with col1:
        manga = st.slider("Manga (m)", 2.0, 15.0, 4.0)
        calado = st.slider("Calado (m)", 0.5, 5.0, 1.5)
        kg = st.slider("Centro de Gravedad (KG) (m)", 0.5, 5.0, 2.0)
    
    with col2:
        # Simplificación de BM para un casco prismático
        bm = (manga**2) / (12 * calado)
        kb = calado / 2
        km = kb + bm
        gm = km - kg
        
        st.metric("Altura Metacéntrica (GM)", f"{gm:.2f} m", delta="Estable" if gm > 0 else "Inestable", delta_color="normal" if gm > 0 else "inverse")
        
        # Plot GZ curve approximation
        angles = np.linspace(0, 60, 100)
        gz = gm * np.sin(np.radians(angles))
        
        fig, ax = plt.subplots()
        ax.plot(angles, gz, label="Brazo Adrizante (GZ)")
        ax.axhline(0, color='red', linestyle='--')
        ax.set_xlabel("Escora (grados)")
        ax.set_ylabel("GZ (m)")
        ax.set_title("Curva de Estabilidad Estática")
        st.pyplot(fig)

with tab2:
    st.header("Resolución del Triángulo de Posición (Marcq St. Hilaire)")
    st.markdown("Cálculo analítico del determinante astronómico.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        lat = st.number_input("Latitud Estimada (grados)", -90.0, 90.0, 36.0)
    with c2:
        dec = st.number_input("Declinación del Astro (grados)", -90.0, 90.0, 15.0)
    with c3:
        hl = st.number_input("Horario Local (grados)", 0.0, 360.0, 45.0)
        
    lat_r = np.radians(lat)
    dec_r = np.radians(dec)
    hl_r = np.radians(hl)
    
    sin_a = np.sin(lat_r) * np.sin(dec_r) + np.cos(lat_r) * np.cos(dec_r) * np.cos(hl_r)
    a_calc = np.degrees(np.arcsin(sin_a))
    
    st.success(f"Altura Calculada (a_c): {a_calc:.4f}°")
    st.latex(r"\sin(a) = \sin(l)\sin(d) + \cos(l)\cos(d)\cos(h_L)")

with tab3:
    st.header("Cinemática del Viento Aparente")
    v_barco = st.slider("Velocidad del barco (nudos)", 0.0, 30.0, 10.0)
    v_viento_real = st.slider("Velocidad del Viento Real (nudos)", 0.0, 50.0, 15.0)
    angulo_viento_real = st.slider("Ángulo del Viento Real (grados)", 0.0, 180.0, 45.0)
    
    ang_rad = np.radians(angulo_viento_real)
    vx = v_viento_real * np.sin(ang_rad)
    vy = v_viento_real * np.cos(ang_rad) + v_barco
    
    v_aparente = np.sqrt(vx**2 + vy**2)
    ang_aparente = np.degrees(np.arctan2(vx, vy))
    
    st.info(f"Viento Aparente: {v_aparente:.1f} nudos a {ang_aparente:.1f}° por la proa")
