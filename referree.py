

class Referree(object):
    """Even though the referree won't actually be keeping
       track of the rules here... the purpose is for her to
       capture the end result of the overall game, and store
       it so that players in the future can benefit from each
       match.

       The ontology is:
       Referree > Players > Game
    """

    def __init__(self, play_type, rounds = 1):
        self.self = self
        self.rounds = rounds
        self.play_type = play_type

        # record info
        self.games = []

        # results calculation
        self.stats = []

    def add_game(self, game):
        return self.games.append(game)
