# Built-in
import os
import pickle
from datetime import datetime, timedelta
# Terceiras
import streamlit as st
import pandas as pd
import numpy as np
# Proprietárias
import config
import constants as cte

def run() -> None:
    """Função principal responsável pela execução da aplicação, renderizando a página selecionada 
    pelo usuário conforme a seleção na caixa da sidebar.  
    """

    player, formation, submit = generate_header()
    
    if submit:

        if not in_cooldown(player):
            results = generate_squad(formation, player)
            display_results(results)
            save_results(results, player)
            text_results = format_results(results)
            display_download_button(text_results)
        
        else:
            cooldown_time = get_cooldown_time(player)
            st.warning(f"Você já gerou um elenco rencemente. Espere {cooldown_time} e tente novamente.")
            # with open(f"./results/{player}-squad.pkl", "rb") as file:
            #     results = pickle.load(file)
            # display_results(results)
            # text_results = format_results(results)
            # display_download_button(text_results)
            # Colocar elenco gerado aqui?


def generate_header():
    st.write("# FIFA Drafter")
    
    col1, col2, col3 = st.columns([0.425, 0.425, 0.15])
    
    players_opt = cte.PLAYERS
    player = col1.selectbox("Selecione o jogador:", options=players_opt)

    formations_opt = cte.FORMATIONS.keys()
    formation = col2.selectbox("Selecione a sua formação:", options=formations_opt)
    
    col3.write("###")
    submit = col3.button("Submeter", use_container_width=True)

    return player, formation, submit


def generate_squad(formation_label, player):
    formation = cte.FORMATIONS[formation_label]
    formation.extend(["RES" for _ in range(cte.NUMBER_OF_RES)])

    overall_ranges = list(cte.PROB_PER_OVER_RANGE.keys())
    overall_ranges_probs = list(cte.PROB_PER_OVER_RANGE.values())

    results = []
    df = pd.read_csv("./data/players.csv")
    for pos in formation:
        overall_range = np.random.choice(overall_ranges, p=overall_ranges_probs)
        lowest_ovr, highest_ovr = overall_range.split("-")
        lowest_ovr = int(lowest_ovr)
        highest_ovr = int(highest_ovr)

        df_filtered = df[(df["overall"] >= int(lowest_ovr)) & (df["overall"] <= int(highest_ovr)) & (df[pos] == 1)]
        while len(df_filtered) < cte.NUMBER_OF_PLAYERS:
            lowest_ovr -= lowest_ovr
            highest_ovr += highest_ovr
            df_filtered = df[(df["overall"] >= lowest_ovr) & (df["overall"] <= highest_ovr) & (df[pos] == 1)]

        player_info = df_filtered.apply(lambda s: f"{s['short_name']} ({s['long_name']}) - {s['overall']}", axis=1)
        possible_players = np.random.choice(player_info, cte.NUMBER_OF_PLAYERS, replace=False)
        
        results.append([pos, possible_players])
    
    dt = datetime.now()
    with open(f"./cooldown/{player}-lastsquad.pkl", "wb") as file:
        pickle.dump(dt, file)

    return results

def format_results(results):
    text = ""
    for res in results:
        pos = res[0]
        players = res[1]

        text += f"{pos}:\n"
        for p in players:
            text += f"\t -> {p}\n"
        text += "\n"

    return text

def save_results(results, player_name):
    with open(f"./results/{player_name}-squad.pkl", "wb") as file:                
        pickle.dump(results, file)
    
    # text = format_results(results)
    # with open(f"./results/{player_name}-squad.txt", "w") as file:                
    #     file.write(text)


def in_cooldown(player):
    if not os.path.isfile(f"./cooldown/{player}-lastsquad.pkl"):
        return False
    
    dt_now = datetime.now()
    with open(f"./cooldown/{player}-lastsquad.pkl", "rb") as file:
        dt_ls = pickle.load(file)

    dt_diff = (dt_now - dt_ls).total_seconds()

    if dt_diff >= cte.COLLDOWN_TIME:
        return False
    
    return True


def get_cooldown_time(player):
    dt_now = datetime.now()
    with open(f"./cooldown/{player}-lastsquad.pkl", "rb") as file:
        dt_ls = pickle.load(file)

    dt_diff = (dt_now - dt_ls).total_seconds()
    cooldown_time_sec = timedelta(seconds=(cte.COLLDOWN_TIME - dt_diff)).total_seconds()
    
    hours, remainder = divmod(cooldown_time_sec, 60*60)
    minutes, seconds = divmod(remainder,60)
    seconds = round(seconds)

    cooldown_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)

    return cooldown_time

def display_download_button(text_results):
    _, col, _ = st.columns([0.35, 0.3, 0.35])
    col.download_button("Baixar resultados em txt", text_results, file_name="fifadrafter-res.txt", 
                        use_container_width=True)


def display_results(results):
    # OP 1
    # text_results = format_results(results)
    # st.write(text_results.replace(">", "").replace("\n", "<br>"), unsafe_allow_html=True)

    # OP 2
    for res in results:
        pos = res[0]
        players = res[1]
        st.write(f"### {pos}")
        for p in players:
            st.write(f"* {p}")


if __name__ == "__main__":
    config.set_page_config()
    run()