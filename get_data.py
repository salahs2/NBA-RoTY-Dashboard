import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

pd.set_option('display.max_columns', None)

'''Getting list of rookies and their positions from tankathon.com'''
class Data: 
    def __init__(self, year : str):
        self.year = year 
        self.data = pd.DataFrame()
    def get_rookies(self,):
        # URL of the website to scrape
        url = f'https://www.tankathon.com/past_drafts/{self.year}'

        # Send an HTTP GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            soup_rookies = soup.find_all('div', 'mock-row-name')
            
            rookies = dict() # Key: Full Name Value: Draft Position
            count = 1
            for i in range(len(soup_rookies)):
                temp = soup_rookies[i] 
                if str(temp)[-20:-6] != 'Forfeited Pick':
                    rookies.update({str(temp)[27:-6] : count})
                    if type(count) is int and count < 58:
                        count+=1
                    else:
                        count = "Undrafted"
        return rookies
    def save_data_to_csv(self,):
        self.data.to_csv(f"data\\nba_rookie_data_{self.year}", index=False)
    
    def run(self): 
        rookies = self.get_rookies()

        '''Getting data from nba api'''
        nba_players = players.get_players()

        nba_rookies = []
        frames = []
        count = 0 
        for player in nba_players:
            if player["full_name"] in rookies:
                nba_rookies.append(player)
                #print(f"name: {player["full_name"]} id: {player['id']}")
                try:   
                    temp = playercareerstats.PlayerCareerStats(player_id=player['id']).get_data_frames()
                    temp[0]["PLAYER_ID"] = player["full_name"]
                    temp = temp[0]
                    #mask = temp['SEASON_ID'] == f"{self.year}-{str(int(self.year)+1)[2:]}"
                    temp = temp.drop(temp[temp['SEASON_ID'] != f"{self.year}-{str(int(self.year)+1)[2:]}"].index)
                    #temp = temp.drop(temp[temp['SEASON_ID'] == f"{self.year}-{str(int(self.year)+1)[2:]}"])
                    frames.append(temp)
                    print(f"{self.year}, iteration: {count}")
                    count+=1
                    time.sleep(1)
                except requests.Timeout:
                    print("The request timed out")
        self.data = pd.concat(frames)

        self.data['PLAYER_ID'].map(rookies)
        self.save_data_to_csv()


years = ["2022"]
for i in years:
    data = Data(year=i)

    data.run()


