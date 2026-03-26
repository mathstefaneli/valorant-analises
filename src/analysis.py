import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def win_rate(df, team):
    games = df[(df["team1"] == team) | (df["team2"] == team)]
    wins = df[df["winner"] == team]

    if len(games) == 0:
        return 0

    return len(wins) / len(games)