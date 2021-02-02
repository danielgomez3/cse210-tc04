from game.dealer import Dealer

"""
Info here
"""
class Director:
    def __init__(self):
        self.keep_playing = True
        self.thrower = Dealer()

    def start_game(self):
        pass