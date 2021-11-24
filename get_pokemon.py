import requests
from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)

pokemon = response.json()
pprint(pokemon['name'])
pprint(pokemon['height'])
pprint(pokemon['weight'])


moves = pokemon['moves']
for move in moves:
    print(move['move']['name'])