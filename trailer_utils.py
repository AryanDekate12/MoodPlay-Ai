import requests

import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_trailer(game_name):

    search_query = f"{game_name} game trailer"

    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": search_query,
        "key": YOUTUBE_API_KEY,
        "maxResults": 1,
        "type": "video"
    }

    response = requests.get(url, params=params)

    data = response.json()

    if "items" in data and len(data["items"]) > 0:

        video_id = data["items"][0]["id"]["videoId"]

        return f"https://www.youtube.com/watch?v={video_id}"

    return None