
from poke_api import get_pokemon_info
from pastebin_api import post_new_paste

def get_pokemon_name():
    """
    Gets the Pokémon name from the command line parameter.

    Returns:
        str: The Pokémon name input as a command line parameter.

    """
    import sys
    if len(sys.argv) < 2:
        print("Please provide the name of the Pokémon as a command line argument.")
        sys.exit(1)
    return sys.argv[1]

def construct_paste_title_and_body_text(pokemon_info):
    """
    Constructs the title and body text for the new paste.

    Args:
        pokemon_info (dict): A dictionary containing all the Pokémon information fetched from the PokéAPI.

    Returns:
        tuple: The paste title and body text as strings in a tuple.
    """
    name = pokemon_info['name'].capitalize()
    abilities = '- ' + '\n- '.join([ability['ability']['name'].replace('-', ' ') for ability in pokemon_info['abilities']])
    title = f"{name}'s Abilities"
    body_text = abilities
    return (title, body_text)

def main():
    pokemon_name = get_pokemon_name()
    print(f"Getting information for {pokemon_name}...")
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info is not None:
        title, body_text = construct_paste_title_and_body_text(pokemon_info)
        url = post_new_paste(title, body_text, '1M', True)
        if url is not None:
            print(f"Posting new paste to PasteBin...success\n{url}")
        else:
            print("Posting new paste to PasteBin...failure")
    else:
        print(f"Getting information for {pokemon_name}...failure")

if __name__ == '__main__':
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
