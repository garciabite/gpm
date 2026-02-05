import streamlit as st
import plotly.express as px


# Função Filtro
def filtro():
    if "filtro" not in st.session_state:
        st.session_state.filtro = False

    if st.button("Habilita/Desabilita os Projetos em Andamento"):
        st.session_state.filtro = not st.session_state.filtro

    return st.session_state.filtro

# Função para plotar o grafico de barras no Menu Dashbord (Indicadores da Mecânica)________________________________________________________________________________________
def mecanica_status(filtro):
    aba = "Mecanica"
    if aba in st.session_state.abas:
        df_progresso_mecanica = st.session_state[f"{aba}"] 
        media = df_progresso_mecanica.groupby('PROJETO')['PROGRESSO'].mean().reset_index()

        # Arredondando os valores de média para 1 casa decimal
        media['PROGRESSO'] = media['PROGRESSO'].round(1)

        # Definindo a cor das barras com base no valor do progresso
        media['Legenda'] = media['PROGRESSO'].apply(lambda x: 'Concluido' if x >= 100 else 'Andamento')

        # Aplicando o filtro, se necessário
        if filtro:
            media = media[media['PROGRESSO'] < 100]
            st.write("Filtro ativo: Exibindo apenas projetos em andamento.")
        else:
            st.write("Exibindo todos os projetos.")

        grafico_barra(media)
    else:
        st.write("Nenhum dado disponível para exibição.")

# Função para plotar o grafico de barras no Menu Dashbord (Indicadores da Elétrica)________________________________________________________________________________________

def eletrica_status(filtro):
    aba = "Eletrica"
    if aba in st.session_state.abas:
        df_progresso_eletrica = st.session_state[f"{aba}"] 
        media = df_progresso_eletrica.groupby('PROJETO')['PROGRESSO'].mean().reset_index()

        # Arredondando os valores de média para 1 casa decimal
        media['PROGRESSO'] = media['PROGRESSO'].round(1)

        # Definindo a cor das barras com base no valor do progresso
        media['Legenda'] = media['PROGRESSO'].apply(lambda x: 'Concluido' if x >= 100 else 'Andamento')

        # Aplicando o filtro, se necessário
        if filtro:
            media = media[media['PROGRESSO'] < 100]
            st.write("Filtro ativo: Exibindo apenas projetos em andamento.")
        else:
            st.write("Exibindo todos os projetos.")

        grafico_barra(media)
    else:
        st.write("Nenhum dado disponível para exibição.")


# Função para plotar o grafico de barras no Menu Mecânica (Indicadores do Envio)________________________________________________________________________________________
def mecanica_envio(filtro):
    aba = "Mecanica"
    if aba in st.session_state.abas:
        df_progresso_mecanica = st.session_state[f"{aba}"] 

        # Filtrar apenas as linhas onde ATIVIDADE é "Solicitação de Envio"
        df_solicitacao_envio = df_progresso_mecanica[df_progresso_mecanica['ATIVIDADE'] == "Solicitação de Envio"]

        media = df_solicitacao_envio.groupby('PROJETO')['PROGRESSO'].mean().reset_index()

        # Arredondando os valores de média para 1 casa decimal
        media['PROGRESSO'] = media['PROGRESSO'].round(1)

        # Definindo a cor das barras com base no valor do progresso
        media['Legenda'] = media['PROGRESSO'].apply(lambda x: 'Concluido' if x >= 100 else 'Andamento')

        # Aplicando o filtro, se necessário
        if filtro:
            media = media[media['PROGRESSO'] < 100]
            st.write("Filtro ativo: Exibindo apenas projetos em andamento.")
        else:
            st.write("Exibindo todos os projetos.")

        grafico_barra(media)
    else:
        st.write("Nenhum dado disponível para exibição.")


# Função para plotar o grafico de barras no Menu Elétrica (Indicadores do Envio)________________________________________________________________________________________
def eletrica_envio(filtro):
    aba = "Eletrica"
    if aba in st.session_state.abas:
        df_progresso_eletrica = st.session_state[f"{aba}"]

        # Filtrar apenas as linhas onde ATIVIDADE é "Solicitação de Envio"
        df_solicitacao_envio = df_progresso_eletrica[df_progresso_eletrica['ATIVIDADE'] == "Solicitação de Envio"]

        media = df_solicitacao_envio.groupby('PROJETO')['PROGRESSO'].mean().reset_index()

        # Arredondando os valores de média para 1 casa decimal
        media['PROGRESSO'] = media['PROGRESSO'].round(1)

        # Definindo a cor das barras com base no valor do progresso
        media['Legenda'] = media['PROGRESSO'].apply(lambda x: 'Concluido' if x >= 100 else 'Andamento')

        # Aplicando o filtro, se necessário
        if filtro:
            media = media[media['PROGRESSO'] < 100]
            st.write("Filtro ativo: Exibindo apenas projetos em andamento.")
        else:
            st.write("Exibindo todos os projetos.")

        grafico_barra(media)
    else:
        st.write("Nenhum dado disponível para exibição.")


