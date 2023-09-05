import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"]*len(self.word_list)
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    def check_guess(self, guess):     
        
        guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word!")

            self.word_guessed = [guess if letter == guess 
                                 else self.word_guessed[self.word.index(letter)]
                                 for letter in self.word]
            self.num_letters = self.word_guessed.count("_")
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            

    def ask_for_input(self):

            guess = input("Please enter a single letter: ")

            if len(guess) != 1 or guess.isalpha() == False:
                print("Not valid input. Please try again.")
            
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

            
            
        
            