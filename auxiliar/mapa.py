# Importa a biblioteca Streamlit para interface web
import streamlit as st

# Importa o módulo Plotly Express, utilizado para visualizações interativas
import plotly.express as px

# Define a função 'mapa', que gera e exibe o mapa de clientes/projetos no mundo
def mapa():

    aba = "Mapa"  # Define o nome da aba que será usada como chave no session_state

    # Verifica se a aba 'Mapa' existe no dicionário de abas salvas na sessão
    if aba in st.session_state.abas:

        # Acessa diretamente o DataFrame da aba 'Mapa' armazenado no session_state
        df_cidades = st.session_state[f"{aba}"]

        # Gera um gráfico do tipo scatter_geo (dispersão geográfica) com as seguintes configurações:
        figura = px.scatter_geo(
            df_cidades,
            lat='Latitude',  # Coluna com latitude
            lon='Longitude',  # Coluna com longitude
            projection="orthographic",  # Projeção esférica (globo 3D)
            hover_name='Cidade',  # Nome exibido ao passar o mouse
            hover_data={  # Dados adicionais exibidos ao passar o mouse
                'Latitude': False,
                'Longitude': False,
                'Cliente': True,
                'Ano': True,
                'Codigo': True,
                'Tipo': True
            },
            opacity=1  # Transparência total (sem transparência)
        )

        # Customizações visuais do globo
        figura.update_geos(
            showland=True,  # Exibe áreas de terra
            landcolor='orange',  # Cor dos continentes
            oceancolor='black',  # Cor dos oceanos
            showocean=True,
            showcoastlines=True,  # Exibe linhas costeiras
            coastlinecolor='white',  # Cor das linhas costeiras
            showframe=False,  # Remove o contorno global
            showcountries=True,  # Exibe as divisões entre países
            countrycolor='white'  # Cor dos contornos dos países
        )

        # Personalização dos pontos que representam as cidades
        figura.update_traces(
            marker=dict(
                size=20,  # Tamanho dos marcadores
                color="#2A6AAE",  # Cor azul dos pontos
                line=dict(width=2, color='white')  # Borda branca ao redor dos pontos
            )
        )

        # Customização geral do layout do gráfico
        figura.update_layout(
            geo=dict(
                bgcolor='rgba(0,0,0,0)'  # Fundo do globo transparente
            ),
            paper_bgcolor='rgba(0,0,0,0)',  # Fundo da área do gráfico transparente
            font=dict(
                size=20,
                color='white'  # Cor branca para todos os textos do gráfico
            ),
            width=1000,  # Largura do gráfico
            height=800   # Altura do gráfico
        )

        # Exibe o gráfico no app Streamlit
        st.plotly_chart(figura)



