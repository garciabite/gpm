import streamlit as st


# 1>>> Configurando as pagina_______________________________________________________________________________________________________________________

#Padrão:
#page = conecta ao nome do código da pagina;
#title = titulo da pagina;
#icon = parametro para inserir o nome dos arquivos pesquisados na pagina: https://fonts.google.com/icons?selected=Material+Symbols+Outlined:cloud_upload:FILL@0;wght@400;GRAD@0;opsz@24&icon.size=24&icon.color=%23e8eaed&icon.platform=web

banco = st.Page( 
    page = "pages/banco.py", 
    title = "Banco de Dados", 
    icon = ":material/cloud_upload:", 
    default= True, 
    )

dash = st.Page( 
    page = "pages/dash.py", 
    title = "Dashboard",
    icon = ":material/insert_chart:", 
    )

eletrica = st.Page( 
    page = "pages/eletrica.py", 
    title= "Elétrica", 
    icon = ":material/bolt:",
    )

mecanica = st.Page( 
    page = "pages/mecanica.py", 
    title= "Mecânica", 
    icon = ":material/manufacturing:", 
    )

home = st.Page( 
    page = "pages/home.py", 
    title = "Home", 
    icon = ":material/home:", 
    )

# 12>>> Navegação entre as pagina_______________________________________________________________________________________________________________________

pg = st.navigation(pages=[home,dash,eletrica,mecanica,banco]) 

pg.run()