from coolname import generate_slug
import random

class Player(object):
    """A player is an object that issues guesses throughout the game.
       Based on the number of players within the game, the computer player will
       use past information collected from its own guesses - as well as the
       guesses of other players - in order to issue its newest guess.
    """

    def __init__(self, gtag = None, seed = 1, ptype = 'robot'):
        self.self = self
        self.gtag = generate_slug(2) if ptype == 'robot' else gtag
        self.ptype = ptype

    def create_guess(self, targets, target_len):
        guess = random.sample(targets, target_len)
        return guess
