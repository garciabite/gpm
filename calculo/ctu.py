import pandas as pd  # Importa a biblioteca pandas para manipulação de dados

# Função para plotar o grafico do resumo dos CTU (Indicadores da Mecânica)________________________________________________________________________________________
def style_cells(row):
    styles = []  # Lista para armazenar os estilos de cada célula

    for col_index, value in enumerate(row):  # Itera sobre os valores e índices das colunas da linha
        style = ""  # Estilo padrão vazio

        # Condição 1: Células vazias
        if pd.isna(value) or str(value).strip() == "":
            style = "background-color: rgb(38,39,48);"  # Aplica fundo escuro para células vazias

        # Condição 2: Colunas 0, 3, 6 e 9 com valores preenchidos
        if col_index in {0, 3, 6, 9} and not pd.isna(value) and str(value).strip():
            style = "color: white; font-weight: bold;"  # Aplica fonte branca e em negrito para identificar cabeçalhos ou títulos

        # Condição 3: Colunas 1, 4, 7 e 10
        if col_index in {1, 4, 7, 10}:
            try:
                numeric_value = float(value)  # Tenta converter o valor da célula para número
                if 1 <= numeric_value < 100:
                    gradiente = int((numeric_value / 99) * 255)  # Calcula intensidade da cor com base no valor
                    style = f"background-color: rgba({200 - gradiente},0,255,1); color: white;"  # Aplica cor com gradiente proporcional e fonte branca
                elif numeric_value == 100:
                    style = "background-color: rgb(42,106,174); color: white;"  # Cor azul especial para 100%
            except ValueError:
                pass  # Ignora se o valor não puder ser convertido para número

        # Condição 4: Colunas entre 2 e 10 com valores específicos (nomes de componentes técnicos)
        if col_index in range(2, 11):
            if str(value) in {"INDICADORES",
                              "BANDEJAS","CINTAS","COLUNAS","CRUZETAS","ELEVADOR","FECHAMENTO COMPL.",
                              "FECHAMENTO RACK","GUIA ELEVADOR","TRANSP. EXTERNO","TRANSP. INTERNO",
                              "PASSARELAS","RACKBEAM","SAPATAS / SOLEIRAS","TRANSMISSÃO","TRAVESSAS",
                              "TORRE VENTILADOR","TRANSFERIDOR","VENTILADOR"}:
                style = "background-color: rgb(237,130,50); color: white; font-weight: bold;"  # Aplica cor laranja com texto branco e negrito

        # Condição 5: Colunas 0 e 1 com categorias específicas
        if col_index in range(0, 2):
            if str(value) in {"STATUS", "MECANISMOS", "CONTAINER", "EVAPORADOR"}:
                style = "background-color: rgb(237,130,50); color: white; font-weight: bold;"  # Mesma formatação laranja para elementos importantes

        styles.append(style)  # Adiciona o estilo calculado à lista

    return styles  # Retorna a lista de estilos para a linha



