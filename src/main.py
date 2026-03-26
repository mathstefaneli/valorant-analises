from analysis import load_data, map_probability

def main():
    df = load_data("data/matches.csv")

    team1 = "LOUD"
    team2 = "Fnatic"
    map_name = "Bind"

    prob = map_probability(df, team1, team2, map_name)

    print(f"Chance de {team1} ganhar da {team2} no mapa {map_name}: {prob:.2f}")

if __name__ == "__main__":
    main()