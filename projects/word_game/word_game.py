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
# --------------------------------
# 1. Display title "Welcome to Word Game!"
# 2. Ask the user to choose a mode:
#       (1) Play Mad Libs
#       (2) Play Hangman
#       (3) Exit
# 3. Store the user's choice as a variable

# Step 2: Based on user's choice, run the selected game
# --------------------------------
# IF choice is 1 -> import mad_libs and run mad_libs.play()
# IF choice is 2 -> import hangman and run hangman.play()
# IF choice is 3 -> exit program
# ELSE -> display "Invalid choice, please try again"

# Step 3: Optional - wrap logic in a loop so user can replay
# --------------------------------
# Keep showing the menu until user chooses Exit


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







