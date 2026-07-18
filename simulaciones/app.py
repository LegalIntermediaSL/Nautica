import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador Náutico", layout="wide")

st.title("Laboratorio de Simulaciones Náuticas ⚓")
st.markdown("Herramientas interactivas para cálculos físicos y astronómicos avanzados.")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Estabilidad Transversal", "Navegación Astronómica", "Cinemática del Viento", "Ortodrómica vs Loxodrómica", "Latitud Polaris", "Cinemática Radar", "Generador de Mareas"])

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

with tab4:
    st.header("Navegación Ortodrómica vs Loxodrómica (CY)")
    st.markdown("Comparativa de distancias para cruceros transoceánicos.")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Punto de Salida")
        l1 = st.number_input("Latitud Salida", -90.0, 90.0, 35.0)
        L1 = st.number_input("Longitud Salida", -180.0, 180.0, -10.0)
    with col_b:
        st.subheader("Punto de Llegada")
        l2 = st.number_input("Latitud Llegada", -90.0, 90.0, 40.0)
        L2 = st.number_input("Longitud Llegada", -180.0, 180.0, -70.0)
    
    dl = np.radians(l2 - l1)
    dL = np.radians(L2 - L1)
    l1_r = np.radians(l1)
    l2_r = np.radians(l2)
    
    # Ortodrómica
    cos_D = np.sin(l1_r)*np.sin(l2_r) + np.cos(l1_r)*np.cos(l2_r)*np.cos(dL)
    # Evitar errores de redondeo
    cos_D = min(1.0, max(-1.0, cos_D))
    dist_orto = np.degrees(np.arccos(cos_D)) * 60.0
    
    # Loxodrómica (aproximación por latitudes medias para distancias que no cruzan el ecuador)
    lm = np.radians((l1+l2)/2)
    apartamiento = np.degrees(dL) * 60.0 * np.cos(lm)
    dif_lat_millas = (l2 - l1) * 60.0
    dist_loxo = np.sqrt(dif_lat_millas**2 + apartamiento**2)
    
    st.metric("Distancia Ortodrómica (Círculo Máximo)", f"{dist_orto:.1f} millas")
    st.metric("Distancia Loxodrómica (Rumbo Constante)", f"{dist_loxo:.1f} millas")
    st.success(f"Ahorro navegando por Ortodrómica: {dist_loxo - dist_orto:.1f} millas")

with tab5:
    st.header("Latitud por la Estrella Polar (CY)")
    st.markdown("Cálculo aproximado para el Hemisferio Norte usando el $hL\\gamma$.")
    
    c_p1, c_p2 = st.columns(2)
    with c_p1:
        av_polar = st.number_input("Altura Verdadera Polaris ($a_v$)", 0.0, 90.0, 36.5)
    with c_p2:
        hl_aries = st.number_input("Ángulo Horario Local de Aries ($hL\\gamma$)", 0.0, 360.0, 145.0)
        
    # Fórmulas de corrección simplificadas basadas en el Almanaque Náutico
    # El término principal es - p * cos(hL_aries) donde p = co-declinación de polaris (~0.73 grados)
    p_deg = 0.73 
    hl_rad = np.radians(hl_aries)
    
    correccion_principal = - p_deg * np.cos(hl_rad)
    lat_calculada = av_polar + correccion_principal
    
    st.info(f"Latitud Observada ($l_v$): {lat_calculada:.2f}° N")
    st.latex(r"l_v \approx a_v - p \cdot \cos(h_{L\gamma})")

with tab6:
    st.header("Cinemática de Derrota: Corriente y Abatimiento (CY)")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        rs = st.number_input("Rumbo de Superficie ($R_s$)", 0.0, 360.0, 90.0)
        vb = st.number_input("Velocidad de Buque ($V_b$)", 0.0, 30.0, 10.0)
    with col_c2:
        rc = st.number_input("Rumbo de Corriente ($R_c$)", 0.0, 360.0, 180.0)
        ihc = st.number_input("Intensidad Corriente ($I_{hc}$)", 0.0, 10.0, 3.0)
        
    rs_rad = np.radians(rs)
    rc_rad = np.radians(rc)
    
    vx_eff = vb * np.sin(rs_rad) + ihc * np.sin(rc_rad)
    vy_eff = vb * np.cos(rs_rad) + ihc * np.cos(rc_rad)
    
    ref = np.degrees(np.arctan2(vx_eff, vy_eff))
    if ref < 0:
        ref += 360
    vef = np.sqrt(vx_eff**2 + vy_eff**2)
    
    st.metric("Rumbo Efectivo ($R_{ef}$)", f"{ref:.1f}°")
    st.metric("Velocidad Efectiva ($V_{ef}$)", f"{vef:.1f} nudos")

with tab7:
    st.header("Generador Sinusoidal de Mareas (PY)")
    st.markdown("Cálculo paramétrico de la sonda en cualquier instante usando la onda senoidal.")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        hora_bm = st.time_input("Hora de Bajamar (BM)", value=None)
        sonda_bm = st.number_input("Sonda Bajamar (m)", 0.0, 15.0, 1.2)
    with col_t2:
        hora_pm = st.time_input("Hora de Pleamar (PM)", value=None)
        sonda_pm = st.number_input("Sonda Pleamar (m)", 0.0, 15.0, 3.8)
        
    if hora_bm and hora_pm:
        import datetime as dtm
        from datetime import datetime, date
        dt_bm = datetime.combine(date.today(), hora_bm)
        dt_pm = datetime.combine(date.today(), hora_pm)
        
        # Asumimos que ocurren en el mismo día y BM es antes que PM para simplificar
        if dt_pm < dt_bm:
            dt_pm += dtm.timedelta(days=1)
            
        duracion_horas = (dt_pm - dt_bm).total_seconds() / 3600.0
        amplitud = sonda_pm - sonda_bm
        
        st.write(f"**Duración de la vaciante/creciente:** {duracion_horas:.2f} horas | **Amplitud:** {amplitud:.2f} m")
        
        # Ploteo de la onda
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates
        
        tiempos = [dt_bm + dtm.timedelta(hours=(duracion_horas * i / 100)) for i in range(101)]
        sondas = []
        for t in tiempos:
            dt_hours = (t - dt_bm).total_seconds() / 3600.0
            # Fórmula sinusoidal del Anuario: S = S_BM + Amplitud * sin^2(90 * t / duracion)
            # En radianes:
            angulo = np.radians(90 * dt_hours / duracion_horas)
            sondas.append(sonda_bm + amplitud * (np.sin(angulo)**2))
            
        fig2, ax2 = plt.subplots()
        ax2.plot(tiempos, sondas, color="teal", linewidth=2)
        ax2.set_xlabel("Hora")
        ax2.set_ylabel("Sonda (m)")
        ax2.set_title("Curva de Marea (Aproximación Sinusoidal)")
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax2.grid(True, linestyle='--', alpha=0.6)
        st.pyplot(fig2)
