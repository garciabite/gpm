import streamlit as st
from auxiliar.mapa import mapa
from auxiliar.texto import resumo, aplicacao, texto_mapa, separador
from auxiliar.lateral import barra


# 2>>> Criar o layout da página no Streamlit_______________________________________________________________________________________________________________________

# Parametro st.set_page_config:
# Configura o título da aba do navegador, define o layout da pagina como "wide" (largura total da tela) e define um ícone para aba.

st.set_page_config(page_title="GPM - Mecânico", layout="wide", page_icon="⚙")


# Parametro st.markdown:
# Insere texto em formato HTML. Aqui, está sendo inserido um título grande e centralizado com o texto "GPM - GESTÃO DE PROJETOS MEBRAFE".
# O parâmetro unsafe_allow_html=True permite o uso de HTML personalizado.
st.markdown("""
    <h1 style="text-align:center; font-size:40px;">GPM - GESTÃO DE PROJETOS MEBRAFE</h1>
    """, unsafe_allow_html=True)

separador()

# Parametro st.coluns
# st.columns(2): Cria duas colunas, dividindo o layout da página em duas partes.
# with coluna1: Tudo dentro deste bloco será exibido na primeira coluna. A função st.image insere uma imagem localizada no caminho "assets/fluxo.png".
#with coluna2:Tudo dentro deste bloco será exibido na segunda coluna. A função resumo() é chamada aqui para exibir o texto relacionado ao resumo, que é importado do módulo texto.

coluna1, coluna2 = st.columns(2)                                                                                # Parametro para criar duas colunas.

with coluna1:                                                                                                   # Parametro para inserir conteudo na terceira coluna, lado esquerdo.
    texto_mapa()                                                                                                # Exibe uma seção de texto relacionado ao mapa.

with coluna2:                                                                                                   # Parametro para inserir conteudo na quarta coluna, lado direito.
    mapa()                                                                                                      # Exibe o mapa em 3D na segunda coluna.

separador()                                                                                                     # Chama a função que cria uma linha de separação na página.

st.video(r"assets/mebrafe.mp4", loop=True, autoplay=True, muted=True, width="stretch") 

separador() 
coluna3, coluna4 = st.columns(2)

with coluna3:                                                                                                   # Parametro para inserir conteudo na primeira coluna, lado esquerdo.
    st.image(r"assets/fluxo.png", caption="", width="stretch")                                                  # Parametro para adiconar imagem.

with coluna4:                                                                                                   # Parametro para inserir conteudo na segunda coluna, lado direito.
    resumo()                                                                                                    # Texto com a função resumo.


separador() 
coluna5, coluna6 = st.columns(2)                                                                                # Parametro para criar duas colunas

with coluna5:
    st.image(r"assets/tcm.png", caption="", width=600)                                                          # Parametro para adiconar imagem com largura fixa.

with coluna6:
    aplicacao()                                                                                                 # Exibe uma seção de texto relacionada à aplicação, importada do módulo texto

separador()                                                                                                     # Chama a função que cria uma linha de separação na página.

#st.image(r"assets/simulacao.gif", caption="", width="stretch")                                                      # Adicona a logomarca.
                           # Exibe o video abaixo do GIF em loop ao abrir a página.

barra()                                                                                                         # Insere a barra lateral na página, usando a função barra importada do módulo lateral.
