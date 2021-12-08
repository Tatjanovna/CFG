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

    print("Your Pokemon for this round is: {}.\nID:{}\nHEIGHT:{}\nWEIGHT:{}\n".format(player1_card['name'].title(),player1_card['id'],player1_card['height'],player1_card['weight']))

    player2 = deck[1]

    url2 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player2)
    response_p2 = requests.get(url2)
    pokemon_p2 = response_p2.json()
    player2_card = {
        'name' : pokemon_p2['name'],
        'id' : pokemon_p2['id'],
        'height' : pokemon_p2['height'],
        'weight' : pokemon_p2['weight'],
        }

    print("Your opponent has {}.\n".format(player2_card['name'].title()))


    global pokestat
    pokestat = input("Which stat do you want to compare? height, weight, id: ")

    while pokestat not in ('height', 'weight', 'id'):
        pokestat = input("Sorry, please enter either height, weight or id: ")

    pokestat_p1 = player1_card[pokestat]
    pokestat_p2 = player2_card[pokestat]


    if pokestat_p1 > pokestat_p2:
        print("You win round {}! Your {} stat of {} bis higher than player two's {}.".format(round, pokestat, pokestat_p1, pokestat_p2))
        p1score = p1score+1
        print("The score is now P1: {} - P2: {}\n".format(p1score,p2score))
    elif pokestat_p1 == pokestat_p2:
        print("Draw! {}! Your {} stat of {} is the same as player two's {}.".format(round, pokestat, pokestat_p1, pokestat_p2))
        print("The score is now P1: {} - P2: {}\n".format(p1score,p2score))
    else:
        print("You lost round {}! Your {} stat of {} did not beat player two's {}.".format(round, pokestat, pokestat_p1, pokestat_p2))
        p2score = p2score+1
        print("The score is now P1: {} - P2: {}\n".format(p1score,p2score))

    with open('pokescore.txt', 'a') as poke_file:
        poke_file.write('P1: '+str(p1score)+' - P2: ')
        poke_file.write(str(p2score)+'\n')



def totalrounds():

    global round
    for round in range(rounds):
        round = round+1
        game_round()

    again = input("Would you like to play again? y/n ")


    if again == 'y':
        totalrounds()
    else:
        print("Goodbye!")


totalrounds()
    
