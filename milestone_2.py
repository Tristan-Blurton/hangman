
import random 

word_list = ["apple", "banana", "pear", "plum", "raspberry"]

def choose_random_word(word_list: list):
    """Choose a word from a list passed to the function."""

    word = random.choice(word_list)
    print(word)

def guess():
    """Ask for and record a letter passed by the user."""

    guess = input("Please enter a single letter: ")

    if len(guess) == 1 and guess.isalpha() == True:
        print("Good guess!")

    else:
        print("Not valid input. Please try again.")
guess()