# Função para plotar o grafico de barras no Menu Mecânica (Indicadores do Aviso)________________________________________________________________________________________
def mecanica_aviso(filtro):
    aba = "Mecanica"
    if aba in st.session_state.abas:
        df_progresso_mecanica = st.session_state[f"{aba}"]

        # Filtrar apenas as linhas onde ATIVIDADE é "Solicitação de Envio"
        df_solicitacao_aviso = df_progresso_mecanica[df_progresso_mecanica['ATIVIDADE'] == "Solicitação de Aviso"]

        media = df_solicitacao_aviso.groupby('PROJETO')['PROGRESSO'].mean().reset_index()

        # Arredondando os valores de média para 1 casa decimal
        media['PROGRESSO'] = media['PROGRESSO'].round(1)

        # Definindo a cor das barras com base no valor do progresso
        media['Legenda'] = media['PROGRESSO'].apply(lambda x: 'Concluido' if x >= 100 else 'Andamento')

        # Aplicando o filtro, se necessário
        if filtro:
            media = media[media['PROGRESSO'] < 100]
            st.write("Filtro ativo: Exibindo apenas projetos em andamento.")
        else:
            st.write("Exibindo todos os projetos.")

        grafico_barra(media)
    else:
        st.write("Nenhum dado disponível para exibição.")


# Função para plotar o grafico de barras no Menu Elétrica (Indicadores do Envio)________________________________________________________________________________________
def eletrica_aviso(filtro):
    aba = "Eletrica"
    if aba in st.session_state.abas:
        df_progresso_eletrica = st.session_state[f"{aba}"]

        # Filtrar apenas as linhas onde ATIVIDADE é "Solicitação de Envio"
        df_solicitacao_aviso = df_progresso_eletrica[df_progresso_eletrica['ATIVIDADE'] == "Solicitação de Aviso"]

        media = df_solicitacao_aviso.groupby('PROJETO')['PROGRESSO'].mean().reset_index()

        # Arredondando os valores de média para 1 casa decimal
        media['PROGRESSO'] = media['PROGRESSO'].round(1)

        # Definindo a cor das barras com base no valor do progresso
        media['Legenda'] = media['PROGRESSO'].apply(lambda x: 'Concluido' if x >= 100 else 'Andamento')

        # Aplicando o filtro, se necessário
        if filtro:
            media = media[media['PROGRESSO'] < 100]
            st.write("Filtro ativo: Exibindo apenas projetos em andamento.")
        else:
            st.write("Exibindo todos os projetos.")

        grafico_barra(media)
    else:
        st.write("Nenhum dado disponível para exibição.")


# Padrão para o grafico de barras______________________________________________________________________________________________________________________________________

def grafico_barra(media,unique_key=None):

    # Criando o gráfico de barras horizontal com Plotly
    fig = px.bar(
        media,
        x='PROGRESSO',
        y='PROJETO',
        orientation='h',
        text=media['PROGRESSO'].astype(str) + '%',  # Adiciona o símbolo de %
        color='Legenda',
        color_discrete_map={'Andamento': '#ED8232', 'Concluido': '#2A6AAE'}  # Mapeia as cores
    )

    # Configurando estilo das barras
    fig.update_traces(
        textposition='outside',
        marker_line_width=0,  # Remove contorno nas barras
        width=0.7  # Aumenta a largura da barra
    )
    
    # Definindo o limite do eixo X para reduzir o comprimento das barras
    fig.update_xaxes(range=[0, 120])  # Ajusta de acordo com o valor máximo de progresso

    # Ajustando o layout e área visual do gráfico
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        font=dict(color="white", size=16),  # Cor e tamanho da fonte geral
        margin=dict(l=120, r=30, t=30, b=30),  # Margens para ajustar a área do gráfico
        height=700,  # Aumenta a altura do gráfico
        width=400,   # Reduz a largura do gráfico
        showlegend=False  # Remove a legenda
    )
    # Removendo as linhas de grade
    fig.update_xaxes(showgrid=False, visible=False)
    # Aumentando o tamanho da fonte do eixo Y
    fig.update_yaxes(tickfont=dict(size=16))  # Aumenta o tamanho da fonte do eixo Y
    fig.update_yaxes(showgrid=False)

    # Exibindo o gráfico interativo no Streamlit
    st.plotly_chart(fig,
                    width="stretch",
                    key=unique_key or f"plot_{id(fig)}"
                    )


