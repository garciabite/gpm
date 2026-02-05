import streamlit as st

def cor():
    # Criando um botão para alternar entre os temas
    modo_escuro = st.toggle("Modo Dark", value=True)  # Começa ativado para Dark Mode

# Definindo a cor do texto dinamicamente
    cor_texto = "white" if modo_escuro else "black"