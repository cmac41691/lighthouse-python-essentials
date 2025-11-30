from storage import load_or_create_score, save_score, reset_score
from mad_libs import start_mad_libs
from hangman import start_hangman
from trivia import start_trivia

def play_games():
    """Main loop for Word Game hub."""
    print("=== Welcome to Word Games Prototype ===")

    # Load or create persistent score data
    score_data = load_or_create_score()
    print(f"📊 Current Stats -> Total Sessions: {score_data['total_sessions']}")

    while True:
        try:
            print("\n==============================")
            print("Menu Options:")
            print("1. Play Mad Libs")
            print("2. Play Hangman")
            print("3. Play Trivia")
            print("4. Reset Stats")
            print("5. Exit")

            player_choice = input("Choose 1–5: ").strip()
            if player_choice not in ("1", "2", "3", "4", "5"):
                raise ValueError("Invalid option. Please choose 1–5.")

        except ValueError as error:
            print(f"⚠️ {error}")
            continue

        # === Game Options ===
        if player_choice == "1":
            print("🎭 Starting Mad Libs...")
            start_mad_libs()
            score_data["mad_libs"] += 1

        elif player_choice == "2":
            print("🪓 Starting Hangman...")
            start_hangman()
            score_data["hangman"] += 1

        elif player_choice == "3":
            print("🧠 Starting Trivia...")
            start_trivia()
            score_data["trivia"] += 1

        # === Reset Stats Option ===
        elif player_choice == "4":
            confirm = input("Are you sure you want to reset all stats? (y/n): ").lower().strip()
            if confirm == "y":
                score_data = reset_score()
                print("✅ Stats reset successfully!")
            else:
                print("❌ Reset cancelled.")
            continue

        # === Exit Option ===
        elif player_choice == "5":
            print("👋 Goodbye! Thanks for playing.")
            break

        # === Update persistent data after each round ===
        score_data["total_sessions"] += 1
        save_score(score_data)

        # === Replay logic ===
        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again != "y":
            print("\n=== Final Session Score ===")
            print(
                f"Mad Libs: {score_data['mad_libs']} | "
                f"Hangman: {score_data['hangman']} | "
                f"Trivia: {score_data['trivia']} | "
                f"Total Sessions: {score_data['total_sessions']}"
            )
            break

if __name__ == "__main__":
    try:
        play_games()
    except KeyboardInterrupt:
        print("\nSession ended by user. Saving progress...")





