from analysis import load_data, team_ranking

def main():
    df = load_data("data/matches.csv")

    ranking = team_ranking(df)

    print("=== RANKING DOS TIMES ===")
    for i, (team, wr) in enumerate(ranking, start=1):
        print(f"{i}. {team} - Win rate: {wr:.2f}")

if __name__ == "__main__":
    main()