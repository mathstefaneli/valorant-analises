from analysis import load_data, win_rate

def main():
    df = load_data("data/matches.csv")

    team = "LOUD"
    rate = win_rate(df, team)

    print(f"Win rate da {team}: {rate:.2f}")

if __name__ == "__main__":
    main()