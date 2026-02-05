import streamlit as st
from auxiliar.lateral import barra
from auxiliar.texto import separador

st.image(r"assets/painel.png", caption="", width="stretch")                                            # Adicona a logomarca.

separador()

st.markdown("<h1 style = 'text-align:center;font-size:40px;'>Em construção!</h1>",        
            unsafe_allow_html = True)                                                                       # Cria o titulo da pagina 
barra()



