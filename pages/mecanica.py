import streamlit as st
from auxiliar.lateral import barra
from calculo.tcm import mecanica_resumo,mecanica_rosca,mecanica_prioridade, dados_clientes,resumo_ctu
from auxiliar.texto import legenda, separador

st.image(r"assets/painel.png", caption="", width="stretch")                                            # Adicona a logomarca.

separador()

barra()

coluna1, coluna2 = st.columns(2)

with coluna1:
    mecanica_resumo()
    legenda()
    mecanica_rosca()
    #st.image(r"assets/fluxo.png", caption="", width="stretch")                                                          # Parametro para adiconar imagem com largura fixa. 
    
with coluna2:
    dados_clientes()
    st.markdown(
        "<h1 style='color: #ED8232; font-size: 24px;'>Lista de Prioridades:</h1>",
        unsafe_allow_html=True
    )
    
    mecanica_prioridade()
    #st.image(r"assets/tcm.png", caption="", width="stretch")                                                          # Parametro para adiconar imagem com largura fixa.


#separador()
resumo_ctu()


