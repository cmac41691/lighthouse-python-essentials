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


# --- Step 4: show state + handle a guess each turn ---
while attempts_left > 0 and "_" in hidden:
    # Display current game state
    print("\n--- Current State ---")
    print("Word so far: " + " ".join(hidden))
    print(f"Attempts left: {attempts_left}")

    # Ask user for a letter
    ask_user = input("Please put in a letter: ").lower().strip()

    # Basic validation (optional but helpful)
    if len(ask_user) != 1 or not ask_user.isalpha():
        print("Please enter a single letter (a–z).")
        continue

    # Right vs wrong guess
    if ask_user in secret_word:
        print("Nice job on the right letter!")
        # Reveal all matching positions in `hidden`
        for i, ch in enumerate(secret_word):
            if ch == ask_user:
                hidden[i] = ask_user
    else:
        attempts_left -= 1
        print("Oops, wrong guess — keep trying!")

# Game loop ends
if "_" not in hidden:
    print(f"\nYou got it! The word was: {secret_word}")
else:
    print(f"\nI'm sorry, you ran out of attempts. The word was: {secret_word}")

