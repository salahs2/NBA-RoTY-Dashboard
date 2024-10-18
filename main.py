import streamlit as st
import pandas as pd
import os
from pathlib import Path
from faker import Faker
from PIL import Image
from io import BytesIO
import base64
# Set the directory where your images are stored
image_directory = "C:/Users/salah/GitHub/NBA-RoTY-Dashboard/assets/Teams"

# Load the CSV file
df = pd.read_csv("nba_rookie_data")

images = {
    
    "ATL" : "https://upload.wikimedia.org/wikipedia/en/thumb/2/24/Atlanta_Hawks_logo.svg/1200px-Atlanta_Hawks_logo.svg.png",
    "BOS" : "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Boston_Celtics.svg/800px-Boston_Celtics.svg.png",
    "CHI" : "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Chicago_Bulls_logo.svg/1200px-Chicago_Bulls_logo.svg.png",
    "BKN" : "https://upload.wikimedia.org/wikipedia/en/thumb/4/40/Brooklyn_Nets_primary_icon_logo_2024.svg/1200px-Brooklyn_Nets_primary_icon_logo_2024.svg.png",
    "CLE" : "https://seeklogo.com/images/N/nba-cleveland-cavaliers-logo-EC287BF14E-seeklogo.com.png",
    "CHA" : "https://upload.wikimedia.org/wikipedia/en/c/c4/Charlotte_Hornets_%282014%29.svg",
    "NYK" : "https://upload.wikimedia.org/wikipedia/en/thumb/2/25/New_York_Knicks_logo.svg/1200px-New_York_Knicks_logo.svg.png",
    "DET" : "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Logo_of_the_Detroit_Pistons.svg/1200px-Logo_of_the_Detroit_Pistons.svg.png",
    "MIA" : "https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Miami_Heat_logo.svg/640px-Miami_Heat_logo.svg.png",
    "PHI" : "https://upload.wikimedia.org/wikipedia/en/thumb/0/0e/Philadelphia_76ers_logo.svg/1200px-Philadelphia_76ers_logo.svg.png",
    "IND" : "https://upload.wikimedia.org/wikipedia/en/1/1b/Indiana_Pacers.svg",
    "ORL" : "https://upload.wikimedia.org/wikipedia/en/thumb/1/10/Orlando_Magic_logo.svg/1200px-Orlando_Magic_logo.svg.png",
    "TOR" : "https://upload.wikimedia.org/wikipedia/sco/thumb/3/36/Toronto_Raptors_logo.svg/241px-Toronto_Raptors_logo.svg.png?20190614044705",
    "MIL" : "https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Milwaukee_Bucks_logo.svg/640px-Milwaukee_Bucks_logo.svg.png",
    "WAS" : "https://upload.wikimedia.org/wikipedia/en/thumb/0/02/Washington_Wizards_logo.svg/800px-Washington_Wizards_logo.svg.png",
    "DEN" : "https://upload.wikimedia.org/wikipedia/en/7/76/Denver_Nuggets.svg",
    "GSW" : "https://upload.wikimedia.org/wikipedia/en/thumb/0/01/Golden_State_Warriors_logo.svg/1200px-Golden_State_Warriors_logo.svg.png",
    "DAL" : "https://upload.wikimedia.org/wikipedia/en/thumb/9/97/Dallas_Mavericks_logo.svg/1200px-Dallas_Mavericks_logo.svg.png",
    "MIN" : "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Minnesota_Timberwolves_logo.svg/1200px-Minnesota_Timberwolves_logo.svg.png",
    "LAC" : "https://upload.wikimedia.org/wikipedia/en/thumb/e/ed/Los_Angeles_Clippers_%282024%29.svg/1200px-Los_Angeles_Clippers_%282024%29.svg.png",
    "HOU" : "https://upload.wikimedia.org/wikipedia/en/2/28/Houston_Rockets.svg",
    "OKC" : "https://upload.wikimedia.org/wikipedia/en/5/5d/Oklahoma_City_Thunder.svg",
    "LAL" : "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Los_Angeles_Lakers_logo.svg/640px-Los_Angeles_Lakers_logo.svg.png",
    "MEM" : "https://upload.wikimedia.org/wikipedia/sco/thumb/f/f1/Memphis_Grizzlies.svg/203px-Memphis_Grizzlies.svg.png?20170408175705", 
    "POR" : "https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Portland_Trail_Blazers_logo.svg/1200px-Portland_Trail_Blazers_logo.svg.png",
    "PHX" : "https://upload.wikimedia.org/wikipedia/en/d/dc/Phoenix_Suns_logo.svg",
    "NOP" : "https://upload.wikimedia.org/wikipedia/en/0/0d/New_Orleans_Pelicans_logo.svg",
    "UTA" : "https://logodownload.org/wp-content/uploads/2021/07/utah-jazz-logo-0.png", 
    "SAC" : "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/SacramentoKings.svg/800px-SacramentoKings.svg.png",
    "SAS" : "https://upload.wikimedia.org/wikipedia/en/a/a2/San_Antonio_Spurs.svg"
}
# Create a new column with full image paths
df['TEAM_ABBREVIATION'] = df['TEAM_ABBREVIATION'].map(images)

st.set_page_config(layout="wide")
st.title(":basketball: NBA 2023 Rookie Of The Year Dashboard :basketball:")
st.data_editor(
    df,
    column_config={
        "TEAM_ABBREVIATION" : st.column_config.ImageColumn(
            ""
        ),
        "PLAYER_ID" : "Player Name",
        "PLAYER_AGE" : "Age",
        "GP" : "Games Played",
        "GS" : "Games something?",
        "MIN" : "Minutes Played",
        "FGM" : "Field Goals Made",
        "FGA" : "Field Goals Attempted",
        "FG_PCT" : "Field Goal %",
        "FG3M" : "3-Pointers Made",
        "FG3A" : "3-Pointers Attempted",
        "FG3_PCT" : "Field Goal %"
    },
    column_order=("TEAM_ABBREVIATION", "PLAYER_ID", "SEASON_ID", "PLAYER_AGE", "GP", "GS", "MIN", "FGM", "FGA", "FG_PCT", "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA", "FT_PCT", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF", "PTS"),
    width= 1500,
    hide_index=True
    
)