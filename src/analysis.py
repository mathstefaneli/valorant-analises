import pandas as pd

# Carrega os dados do CSV
def load_data(path):
    return pd.read_csv(path)


# Calcula o win rate geral de um time
def win_rate(df, team):
    games = df[(df["team1"] == team) | (df["team2"] == team)]
    wins = df[df["winner"] == team]

    if len(games) == 0:
        return 0

    return len(wins) / len(games)


# Probabilidade baseada no confronto direto
def match_probability(df, team1, team2):
    matches = df[
        ((df["team1"] == team1) & (df["team2"] == team2)) |
        ((df["team1"] == team2) & (df["team2"] == team1))
    ]

    if len(matches) == 0:
        return 0.5  # sem dados

    wins_team1 = matches[matches["winner"] == team1]

    return len(wins_team1) / len(matches)


# Probabilidade mais avançada (misturando fatores)
def advanced_probability(df, team1, team2):
    wr1 = win_rate(df, team1)
    wr2 = win_rate(df, team2)

    h2h = match_probability(df, team1, team2)

    # peso maior pro confronto direto
    prob = (h2h * 0.6) + (wr1 * 0.4)

    return prob