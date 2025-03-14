# :basketball: NBA Rookie Of The Year Dashboard :basketball:
## Overview
This project predicts the NBA Rookie of the Year (ROTY) for each season based on player statistics. A Random Forest model is trained using historical player data, and a Streamlit dashboard is used to visualize predictions. see a live demo [here](https://roty-dashboard.streamlit.app/) 
## Features
**Data Processing**: Reads player statistics from multiple CSV files and calculates per-game metrics.

**Machine Learning Model**: Uses a Random Forest Classifier to predict the likelihood of a player winning ROTY.

**Yearly Predictions**: Ensures that every year has a predicted ROTY based on model probability.

**Interactive Dashboard**: Built with Streamlit to display predictions and trends.

## NBA Rookie Data Scraper

This Python script scrapes NBA rookie data from [Tankathon](https://www.tankathon.com) and retrieves player statistics from the NBA API. The data is saved in a CSV file for further analysis.

This script scrapes NBA rookie information from Tankathon for a given draft year and combines it with career stats from the NBA API. The final dataset, which includes rookies' draft positions and their statistics, is saved as a CSV file.

### Prerequisites

Ensure you have the following Python libraries installed:

```bash
pip install requests beautifulsoup4 pandas numpy nba_api streamlit
```

## Rookie of the Year Dashboard
This project is a Streamlit-based web application that visualizes NBA rookie data. It loads and displays a dataset of NBA rookies along with their career stats and enhances the presentation by associating team logos with each player.

