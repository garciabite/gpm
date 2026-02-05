# Importa a biblioteca Streamlit para criação da aplicação web
import streamlit as st

# Importa uma função personalizada chamada 'cor' do módulo 'cores', localizado na pasta 'styles'
# Essa função retorna uma string com uma cor (hexadecimal ou nome) usada nos textos do sidebar
#from styles.cores import cor


# 2 >>> Criar o sidebar ____________________________________________________________________________________________________________________
# Define uma função chamada 'barra' que constrói o conteúdo lateral da aplicação (sidebar).
def barra():
    
    # Adiciona a logomarca da Mebrafe na sidebar, com ajuste automático de largura
    st.sidebar.image(r"assets/mebrafe.png", caption="", width="stretch")
    
    # Adiciona a imagem do túnel (produto da empresa), com largura ajustada
    st.sidebar.image(r"assets/tunel.png", caption="", width="stretch")
    
    # Adiciona a imagem representando os clientes da empresa
    st.sidebar.image(r"assets/clientes.png", caption="", width="stretch")

    # 2.1 >>> Criar o sidebar :(Adm, Data e Versão) - Explicação Manual
    # Insere um texto formatado em HTML na sidebar, mostrando informações do administrador, data e versão do sistema.
    st.sidebar.markdown(
        f"""
        <p style="line-height:1.5;">
        <span style="color:#ED8232;"><b>Adm:</b></span> <span style="color:white;">Cristian Garcia</span><br>
        <span style="color:#ED8232;"><b>Data:</b></span> <span style="color:white;">20/09/24</span><br>
        <span style="color:#ED8232;"><b>Versão:</b></span> <span style="color:white;">11</span>
        </p>
        """,
        unsafe_allow_html=True  # Permite a renderização de HTML no markdown
    )