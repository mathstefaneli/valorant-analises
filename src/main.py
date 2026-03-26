from analysis import load_data, calculate_elo

def main():
    df = load_data("data/matches.csv")

    ratings = calculate_elo(df)

    print("=== RANKING ELO ===")
    
    # ordenar do maior pro menor
    sorted_teams = sorted(ratings.items(), key=lambda x: x[1], reverse=True)

    for i, (team, rating) in enumerate(sorted_teams, start=1):
        print(f"{i}. {team} - Elo: {rating:.0f}")

if __name__ == "__main__":
    main()