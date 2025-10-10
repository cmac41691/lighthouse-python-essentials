# Project: Hangman (simplified)
# ------------------
# Goal: Build a word guessing game where the user guesses letters 
# until they win or run out of attempts.

# Step 1: Choose a secret word
# 👉 Google: "python random choice from list"
# Example: words = ["python", "lighthouse", "code"]

# Step 2: Initialize game state
# 👉 Google: "python underscores for word guessing"
# - Create underscores for each letter
# - Track guesses
# - Set max attempts (e.g., 6)

# Step 3: Ask user for a guess
# 👉 Google: "python input single character"
# 👉 Google: "python validate input length"
# - Make sure it’s a single letter

# Step 4: Check guess
# 👉 Google: "python if char in string"
# - If correct, replace underscore
# - If wrong, subtract attempt

# Step 5: Print current state
# 👉 Google: "python join list into string"
# - Show progress (_ a _ _)
# - Show remaining attempts

# Step 6: End game conditions
# 👉 Google: "python while loop break conditions"
# - Win if all letters guessed
# - Lose if attempts run out
# --- Step 1: choose a secret word ---
import random

secret_words = ["python", "lighthouse", "adventure", "journey", "code"]
secret_word = random.choice(secret_words)

# --- Step 2: initialize game state ---
hidden = ["_"] * len(secret_word)   # underscores per letter
attempts_left = 6                    # classic hangman tries
guessed = set()                      # what the player has tried

# (optional while debugging)
# print(secret_word)
# print(" ".join(hidden))

# ---  Step 3: Ask user for a guess ---
while attempts_left > 0 and "_" in hidden:
    ask_user = input("Please put in a letter:").lower().strip()
    if ask_user in secret_word:
        secret_word += 1
        print("Nice job on the right letter")
    if guessed not in secret_word:
        attempts_left -= 6
        print("Oops, wrong guess try again!")
print("Try another letter" + secret_word)

