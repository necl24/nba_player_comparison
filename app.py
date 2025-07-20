import streamlit as st
import pandas as pd
import numpy as np

data_path = "/Users/neilaeron/Documents/NBA_Comparison/data/Player Per Game.csv"

@st.cache_data
def load_nba_data(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    return df

df = load_nba_data(data_path)

st.dataframe(df)
st.title('NBA COMPARISON APP')

player_name_input = st.text_input("Enter NBA Player Name", "Russell Westbrook")
season_input = st.text_input("Season", "2017")

comparison_button = st.button("Find Comparable Players")

if comparison_button:
    if player_name_input and season_input:
        try:
            normalized_player_input = player_name_input.strip().lower()
            normalized_season_input = int(season_input.strip())

            target_player_season_df = df[
                (df['player'].str.lower() == normalized_player_input) &
                (df['season'] == normalized_season_input)
            ]

            if target_player_season_df.empty:
                st.error(f"Player '{player_name_input}' in season '{season_input}' not found in the dataset. Please check spelling and season format.")
            else:
                st.success(f"Found stats for {player_name_input} in {season_input}:")
                st.dataframe(target_player_season_df.head(1))

        except ValueError:
            st.error("Please enter a valid year for the Season (e.g., 2017).")
        except KeyError as e:
            st.error(f"A column expected for filtering was not found. Please check column names in your CSV. Error: {e}")
    else:
        st.warning("Please enter both a player name and a season to find comparisons.")
