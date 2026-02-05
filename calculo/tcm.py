import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from auxiliar.texto import formato_resumo
from calculo.ctu import style_cells

# Função para plotar o grafico de rosca no Menu Mecânica (Indicadores Individuais)________________________________________________________________________________________

def mecanica_resumo():
    st.markdown(
        "<h1 style='color: #ED8232; font-size: 24px;'>Selecione um Projeto:</h1>",
        unsafe_allow_html=True
    )
    # Verifica se o DataFrame está disponível no st.session_state
    aba = "Mecanica"
    if aba in st.session_state.abas:
        lista = st.session_state[f"{aba}"]  
        # Cria um selectbox para selecionar apenas um projeto por vez e armazena a seleção no st.session_state
        st.session_state.projeto_selecionado = st.selectbox(
            '',
            options=lista['PROJETO'].unique()
        )  

        # Exibe o nome do projeto selecionado
        #st.write(f"Projeto Selecionado: {st.session_state.projeto_selecionado}")

# Padrão para o grafico de pizza______________________________________________________________________________________________________________________________________

def mecanica_rosca(tamanho_grafico=(3, 3), tamanho_fonte=17):
    # Verifica se o DataFrame e o projeto selecionado estão disponíveis no st.session_state
    aba = "Mecanica"
    if aba in st.session_state.abas and "projeto_selecionado" in st.session_state:
        lista = st.session_state[f"{aba}"]  
        projeto_selecionado = st.session_state.projeto_selecionado
        
        # Filtra o DataFrame para obter apenas os dados do projeto selecionado
        projeto = lista[lista['PROJETO'] == projeto_selecionado]['PROGRESSO']
        
        # Calcula a média do progresso
        progresso = projeto.mean()
        
        # Garante que o percentual seja um valor entre 0 e 1
        percentual = max(0, min(progresso / 100, 1))
        
        # Configuração do gráfico de rosca com o tamanho especificado
        fig, ax = plt.subplots(figsize=tamanho_grafico)
        
        # Gráfico de rosca com fundo transparente e apenas o valor percentual no centro
        ax.pie([percentual, 1 - percentual], 
               colors=['#2A6AAE', '#ED8232'], 
               startangle=90,
               wedgeprops=dict(width=0.3))
        
        # Centraliza o percentual no gráfico
        ax.text(0, 0, f'{percentual * 100:.1f}%', ha='center', va='center', fontsize=tamanho_fonte, color='white')
        
        # Remove fundo branco
        fig.patch.set_alpha(0)
        
        # Exibe o gráfico com Streamlit
        st.pyplot(fig)
    else:
        st.write("O DataFrame 'df_mecanica' ou o projeto selecionado não estão disponíveis no estado da sessão.")


#Função para lista das priordades (Mecanica)

def mecanica_prioridade():
    # Verifica se o DataFrame e o projeto selecionado estão disponíveis no st.session_state
    aba = "Mecanica"
    if aba in st.session_state.abas and "projeto_selecionado" in st.session_state:
        # Obtém o DataFrame do estado da sessão
        df_prioridade = st.session_state[f"{aba}"] 
        
        # Filtra o DataFrame para o projeto selecionado com STATUS "PRIORIDADE" e apenas as colunas desejadas
        atividades = df_prioridade[(df_prioridade['PROJETO'] == st.session_state.projeto_selecionado) & 
                                   (df_prioridade['STATUS'] == 'PRIORIDADE')][["FAMILIA", "ATIVIDADE", "STATUS"]]
        
        # Verifica se há atividades para exibir
        if not atividades.empty:
            # Exibe o DataFrame filtrado
            st.dataframe(
                atividades,
                width="stretch",
                hide_index= True,
                height=400,
                )
        else:
            st.write("Nenhuma atividade com status PRIORIDADE para o projeto selecionado.")
    else:
        st.write("O DataFrame 'df_mecanica' ou o projeto selecionado não estão disponíveis no estado da sessão.")


