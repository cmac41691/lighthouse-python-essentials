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

from storage import load_or_create_score, save_score

from mad_libs import start_mad_libs
from hangman import start_hangman
from trivia import start_trivia

def play_games():
    """Main loop for Word Game hub."""
    score = 0
    print("=== Welcome to Word Games ===")

score_data = load_or_create_score()  
print(f"Current Stats -> Total Session: {score_data}['total_sessions']")

while True:
        try:
            print("\nMenu options:")
            print("1. Play Mad Libs")
            print("2. Play Hangman")
            print("3. Play Trivia")
            print("4. Exit")

            player_choice = input("Choose 1, 2, 3, or 4: ").strip()

            if player_choice not in ("1", "2", "3", "4"):
                raise ValueError("Invalid option, please try again.")

        except ValueError as error:
            print(f" {error}")
            continue
    # load_or_create_score()
    # print("Current Stats -> Total Sessions: X")   
     
        if player_choice == "1":
            print("Starting Mad Libs...")
            start_mad_libs()
            score += 1
            print(f" Session Score: {score}")  

        elif player_choice == "2":
            print(" Starting Hangman...")
            start_hangman()
            score += 1
            print(f" Session Score: {score}")

        elif player_choice == "3":
            print("Starting Trivia..") 
            start_trivia()
            score += 1
            print(f"Session Score: {score}")

        elif player_choice == "4":
            print(" Goodbye! Thanks for playing.")
            break

        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")
            break

# score_data["total_sessions"] += 1
# save_score(score_data)
# #print("Final Session Score:")
#print("Mad Libs: X | Hangman: Y | Trivia: Z | Total Session: N")        

print(f"\nFinal Session Score: {score}")

if __name__ == "__main__":
    play_games()





