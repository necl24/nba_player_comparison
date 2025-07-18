import streamlit as st
import pandas as pd
import numpy as np

st.title('NBA COMPARISON APP')

nbaplayername = st.text_input("Enter NBA Player Name")
Season = st.text_input("Season")

comparison_button = st.button("Find Comparable Players")

if comparison_button:
    st.write(f"You entered Player: {nbaplayername}")
    st.write(f"You entered Season: {Season}")
    st.info("Your player is simliar to ...")