def resumo_ctu():
    # Verifica se há abas disponíveis e um projeto selecionado
    if st.session_state.abas and "projeto_selecionado" in st.session_state:
        aba_selecionada = st.session_state.projeto_selecionado

        # Verifica se a aba selecionada está disponível no st.session_state
        if aba_selecionada in st.session_state:
            df_ctu = st.session_state[aba_selecionada].fillna("").replace("None", "")

            # Personalizar o DataFrame (Exemplo: aplicar estilos)
            ctu_resumo = df_ctu.style.apply(style_cells, axis=1)

            # Exibir tabela com estilo aplicado
            st.write(f"<h4>Resumo CTU: {aba_selecionada}</h4>",
                     unsafe_allow_html=True)
            
            st.dataframe(ctu_resumo,
                         width="stretch",
                         height=1260,
                         hide_index=True)
        else:
            # Aba específica não encontrada
            st.write("Este projeto não tem resumo de CTU.")
    else:
        # Nenhuma aba ou projeto selecionado
        st.write("Este projeto não tem resumo CTU.")


def dados_clientes():
    st.markdown(
        "<h1 style='color: #ED8232; font-size: 24px;'>Dados do Projeto:</h1>",
        unsafe_allow_html=True
    )
    
    # Verifica se os DataFrames estão disponíveis no st.session_state
    aba = "Mapa"
    if aba in st.session_state.abas and "projeto_selecionado" in st.session_state:
    #if "df_mecanica" in st.session_state and "df_mapa" and "projeto_selecionado" in st.session_state:
        # Obtém a lista de projetos no df_mecanica para exibir no selectbox

        # Cria um selectbox para selecionar apenas um projeto por vez e armazena a seleção no st.session_state
        projeto_selecionado = st.session_state.projeto_selecionado

        # Extrai os últimos quatro dígitos do projeto selecionado
        codigo_projeto = projeto_selecionado[-4:]

        # Filtra o DataFrame df_mapa para encontrar a linha com o mesmo código nos últimos quatro dígitos
        df_mapa = st.session_state[f"{aba}"]

        # Certifica-se de que a coluna 'Codigo' está no tipo string
        df_mapa['Codigo'] = df_mapa['Codigo'].astype(str)
        linha_correspondente = df_mapa[df_mapa['Codigo'].str.endswith(codigo_projeto)]

        # Verifica se encontrou uma linha correspondente e exibe as informações
        if not linha_correspondente.empty:
            cidade = linha_correspondente['Cidade'].values[0]
            tipo = linha_correspondente['Tipo'].values[0]
            modelo = linha_correspondente['Modelo'].values[0]
            nivel = linha_correspondente['Niveis'].values[0]
            status = linha_correspondente['Status'].values[0]
            #data_inicial = linha_correspondente['Data Inicial'].values[0]

            # Converte a data do Excel para formato de data
            data_inicial = pd.to_datetime(
                linha_correspondente['Data Inicial'].values[0]
            ).strftime('%d/%m/%Y')  # Formato desejado: DD/MM/YYYY

            total_dias = linha_correspondente['Total Dias'].values[0]

            # Exibe os dados encontrados
            st.markdown(formato_resumo("Cidade", cidade), unsafe_allow_html=True)
            st.markdown(formato_resumo("Tipo", tipo), unsafe_allow_html=True)
            st.markdown(formato_resumo("Modelo", modelo), unsafe_allow_html=True)
            st.markdown(formato_resumo("Níveis", nivel), unsafe_allow_html=True)
            st.markdown(formato_resumo("Status", status), unsafe_allow_html=True)
            st.markdown(formato_resumo("Data Inicial", data_inicial), unsafe_allow_html=True)
            st.markdown(formato_resumo("Total Dias", total_dias), unsafe_allow_html=True)
        else:
            st.write("Nenhum dado encontrado para os últimos 4 dígitos do projeto selecionado.")