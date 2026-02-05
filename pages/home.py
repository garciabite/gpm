import streamlit as st
import time
from auxiliar.mapa import mapa
from auxiliar.texto import resumo, aplicacao, texto_mapa, separador
from auxiliar.lateral import barra

st.set_page_config(page_title="GPM - Mecânico", layout="wide", page_icon="⚙")


# >>> Ocultar barra superior SOMENTE nesta página
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("""
    <h1 style="text-align:center; font-size:40px;">GPM - GESTÃO DE PROJETOS MEBRAFE</h1>
""", unsafe_allow_html=True)

separador()

# Inicializa estado
if 'slide_index' not in st.session_state:
    st.session_state.slide_index = 0

# Placeholder para os slides
slide_container = st.empty()

# Lógica de apresentação de slides
with slide_container.container():
    slide = st.session_state.slide_index

    if slide == 0:
        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/fluxo.png", width="stretch")
        with col2:
            resumo()

    elif slide == 1:
        col3, col4 = st.columns(2)
        with col3:
            texto_mapa()
        with col4:
            mapa()

    elif slide == 2:
        col5, col6 = st.columns(2)
        with col5:
            st.image("assets/tcm.png", width=600)
        with col6:
            aplicacao()

# A parte que faz ele "rodar"
time.sleep(10)  # Espera 10 segundos
st.session_state.slide_index = (st.session_state.slide_index + 1) % 3
st.rerun()

# Elementos fixos
separador()
st.image("assets/simulacao.gif", width="stretch")
barra()



