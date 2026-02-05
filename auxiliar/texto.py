import streamlit as st
from datetime import datetime

# Função que exibe um texto institucional com foco nos diferenciais do TCM Mebrafe
def resumo():
    st.markdown("""
    <!-- Bloco institucional com destaques em laranja -->
    <p style="font-size:25px;">
    A Mebrafe está presente em mais de 35 cidades em diferentes países, consolidando sua expertise e excelência com o túnel de congelamento e resfriamento contínuo para proteínas – 
    <span style="color:#ED8232;"><b>TCM</b></span>. Nossa presença global reforça o compromisso em oferecer 
    <span style="color:#ED8232;"><b>desempenho superior</b></span>, 
    <span style="color:#ED8232;"><b>assistência técnica especializada</b></span> e 
    <span style="color:#ED8232;"><b>análises de resultados precisas</b></span>, garantindo que você tenha total 
    <span style="color:#ED8232;"><b>confiabilidade</b></span> nas operações.
    </p>
    
    <p style="font-size:25px;">
    O <span style="color:#ED8232;"><b>TCM</b></span> se destaca por sua 
    <span style="color:#ED8232;"><b>conectividade</b></span> e 
    <span style="color:#ED8232;"><b>fluxo operacional inteligente</b></span>, proporcionando uma experiência eficiente e integrada. 
    Com a Mebrafe, seu projeto recebe suporte completo e soluções personalizadas, assegurando um diferencial competitivo em qualquer mercado.
    </p>

    <p style="font-size:25px;">
    Nosso objetivo é entregar mais do que um produto – é fornecer resultados reais, que otimizam seu negócio e reduzem custos operacionais.
    </p>
    """, unsafe_allow_html=True)

# Função que descreve tecnicamente a aplicação do TCM
def aplicacao():
    st.write("""
    <!-- Título da seção de aplicação -->
    <p style="font-size:40px;">
    <span style="color:#ED8232;"><b>TCM - Aplicação</b></span>         
    <p style="font-size:20px;">
    Túnel de Congelamento e Resfriamento Contínuo – TCM
    A Mebrafe apresenta o TCM, um túnel de congelamento e resfriamento contínuo para caixas, que combina inovação tecnológica e eficiência energética incomparável.
    <br><br>Com sistemas exclusivos, o TCM proporciona performance superior e baixo consumo de energia, ideal para otimizar a produção de alimentos.
    <br><br>Projetado para atender a diferentes mercados, como o de frango, suínos e bovinos, o TCM pode congelar até 30 toneladas de produtos por hora em caixas, operando com velocidades de até 2.000 caixas/h, graças ao conceito inovador de dois túneis sincronizados(*).
    <br><br>Na versão compacta, o TCM se destaca por sua viabilidade econômica em produções menores, gerando economia significativa de energia e redução de custos operacionais. Além disso, pode ser configurado em etapas de capacidade crescentes, permitindo que seu investimento inicial seja otimizado, com possibilidade de expansão futura sem interrupções na produção.
    </p>
    """, unsafe_allow_html=True)

# Função que apresenta dados numéricos da presença global do TCM
def texto_mapa():
    st.write("""
    <p style="font-size:50px;">
    <span style="color:#ED8232;"><b>TCM Mebrafe pelo mundo...</b></span>

    <p style="font-size:50px;">
    <br>+ 50 cidades
    <br>+ 50 TCM desenvolvidos e implementados
    <br>+ 4,2* milhões de toneladas  de congelados / ano
    </p>
    <p style="font-size:50px;">
    <span style="color:#2A6AAE;">TCM Mebrafe representa *14% de toda a produção nacional.</span>
    </p>
    <p style="font-size:20px;">
    <br> * Corresponde a proteína animal (ave, bovino e suíno) produzida no Brasil.
    <br> Fonte: EXAME Agro (Publicado em 2 de novembro de 2023).    
    """, unsafe_allow_html=True)

# Função para exibir uma linha visualmente elegante entre seções
def separador():
    st.write("""
    <hr style="border: none; height: 1px; background-image: linear-gradient(to right, #2A6AAE, #ED8232);">
    """, unsafe_allow_html=True)

# Função que mostra data do último carregamento + legenda visual das cores dos indicadores
def legenda():
    st.session_state.data_carregamento = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if "data_carregamento" in st.session_state:
        st.write(f"**Indicadores atualizado em:** {st.session_state.data_carregamento}")

        st.markdown("""
            <!-- Legenda visual com cores dos status -->
            <div style="display: flex; align-items: center; font-size: 16px;">
                <div style="width: 25px; height: 25px; background-color: #ED8232; margin-right: 10px;"></div>
                <span style="color:{cor()};">Andamento</span>
            </div>
            <div style="display: flex; align-items: center; font-size: 16px; margin-top: 5px;">
                <div style="width: 25px; height: 25px; background-color: #2A6AAE; margin-right: 10px;"></div>
                <span style="color: {cor()};">Concluído</span>
            </div>
        """, unsafe_allow_html=True)

# Função auxiliar para formatar pares label/valor com destaque no Streamlit
def formato_resumo(label, value):
    return f"""
    <p style="font-size:25px; color:#ED8232;">
        {label}: <span style="color:white;">{value}</span>
    </p>
    """

