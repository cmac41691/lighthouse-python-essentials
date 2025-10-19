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
while True:
    print("\n-- Welcome to Word Game! --")
    print("Would you like to play either Mad Libs or Hangman?")
    print("(1) Mad Libs")
    print("(2) Hangman")
    print("(3) Exit")

    try:
        options = int(input("Please pick from the options: "))

        if options == 1:
            print("Starting Mad Libs...")
        elif options == 2:
            print("Starting Hangman...")
        elif options == 3:
            print("Goodbye! Exiting game.")
            break
        else:
            print("That's not a valid option, please pick again.")

    except ValueError:
        print("Wrong input — please enter a number, not text.")


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







