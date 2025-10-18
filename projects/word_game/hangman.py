# Project: Hangman (simplified)
# ------------------
# Goal: Build a word guessing game where the user guesses letters
# until they win or run out of attempts.

import random

# --- Step 1: choose a secret word ---
secret_words = ["python", "lighthouse", "adventure", "journey", "code"]
secret_word = random.choice(secret_words)

# --- Step 2: initialize game state ---
hidden = ["_"] * len(secret_word)   # underscores per letter
attempts_left = 6                    # classic hangman tries
guessed = set()                      # letters the player has tried

# --- Step 3+4: main game loop (show state + handle a guess each turn) ---
while attempts_left > 0 and "_" in hidden:
    # Show current state
    print("\n--- Current State ---")
    print("Word so far:", " ".join(hidden))
    print(f"Attempts left: {attempts_left}")
    print("Tried:", ", ".join(sorted(guessed)) if guessed else "-")

    # Ask user for a letter
    ask_user = input("Please put in a letter: ").lower().strip()

    # Validate input
    if len(ask_user) != 1 or not ask_user.isalpha():
        print("Please enter a single letter (a–z).")
        continue

    # Repeated guess? don't penalize
    if ask_user in guessed:
        print(f"You already tried '{ask_user}'.")
        continue

    # Apply guess
    if ask_user in secret_word:
        for i, ch in enumerate(secret_word):
            if ch == ask_user:
                hidden[i] = ask_user
        print("Nice job on the right letter!")
    else:
        attempts_left -= 1
        print("Oops, wrong guess — keep trying!")

    # Record this new guess
    guessed.add(ask_user)

# --- End of game ---
print("\nFinal word:", " ".join(hidden))
if "_" not in hidden:
    print(f"You got it! The word was: {secret_word}")
else:
    print(f"I'm sorry, you ran out of attempts. The word was: {secret_word}")
