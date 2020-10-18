'''
The purpose of this script is to generate synthetic data for the purpose
of training machine learning models to derive strategies based for
playing the mastermind game.
'''

from referree import Referree
import random
import pandas as pd
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Create a ref to observe the game
referree = Referree(play_type = 'robot', games = 10, players = 4)

print(referree.officiate())
total_manufactured_data = pd.concat(referree.games_stats, axis = 0)
total_manufactured_data.to_csv('test.csv')
