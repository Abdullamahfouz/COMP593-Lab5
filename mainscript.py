import requests
import sys

DEV_KEY = 'i-8pVNkWG9SUtbh3DJ8XY9c-vcKxoFFQ'
PASTEBIN_URL = 'https://pastebin.com/api/api_post.php'

def main():
    pokemon_name = get_pokemon_name()
    pokemon_info = get_pokemon_info(pokemon_name)
    title, body = construct_paste_title_and_body(pokemon_info)
    paste_url = create_paste(title, body)
    print(f"Paste created: {paste_url}")

def get_pokemon_name():
    if len(sys.argv) < 2:
        print("Please provide a Pokémon name as a command line argument.")
        sys.exit(1)
    return sys.argv[1]

def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch Pokémon information for {pokemon_name}.")
        sys.exit(1)
    return response.json()

def construct_paste_title_and_body(pokemon_info):
    name = pokemon_info['name'].capitalize()
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    title = f"{name}'s Abilities"
    body = "\n".join(abilities)
    return (title, body)

def create_paste(title, body):
    data = {
        'api_dev_key': DEV_KEY,
        'api_option': 'paste',
        'api_paste_private': '1',
        'api_paste_expire_date': '1M',
        'api_paste_name': title,
        'api_paste_code': body
    }
    response = requests.post(PASTEBIN_URL, data=data)
    return response.text


if __name__ == '__main__':
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
