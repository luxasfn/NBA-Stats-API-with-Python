
import requests
import pandas as pd

def fetch_nba_players():
    url = "https://www.balldontlie.io/api/v1/players"
    players = []
    page = 1

    print("Coletando dados dos jogadores...")

    while True:
        response = requests.get(url, params={"page": page, "per_page": 100})
        data = response.json()
        players.extend(data["data"])
        if not data["meta"]["next_page"]:
            break
        page += 1

    df = pd.DataFrame(players)
    df.to_csv("../data/players.csv", index=False)
    print(f"Dados salvos: {len(df)} jogadores em data/players.csv")

if __name__ == "__main__":
    fetch_nba_players()
