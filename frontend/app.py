# Built-in
import requests
import os
from datetime import datetime
# Terceiras
import streamlit as st
import pandas as pd
# Proprietárias
import config
import constants as cte

def run() -> None:
    """Função principal responsável pela execução da aplicação, renderizando a página selecionada 
    pelo usuário conforme a seleção na caixa da sidebar.  
    """

    formation, submit = generate_header()
    
    if submit:
        # TODO
        pass


def generate_header():
    st.write("# FIFA Drafter")
    
    col1, col2 = st.columns([0.8, 0.2])
    formations_opt = cte.FORMATIONS.keys()
    formation_sel = col1.selectbox("Selecione a sua formação:", options=formations_opt)
    col2.write("###")
    submit = col2.button("Submeter", use_container_width=True)

    formation = cte.FORMATIONS[formation_sel]

    return formation, submit


def generate_squad_info(formation):
    generation_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    squad_info = requests.post(f"http://{os.environ['API_URL']}:{os.environ['API_PORT']}/generate_squad")
    
    st.write(f"""
        - **Data-hora de geração do time**: {generation_datetime}
        - **Informações do elenco**:
    """)
    _, col, _ = st.columns([1, 2, 1])
    col.dataframe(format_squad(squad_info))


def format_squad(squad_info):
    df = pd.DataFrame(squad_info).T
    
    return df


if __name__ == "__main__":
    config.set_page_config()
    run()