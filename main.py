
from referree import Referree
from game import Game
from player import Player
import random
import pprint

pp = pprint.PrettyPrinter(indent=4)
# Create a ref to observe the game
r = Referree(play_type = 'test')

# Create the players
p1 = Player()
# print("Welcome: ", p1.gtag)

p2 = Player()
# print("Welcome: ", p2.gtag)

player_list = [p1, p2]

# Officiate the game
g = Game(players = player_list)
g.random_move_order()
g.create_turns()

# Play the game
g.randomize_targets()

move_counter = 1
for player in g.game_move_order:
    options = g.target_data.Pokemon.values

    # TODO Implement historical check of previous guesses
    player_guess = player.create_guess(list(options), g.targets)
    g.turn_guesses.append(player_guess)
    g.hitblow_check(player_guess, move_counter)
    g.game_status(player, player_guess, move_counter)

    # local checks
    # pp.pprint([player.gtag, player_guess, g.target_pattern,
    #            g.hitblow[move_counter-1]['hit'], g.hitblow[move_counter-1]['blow']])

    if g.winner == None:
        continue
    else:
        break

    move_counter += 1

# report the results to the referree
print(g.turn_guesses)
