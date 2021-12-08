import random
import requests


while True:
    try:
        rounds = int(input("How many rounds of PokeTrumps would you like to play? "))
        print()
    except ValueError:
        print("Sorry, please enter number again.\n")
        continue
    else:
        break


p1score = 0
p2score = 0

with open('pokes-core.txt', 'w+') as poke_file:
    poke_file.write('Poke-trumps Score Sheet\n')


def game_round():

    deck = random.sample(range(1,151),2)
    player1 = deck[0]

    global p1score
    global p2score


    url1 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player1)
    response_p1 = requests.get(url1)
    pokemon_p1 = response_p1.json()

    player1_card = {
        'name': pokemon_p1['name'],
        'id': pokemon_p1['id'],
        'height': pokemon_p1['height'],
        'weight': pokemon_p1['weight'],
        }

    
