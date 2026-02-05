# 1>>> Importar bibliotecas
#import pandas as pd
import streamlit as st
from auxiliar.lateral import barra
from calculo.media import mecanica_status,mecanica_aviso,mecanica_envio,eletrica_status,eletrica_aviso,eletrica_envio,filtro
from auxiliar.texto import legenda, separador
#from styles.cores import cor

# 5>>> Criar o layout da página no Streamlit_______________________________________________________________________________________________________________________

st.set_page_config(page_title="GPM - Mecânico", layout="wide")                                              # Criar o layout da pagina                                                                    

st.image(r"assets/painel.png", caption="", width="stretch")                                            # Adicona a logomarca.                                                                       

separador()

estado =filtro()

barra()

# Layout para o campo dos indicadores dos resultados  do Progresso: Mecanica e Elétrica__________________________________________________________________________________________________________

legenda()

coluna1, coluna2 = st.columns(2)

with coluna1:                                                                                                  # Parametro para inserir conteudo na primeira coluna, lado esquerdo.
    st.markdown("<h1 style = 'text-align:center;font-size:40px;color:white;'>Indicadores Mecânica</h1>",        
            unsafe_allow_html = True)
    mecanica_status(estado)

with coluna2:
    st.markdown("<h1 style = 'text-align:center;font-size:40px;color:white;'>Indicadores Elétrica</h1>",        
            unsafe_allow_html = True)   
    eletrica_status(estado)

separador()

# Layout para o campo dos indicadores dos resultados do Aviso: Mecanica e Elétrica__________________________________________________________________________________________________________

legenda()

coluna1, coluna2 = st.columns(2)

with coluna1:                                                                                                  # Parametro para inserir conteudo na primeira coluna, lado esquerdo.
    st.markdown("<h1 style = 'text-align:center;font-size:40px;color:white;'>Solicitação de Aviso: Mecânica</h1>",        
            unsafe_allow_html = True)
    mecanica_aviso(estado)

with coluna2:
    st.markdown("<h1 style = 'text-align:center;font-size:40px;color:white;'>Solicitação de Aviso: Elétrica</h1>",        
            unsafe_allow_html = True)   
    eletrica_aviso(estado)

separador()

# Layout para o campo dos indicadores dos resultados do Envio: Mecanica e Elétrica__________________________________________________________________________________________________________

legenda()

coluna1, coluna2 = st.columns(2)

with coluna1:                                                                                                  # Parametro para inserir conteudo na primeira coluna, lado esquerdo.
    st.markdown("<h1 style = 'text-align:center;font-size:40px;color:white;'>Solicitação de Envio: Mecânica</h1>",        
            unsafe_allow_html = True)
    mecanica_envio(estado)

with coluna2:
    st.markdown("<h1 style = 'text-align:center;font-size:40px;color:white;'>Solicitação de Envio: Elétrica</h1>",        
            unsafe_allow_html = True)   
    eletrica_envio(estado)

separador()