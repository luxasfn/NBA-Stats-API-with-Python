
import requests
import pandas as pd

def fetch_nba_game_stats(season=2023, max_pages=5):
    url = "https://www.balldontlie.io/api/v1/stats"
    all_stats = []

    print(f"Coletando estatísticas de jogos da temporada {season}...")

    for page in range(1, max_pages + 1):
        response = requests.get(url, params={
            "page": page,
            "per_page": 100,
            "seasons[]": season
        })
        data = response.json()
        all_stats.extend(data["data"])
        print(f"Página {page} coletada com {len(data['data'])} registros.")

    df = pd.DataFrame(all_stats)
    df.to_csv("../data/game_stats.csv", index=False)
    print(f"Dados salvos: {len(df)} registros em data/game_stats.csv")

if __name__ == "__main__":
    fetch_nba_game_stats()
