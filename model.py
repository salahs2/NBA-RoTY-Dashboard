import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Show all columns
pd.set_option('display.max_columns', None)

# Path to the folder containing the CSV files
folder_path = 'data/'

# List to hold individual DataFrames
frames = []

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(f"data/{filename}", index_col=False)
        
    # Append the DataFrame to the list
    frames.append(df)

df = pd.concat(frames, ignore_index=True)
# Adding per game stats 
df['PPG'] = df['PTS'] / df['GP']
df['RPG'] = df['REB'] / df['GP']
df['APG'] = df['AST'] / df['GP']
df['SPG'] = df['STL'] / df['GP']
df['BPG'] = df['BLK'] / df['GP']
df['TOPG'] = df['TOV'] / df['GP']
df['ORPG'] = df['OREB'] / df['GP']
df['DRPG'] = df['DREB'] / df['GP']
df['PFPG'] = df['PF'] / df['GP']
df['3PMPG'] = df['FG3M'] / df['GP']
df['3PAPPG'] = df['FG3A'] / df['GP']

roty = {
    "Victor Wembanyama": "SAS",
    "Paolo Banchero" : "ORL",
    "Scottie Barnes" : "TOR",
    "LaMelo Ball" : "CHA",
    "Ja Morant" : "MEM",
    "Luka Doncic" : "DAL",
    "Ben Simmons" : "PHI",
    "Malcolm Brogdon" : "MIL",
    "Karl-Anthony Towns" : "MIN",
    "Andrew Wiggins" : "MIN",
    "Michael Carter-Williams" : "PHI",
    "Damian Lillard" : "POR",
    "Kyrie Irving" : "CLE",
}
df['is_roty'] = df.apply(lambda row: 'Yes' if row['PLAYER_ID'] in roty.keys() and row['TEAM_ABBREVIATION'] in roty.values() else 'No', axis=1)


# Model 
X = df.drop(columns=['is_roty'])  # All columns except 'Y'
y = df['is_roty']  # The target column 'Y'
# Convert only the columns that can be cast to float
def convertible_to_float(series):
    try:
        series.astype(float)
        return True
    except ValueError:
        return False

# Filter out non-float convertible columns
X_numeric = X.loc[:, X.apply(convertible_to_float, axis=0)]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_numeric, y, test_size=0.2, random_state=42)


# Create an SVM model
forest = RandomForestClassifier()
# Fit the model on the training data
forest.fit(X_train, y_train)

# Predict on the test data
y_pred = forest.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

df['model_predict'] = forest.predict(X_numeric)

df.to_csv("data/Model_Data", index=False)