import pandas as pd
from player import Player
from game import Game

def play_game(self, players):
    # TODO Flip the coin - randomize the order of the players
    g = Game(players = players)

    # Inform the players of the available options:
    options = g.target_data.Pokemon.values
    options.sort()
    g.random_move_order()

    # create the order pattern for players to follow
    g.create_turns()

    # Facilitate the moves with robot players
    move_counter = 1
    for player in g.game_move_order:

        # create a random guess based off the available answers
        player_guess = player.create_guess(g.options, g.targets, g.turn_guesses)
        g.turn_guesses.append(player_guess)

        # check if the guess was right, both content and order
        g.hitblow_check(g.target_data.Pokemon.values, player_guess, move_counter)

        # check on the status of the game
        g.game_status(player, player_guess, move_counter)

        # if the correct order of all elements is satisfied, then end the game
        if g.hitblow[move_counter-1]['hit'] == g.targets:
            break

        move_counter += 1

    return g


class Referree(object):
    """Even though the referree won't actually be keeping
       track of the rules here... the purpose is for her to
       capture the end result of the overall game, and store
       it so that players in the future can benefit from each
       match.

       The ontology is:
       Referree > Players > Game
    """

    def __init__(self, play_type, games = 1, players = 2):
        self.self = self
        self.games = games
        self.play_type = play_type
        self.players = players

        # record info
        self.games_stats = []

    def officiate(self):
        # TODO instantiate the players
        player_bucket = [Player() for num_players in range(0, self.players)]

        print('playing', str(self.games), 'games')
        for game_round in range(self.games):
            print('officiating game: ', str(1 + game_round))
            game_info = play_game(self, player_bucket)

            # capture the guessing data
            game_guesses = pd.DataFrame(game_info.turn_guesses)
            game_guesses.columns = ['guess_' + str(target_num + 1) for target_num in range(game_info.targets)]

            # capture the hit blow check data
            game_hit_blow = pd.DataFrame(game_info.hitblow)

            # capture the turn info
            game_move_order = pd.DataFrame([x.gtag for x in game_info.game_move_order], columns = ['player_tag'])

            # put all the fields together
            total_game_pd = pd.concat([game_guesses, game_hit_blow, game_move_order], axis = 1).dropna()
            total_game_pd['game_number'] = game_round

            self.games_stats.append(total_game_pd)
