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

def team_ranking(df):
    teams = set(df["team1"]).union(set(df["team2"]))

    ranking = []

    for team in teams:
        wr = win_rate(df, team)
        ranking.append((team, wr))

    # ordenar do maior pro menor
    ranking.sort(key=lambda x: x[1], reverse=True)

    return ranking

def calculate_elo(df, k=32):
    teams = set(df["team1"]).union(set(df["team2"]))

    # todos começam com 1000
    ratings = {team: 1000 for team in teams}

    for _, row in df.iterrows():
        team1 = row["team1"]
        team2 = row["team2"]
        winner = row["winner"]

        r1 = ratings[team1]
        r2 = ratings[team2]

        # probabilidade esperada
        expected1 = 1 / (1 + 10 ** ((r2 - r1) / 400))
        expected2 = 1 / (1 + 10 ** ((r1 - r2) / 400))

        # resultado real
        score1 = 1 if winner == team1 else 0
        score2 = 1 if winner == team2 else 0

        # atualização
        ratings[team1] = r1 + k * (score1 - expected1)
        ratings[team2] = r2 + k * (score2 - expected2)

    return ratings

def map_win_rate(df, team, map_name):
    games = df[
        ((df["team1"] == team) | (df["team2"] == team)) &
        (df["map"] == map_name)
    ]

    wins = df[
        (df["winner"] == team) &
        (df["map"] == map_name)
    ]

    if len(games) == 0:
        return 0

    return len(wins) / len(games)

def map_probability(df, team1, team2, map_name):
    wr1 = map_win_rate(df, team1, map_name)
    wr2 = map_win_rate(df, team2, map_name)

    if wr1 + wr2 == 0:
        return 0.5

    return wr1 / (wr1 + wr2)