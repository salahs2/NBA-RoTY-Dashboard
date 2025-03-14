import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px
import os
# Set the directory where your images are stored
image_directory = "C:/Users/salah/GitHub/NBA-RoTY-Dashboard/assets/Teams"

# Load the CSV file
df2 = pd.read_csv("nba_rookie_data")

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
df2['TEAM_ABBREVIATION'] = df2['TEAM_ABBREVIATION'].map(images)

st.set_page_config(layout="wide")


roty = {
    "2024" : "Undetermined" , 
    "2023" : "Victor Wembanyama",
    "2022" :"Paolo Banchero" ,
    "2021" :"Scottie Barnes" ,
    "2020" :"LaMelo Ball" ,
    "2019" :"Ja Morant" ,
    "2018" :"Luka Doncic" ,
    "2017" :"Ben Simmons" ,
    "2016" :"Malcolm Brogdon" ,
    "2015" :"Karl-Anthony Towns" ,
    "2014" :"Andrew Wiggins" ,
    "2013" :"Michael Carter-Williams" ,
    "2012" :"Damian Lillard" ,
    "2011" :"Kyrie Irving" ,
}
year = {
    '2024-25' : '2024',
    '2023-24' : '2023',
    '2022-23' : '2022',
    '2021-22' : '2021',
    '2020-21' : '2020',
    '2019-20' : '2019',
    '2018-19' : '2018',
    '2017-18' : '2017',
    '2016-17' : '2016',
    '2015-16' : '2015'
}

# Load predictions
def load_data():
    file_path = "data/Predicted_ROTY.csv"
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error("Predicted_ROTY.csv not found. Run the model first!")
        return None

df = load_data()

if df is not None:
    st.title("NBA Rookie of the Year Predictions 🏀")
    
    # Select Year
    year_selected = st.selectbox("Select Year:", sorted(df['year'].unique(), reverse=True))
    df2 = pd.read_csv(f"data/nba_rookie_data_{year[year_selected]}")
    df2['TEAM_ABBREVIATION'] = df2['TEAM_ABBREVIATION'].map(images)

    st.data_editor(
        df2,
        column_config={
            "TEAM_ABBREVIATION" : st.column_config.ImageColumn(
                ""
            ),
            "PLAYER_ID" : "Player Name",
            "PLAYER_AGE" : "Age",
            "GP" : "Games Played",
            "GS" : "Games Started",
            "MIN" : "Minutes Played",
            "FGM" : "Field Goals Made",
            "FGA" : "Field Goals Attempted",
            "FG_PCT" : "Field Goal %",
            "FG3M" : "3-Pointers Made",
            "FG3A" : "3-Pointers Attempted",
            "FG3_PCT" : "Field Goal %",
            "FTM" : "Free Throws Made",
            "OREB" : "Offensive Rebounds",
            "DREB" : "Defensive Rebounds",
            "REB" : "Rebounds",
            "AST" : "Assists", 
            "STL" : "Steals",
            "BLK" : "Blocks",
            "TOV" : "Turnovers",
            "PF" : "Personal Fouls",
            "FTA" : "Free Throws Attempted",
            "FT_PCT" : "Free Throw %",
            "PTS" : "Points"
        },
        column_order=("TEAM_ABBREVIATION", "PLAYER_ID", "SEASON_ID", "PTS", "REB", "AST", "STL", "BLK", "TOV",  "PLAYER_AGE", "GP", "GS", "MIN", "FGM", "FGA", "FG_PCT", "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA", "FT_PCT", "OREB", "DREB", "PF"),
        width= 1500,
        hide_index=True
        
    )
    # Get Prediction for Selected Year
    roty_player = df[df['year'] == year_selected]
    if not roty_player.empty:
        player_id = roty_player['PLAYER_ID'].values[0]
        team = roty_player['TEAM_ABBREVIATION'].values[0]
        prob = roty_player['roty_probability'].values[0]
        
        st.subheader(f"Predicted Rookie of the Year for {year_selected}")
        st.write(f"🏆 **Player ID:** {player_id}")
        st.write(f"🏀 **Team:** {team}")
        st.write(f"📊 **ROTY Probability:** {prob:.2%}")
    else:
        st.warning(f"No prediction found for {year_selected}.")
    
    # # Plot Top Players per Year
    # st.subheader("ROTY Probability by Year")
    # fig = px.bar(df, x='year', y='roty_probability', hover_data=['PLAYER_ID', 'TEAM_ABBREVIATION'],
    #              text='roty_probability', labels={'roty_probability': 'Probability'},
    #              title="Top Predicted Rookies by Year")
    # st.plotly_chart(fig)