import streamlit as st
import pandas as pd
import numpy as np

FilePath = "/Users/neilaeron/Documents/NBA_Comparison/data/Player Per Game.csv"

@st.cache_data
def load_nba_data(FilePath):
    df = pd.read_csv(FilePath)
    return df

df = load_nba_data(FilePath)

st.dataframe(df)  


st.title('NBA COMPARISON APP')

nbaplayername = st.text_input("Enter NBA Player Name")
Season = st.text_input("Season")

comparison_button = st.button("Find Comparable Players")

if comparison_button:
    st.write(f"You entered Player: {nbaplayername}")
    st.write(f"You entered Season: {Season}")
    st.info("Your player is simliar to ...")
