import random

class Hangman:

    def __init__(self, num_lives = 5):
        self.num_lives = num_lives
        
        self.word_list = ["apple", "banana", "pear", "plum", "raspberry"]
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"]*len(self.word_list)
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    def check_guess(self, guess):     
        
        guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word!")
            

    def ask_for_input(self):

        while True:
            guess = input("Please enter a single letter: ")

            if len(guess) != 1 or guess.isalpha() == False:
                print("Not valid input. Please try again.")
            
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


game1 = Hangman()
game1.ask_for_input()

            
            
        
            