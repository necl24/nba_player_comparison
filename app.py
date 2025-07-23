import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

data_path = data/Player Per Game.csv

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

# Define the features to use for comparison (8 core stats)
comparison_features = [
    'pts_per_game', 'trb_per_game', 'ast_per_game', 'stl_per_game', 'blk_per_game',
    'fg_percent', 'x3p_percent', 'ft_percent'
]

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
                st.error(f"Player '{player_name_input}' in season '{normalized_season_input}' not found in the dataset. Please check spelling and season format.")
            else:
                st.success(f"Found stats for {player_name_input} in {normalized_season_input}:")
                st.dataframe(target_player_season_df.head(1))

                st.markdown("---")


                target_stats_for_comparison = target_player_season_df[comparison_features].values

                target_mask = (df['player'].str.lower() == normalized_player_input) & \
                              (df['season'] == normalized_season_input)

                comparison_pool_df = df[~target_mask].copy()

                comparison_pool_df[comparison_features] = comparison_pool_df[comparison_features].fillna(0)

                display_cols_for_preview = ['player', 'season', 'team'] + comparison_features
            

                st.info("Now, standardizing data and calculating similarities...")
            
                scaler = StandardScaler()
                scaled_comparison_pool_stats = scaler.fit_transform(comparison_pool_df[comparison_features])

                scaled_target_stats = scaler.transform(target_stats_for_comparison)

                st.success("Data standardized successfully!") 

                distances = euclidean_distances(scaled_target_stats, scaled_comparison_pool_stats)

                # Add the new column using direct assignment
                comparison_pool_df['Distance'] = distances[0]
                sorted_comparisons =  comparison_pool_df.sort_values(by='Distance',ascending=True)
                top_comparable_players =  sorted_comparisons.head(5)
                st.write("Top 5 Comparable Players ") 

                st.dataframe(top_comparable_players)



        except ValueError:
            st.error("Please enter a valid year for the Season (e.g., 2017).")
        except KeyError as e:
            st.error(f"A column expected for filtering or comparison was not found. Please check column names in your CSV. Error: {e}")
    else:
        st.warning("Please enter both a player name and a season to find comparisons.")







