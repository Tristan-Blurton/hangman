
import random 

word_list = ["apple", "banana", "pear", "plum", "raspberry"]

def choose_random_word(word_list: list):
    """Choose a word from a list passed to the function."""

    word = random.choice(word_list)
    return word

def ask_for_input():
    """Ask for and record a letter passed by the user."""
    
    while True:
        guess = input("Please enter a single letter: ")

        if len(guess) == 1 and guess.isalpha() == True:
            return guess
            exit()
        else:
            print("Not valid input. Please try again.")

def check_guess(guess,word):
    """Check if the guessed letter is in the chosen word."""
    
    guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word!")
        return None
    else: 
        print(f"Sorry, {guess} is not in the word. Try again.")
        return None
