import requests


def get_pokemon_info(name_or_id):
    """
    Fetches information for a specified Pokémon from the PokéAPI.

    Args:
        name_or_id (str or int): The name or PokéDex number of the Pokémon to fetch.

    Returns:
        dict: A dictionary containing all the Pokémon information fetched from the PokéAPI, if retrieved successfully.
        None: If the Pokémon information is not fetched successfully.

    """
    url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id.lower().strip()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get Pokémon info for {name_or_id}. Error code: {response.status_code}")
        return None