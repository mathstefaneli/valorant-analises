from analysis import load_data, advanced_probability

def main():
    df = load_data("data/matches.csv")

    team1 = "LOUD"
    team2 = "Fnatic"

    prob = advanced_probability(df, team1, team2)

    print(f"Probabilidade AVANÇADA de {team1} ganhar da {team2}: {prob:.2f}")

if __name__ == "__main__":
    main()