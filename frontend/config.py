# Defaults
import logging
import warnings
# Terceiras
import streamlit as st
# Proprietárias
import constants as cte


def set_logger() -> logging.Logger:
    """Instancia o Logger usado para a aplicação.

    Returns:
        logging.Logger: Retorna o Logger da aplicação. 
    """

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


def set_page_config() -> None:
    """Seta as configurações padrões para o Streamlit.
    """
    
    st.set_page_config(cte.APP_INFO["name"], page_icon=cte.APP_INFO["favicon"])  # Deve ficar aqui para nao bugar
    st.markdown("""<style>footer{visibility:hidden;}</style>""", unsafe_allow_html=True)
    warnings.filterwarnings("ignore")  # Só para parar de levantar warning do pandas no log...


LOGGER = set_logger()