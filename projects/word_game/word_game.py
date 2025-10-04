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


# Step 1: Choose a secret word
# 👉 Google: "python random choice from list"
# Example: words = ["python", "lighthouse", "code"]

# Step 2: Set up variables to track the game state
# 👉 Google: "python underscores for word guessing"
# - Create a list of underscores for each letter in the word
# - Keep track of letters guessed
# - Set max attempts

# Step 3: Ask the user to guess a letter
# 👉 Google: "python check if character in string"
# - Use input() for the guess
# - Validate that it’s a single letter

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







