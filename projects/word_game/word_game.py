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
    print("Welcome to Word Games!")

    while True:
        # menu
        print("\nMenu options")
        print("(1) Play Mad Libs")
        print("(2) Play Hangman")
        print("(3) Exit")

        player_choice = input("Please pick a choice (1, 2, or 3): ").strip()

        if player_choice == "1":
            print("\nStarting Mad Libs...")
            start_mad_libs()
            print("Mad Libs complete!")

        elif player_choice == "2":
            print("\nStarting Hangman...")
            start_hangman()
            print("Hangman session complete!")

        elif player_choice == "3":
            print("Farewell! Exiting Word Games...")
            break

        else:
            print("That's not a valid choice — try again.")
            continue

        # replay prompt after user finishes a game
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if play_again != "y":
            print("Thanks for playing! See you next time for more Word Games!")
            break

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







