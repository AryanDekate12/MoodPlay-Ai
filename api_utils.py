import requests
import random
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAWG_API_KEY")

def fetch_games(params):

    url = "https://api.rawg.io/api/games"

    response = requests.get(url, params=params)

    data = response.json()

    games = []

    if "results" in data:

        for game in data["results"]:

            store_links = []

            # SAFE CHECK
            if "stores" in game and game["stores"]:

                for store in game["stores"]:

                    if "store" in store and "name" in store["store"]:
                        store_links.append(store["store"]["name"])

            games.append({
                "name": game.get("name"),
                "rating": game.get("rating"),
                "image": game.get("background_image"),
                "released": game.get("released"),
                "stores": store_links
            })

    return games


def get_games(genre, device):

    current_year = datetime.now().year

    if device == "Laptop":
        platform = "4"
    else:
        platform = "21,3"

    params = {
        "key": API_KEY,
        "genres": genre,
        "platforms": platform,
        "page_size": 30,
        "ordering": "-added",
        "dates": f"{current_year-6}-01-01,{current_year}-12-31"
    }

    games = fetch_games(params)

    random.shuffle(games)

    return games[:5]