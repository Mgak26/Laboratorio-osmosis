# streamlit_app.py

import streamlit as st

# Modelo simplificado de osmosis
sensitivity = {
    "Papa": 0.15,
    "Zanahoria": 0.10
}

def calcular_masa_final(vegetal, masa_inicial, concentracion, tiempo):
    factor = sensitivity[vegetal]
    delta = - factor * concentracion * (tiempo / 10)

    if concentracion == 0:
        delta = + factor * 0.05 * (tiempo / 10)

    masa_final = masa_inicial * (1 + delta)
    return max(0, masa_final)

# Título
st.title("🧪 Simulador de Osmosis en Tejido Vegetal")

# Explicación
st.markdown("""
Este simulador permite experimentar virtualmente el proceso de **osmosis** en trozos de papa o zanahoria 
sumergidos en soluciones de NaCl a distintas concentraciones.
""")

# Entradas del usuario
vegetal = st.selectbox("Seleccione el vegetal:", ["Papa", "Zanahoria"])

masa_inicial = st.number_input("Ingrese la masa inicial del vegetal (g):", min_value=0.1, max_value=500.0, value=50.0)

concentracion = st.selectbox("Seleccione la concentración de NaCl (g/mol):", [0.0, 0.2, 0.4, 0.6, 0.8])

tiempo = st.slider("Seleccione el tiempo de inmersión (min):", min_value=1, max_value=120, value=30)

# Botón de simulación
if st.button("Simular"):
    masa_final = calcular_masa_final(vegetal, masa_inicial, concentracion, tiempo)
    variacion = masa_final - masa_inicial
    st.success(f"✅ Masa final estimada: **{masa_final:.2f} g**")
    st.info(f"Variación de masa: **{variacion:+.2f} g**")
