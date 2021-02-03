from game.dealer import Dealer

"""
Info here
"""
STARTING_POINTS = 400
LOSING_LIMIT = 0
MAX_POINTS = 100
NEG_POINTS = 75

class Director:
    def __init__(self):
        self.keep_playing = True
        self.score = STARTING_POINTS
        self.user_guess = []
        self.dealer = Dealer()
        self.player_choice = []

    def start_game(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        self.dealt_card = self.dealer.deal_card()
        self.user_guess = self.dealer.get_input()

    def do_updates(self):
        if self.dealer.was_guess_correct == True:
            self.score += MAX_POINTS
        
        elif self.dealer.was_guess_correct == False:
            self.score -= NEG_POINTS

    def do_outputs(self):
        print("\n The card was:", self.dealer.dealt_card)
        print("Your score is:", self.score)
        
        if self.score == 0 or self.score < 0:
            print("You lost.. thanks for playing.")
            self.keep_playing = False

        self.player_choice = input("Keep playing? [y/n]: ")
        if self.player_choice == 'y' or 'Y':
            self.keep_playing = True
                 
        elif self.player_choice == 'n' or 'N':
            self.keep_playing = False
  
        # else:
        #     print("Wrong Input!")
        #     do_outputs()