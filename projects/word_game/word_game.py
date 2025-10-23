# Project: Word Game
# ------------------
# Goal: Build a simple word guessing game (like Hangman but simplified).
# The program should choose a secret word, then let the user guess letters
# until they either guess the whole word or run out of attempts.

# Word Game (Final Project)
# ------------------
# This project combines Mad Libs and Hangman ideas.
# - User can pick a mode: play Mad Libs or Hangman
# - Program runs the selected game


# Step 1: Show game menu
# import two files for word game picks 
from mad_libs import start_mad_libs 
from hangman import start_hangman

# run a function with modules too     
def play_games():
    print("Welcome to Word Game!")

    while True:
        print("\nMenu options:")
        print("1) Play Mad Libs")
        print("2) Play Hangman")
        print("3) Exit")

        player_choice = input("Enter your choice (1 for Mad Libs, 2 for Hangman, 3 to Exit): ").strip()

        if player_choice == "1":
            print("You picked Mad Libs")
            start_mad_libs()
        elif player_choice == "2":
            print("You picked Hangman")
            start_hangman()
        elif player_choice == "3":
            print("Farewell")
            break
        else:
            print("That's not a choice — try again")

# run it
play_games()


# Step 4: Update the game state
# 👉 Google: "python replace list element by index"
# - If the letter is in the word, reveal it in the underscores
# - If not, subtract from attempts

# Step 5: Print the current state
# 👉 Google: "python join list into string"
# - Show the word with guessed letters + underscores
# - Show remaining attempts

# Step 6: End the game
# 👉 Google: "python while loop with break"
# - If all letters guessed, user wins
# - If attempts run out, game over

# Example interaction:
# Word: _ _ _ _ _ 
# Guess a letter: o
# Word: _ o _ _ o
# Attempts left: 4
# ... 







