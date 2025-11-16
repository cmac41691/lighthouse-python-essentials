# Project: Word Game
# ------------------
# Goal: Build a simple word guessing game (like Hangman but simplified).
# The program should choose a secret word, then let the user guess letters
# until they either guess the whole word or run out of attempts.



from storage import load_or_create_score, save_score
from mad_libs import start_mad_libs
from hangman import start_hangman
from trivia import start_trivia


def play_games():
    """Main loop for Word Game hub."""
    print("=== Welcome to Word Games ===")

    # ✅ Load or create persistent score data
    score_data = load_or_create_score()
    print(f"📊 Current Stats -> Total Sessions: {score_data['total_sessions']}")

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
            print(f"⚠️ {error}")
            continue

        # ✅ Game choices
        if player_choice == "1":
            print("🎭 Starting Mad Libs...")
            start_mad_libs()
            score_data["mad_libs"] += 1

        elif player_choice == "2":
            print("🔠 Starting Hangman...")
            start_hangman()
            score_data["hangman"] += 1

        elif player_choice == "3":
            print("🧠 Starting Trivia...")
            start_trivia()
            score_data["trivia"] += 1

        elif player_choice == "4":
            print("👋 Goodbye! Thanks for playing.")
            break

        # ✅ Replay logic
        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")

            # ✅ Update persistent data before exiting
            score_data["total_sessions"] += 1
            save_score(score_data)

            print("\n=== Final Session Score ===")
            print(
                f"Mad Libs: {score_data['mad_libs']} | "
                f"Hangman: {score_data['hangman']} | "
                f"Trivia: {score_data['trivia']} | "
                f"Total Sessions: {score_data['total_sessions']}"
            )
            break


if __name__ == "__main__":
    play_games()





