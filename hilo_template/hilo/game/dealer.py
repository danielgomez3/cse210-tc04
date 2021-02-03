import random
"""
info here
"""
class Dealer:
    def __init__(self): 
        self.was_guess_correct = None
        self.random_card = 0
        self.dealt_card = 0
        self.guess = []

#TODO: Cause this to increment after it is true! DO it here
    def guessed_higher(self):
        if self.random_card < self.dealt_card:
            self.was_guess_correct = True

        else:
            self.was_guess_correct = False

#TODO: Cause this to increment after it is true! DO it here
    def guessed_lower(self):
        if self.random_card < self.dealt_card:
            self.was_guess_correct = True

        else:
            self.was_guess_correct = False


    def deal_card(self):
        self.random_card = random.randint(1,13)
        print("\nThe Card is: ", self.random_card)
        self.dealt_card = random.randint(1,13)

    def get_input(self):
        self.guess = 0
        self.guess = input("Higher or lower? [h/l]: ")
        # Return response to the director. And basic error handling
        if self.guess == 'h' or 'H':
            self.guessed_higher()
                 
        elif self.guess == 'l' or 'L':
            self.guessed_lower()

        else:
            print("Wrong Input!")
            get_input()


