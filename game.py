import pandas as pd
import random
import itertools

class Game(object):
    """A game constitutes the parameters that determine how
       a players will compete with one another. In the traditional
       game, this is a two player game that has up to 8 guesses
       (4 guesses each, per player), and up to 6 different balls
       to guess from.

       Given my interest in increasing the complexity in the game,
       while I will keep these defaults, I will also provide different
       options for game parameters to be **greatly** altered.
    """

    def __init__(self, players, turns = 8, targets = 3, sprites = 'pokemon', options = 5):
        self.self = self
        self.players = players
        self.targets = targets
        self.players_num = len(self.players)
        self.move_order = None
        self.game_move_order = None
        self.turns = int(turns)
        self.total_turns = len(players) * turns
        self.sprites_choice = pd.read_csv('sprites/pokemon.csv') if sprites == 'pokemon' else None

        # Sampling also randomizes the order
        self.target_data = self.sprites_choice.sample(options)
        self.options = list(self.target_data.Pokemon.values)
        self.target_pattern = None

        # turn info
        self.turn_guesses = []
        self.hitblow = []
        self.winner = None
        self.winner_combo = None
        self.num_guesses = None

        # outcome info
        self.turn_stats = []

    def random_move_order(self):
        # pnames = [x.gtag for x in self.players]
        random.shuffle(self.players)
        self.move_order = [self.players]

    def create_turns(self):
        game_order = list(itertools.chain.from_iterable(self.move_order * self.turns))
        self.game_move_order = game_order

    def randomize_targets(self):
        pokedata = self.target_data.Pokemon.values[0:self.targets]
        self.target_pattern = list(pokedata)

    def hitblow_check(self, guess, move):
        blow = 0
        hit = 0

        counter = 0
        for val in guess:
            if val == self.target_pattern[counter]:
                hit += 1
            elif val != self.target_pattern[counter] and val in self.target_pattern:
                blow += 1
            else:
                pass
            counter += 1

        correct = hit + blow
        return self.hitblow.append({'move': move, 'hit': hit, 'blow': blow, 'miss': len(guess) - correct})

    def game_status(self, player, guess, move):
        if self.hitblow[move-1]['hit'] == self.targets:
            game_status = 'winner'
            self.winner = player.gtag
            self.winner_combo = guess
            self.num_guesses = move

        elif (self.hitblow[move-1]['hit'] < self.targets) & (move == self.total_turns):
            game_status = 'fail'
            self.winner = 'none'

        else:
            self.num_guesses = move
