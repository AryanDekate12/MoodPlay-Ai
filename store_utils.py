def get_store_links(game_name, stores, device):

    query = game_name.replace(" ", "+")

    links = []

    if device == "Mobile":

        if "Google Play" in stores:
            links.append(("PlayStore", f"https://play.google.com/store/search?q={query}&c=apps"))

        if "Apple App Store" in stores:
            links.append(("App Store", f"https://apps.apple.com/us/search?term={query}"))

    else:

        if "Steam" in stores:
            links.append(("Steam", f"https://store.steampowered.com/search/?term={query}"))

        if "Epic Games" in stores:
            links.append(("Epic Games", f"https://store.epicgames.com/en-US/browse?q={query}"))

        if "GOG" in stores:
            links.append(("GOG", f"https://www.gog.com/en/games?query={query}"))

    return links