from milestone_4 import *

word_list = ["apple", "pear", "banana", "raspberry", "orange"]

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        print(game.word_guessed)
        if game.num_lives == 0:
            print("You lose!")
            exit()
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You win!")
            exit()

play_game(word_list)