import random
"""
The Dealer class does all the heavy lifting and logic for the program to funciton
"""
class Dealer:
    """
    Variables are initialized here. Never outside the init unless specified 
    """
    def __init__(self): 
        self.was_guess_correct = None
        self.random_card = 0
        self.dealt_card = 0
        self.guess = []
    """
    If the user was to guess higher then this funciton is called to form the logic necessary
    to send to the Director class
    """
    def guessed_higher(self):
        if self.random_card < self.dealt_card:
            self.was_guess_correct = True

        else:
            self.was_guess_correct = False

    """
    Same function as guessed_higher method
    """
    def guessed_lower(self):
        if self.random_card < self.dealt_card:
            self.was_guess_correct = True

        else:
            self.was_guess_correct = False

    """
    This method is invoked at the start of the game to reset the random card
    and the dealt card to new random numbers
    """
    def deal_card(self):
        self.random_card = random.randint(1,13)
        print("\nThe Card is: ", self.random_card)
        self.dealt_card = random.randint(1,13)

    """
    Will retrieve user input and use basic logic to problem solve and call on the
    guessed_lower/higher methods
    """
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


