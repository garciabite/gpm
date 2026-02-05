import pandas as pd
import streamlit as st

# 1>>> Criar o layout da página no Streamlit_______________________________________________________________________________________________________________________

st.set_page_config(page_title="GPM - Mecânico", layout="wide")                                                  # Criar o layout da página.                                                                   

st.markdown("<h1 style = 'text-align:center;font-size:40px;'>GPM - GESTÃO DE PROJETOS MEBRAFE</h1>",        
            unsafe_allow_html = True)                                                                           # Criar o Título da página.

# 2>>> Criar o sidebar para os botões______________________________________________________________________________________________________________________________
st.sidebar.image(r"assets/mebrafe.png", caption="", width="stretch")                                        # Adicona a logomarca.
st.sidebar.image(r"assets/tunel.png", caption="", width="stretch")                                        # Adicona a logomarca.
st.sidebar.header("GPM - Mecânica")                                                                             # Cria o Subtítulo. 

# 3>>> Carregar banco de dados e filtrar______________________________________________________________________________________________________________________________

if "abas" not in st.session_state:
    st.session_state.abas = []                                                                              # Inicializar lista de abas

arquivo = st.file_uploader(label="Upload Banco de Dados", type=["xlsx"])                                    # Upload do arquivo

if arquivo is not None:  # Verifica se o arquivo foi carregado
    xls = pd.ExcelFile(arquivo)

    # >>> Adicionado em 14/01/25
    abas = xls.sheet_names
    st.session_state.abas = abas                                                                        # Parametro para armazernar as abas

    for aba in abas:
        st.session_state[f"{aba}"]=pd.read_excel(xls,sheet_name=aba)                                 # Parametro para ler as abas
        
    st.success("Arquivo carregado com sucesso!")

else:
    st.write("Por favor, faça o upload da base de dados!")  # Mensagem de aviso


#if st.session_state.abas:
    #df_mecanica = st.session_state[f"Mecanica"]
    #df_eletrica = st.session_state[f"Eletrica"]
    #df_mapa = st.session_state[f"Mapa"]

    #st.dataframe(df_mecanica,width="stretch",height=800,hide_index=True)
    #st.dataframe(df_mapa,width="stretch",height=800,hide_index=True)
