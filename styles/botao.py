import streamlit as st

def botao_laranja():
    return {
        "container": {"padding": "0!important", "background-color": "transparent"},
        "icon": {"color": "white", "font-size": "20px"},  # Ícones na cor branca quando não selecionados
        "nav-link": {
            "font-size": "16px",
            "text-align": "left",
            "margin": "0px",
            "background-color": "transparent",  # Fundo transparente para os botões não selecionados
            "color": "white",  # Fonte branca quando o botão não está selecionado
        },
        "nav-link-selected": {
            "background-color": "orange",  # Fundo laranja quando selecionado
            "color": "white",             # Fonte laranja para combinar com o fundo
            "--icon-color": "white"       # Ícone laranja para combinar com o fundo
        },
    }

