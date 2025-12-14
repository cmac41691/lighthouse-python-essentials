from storage import load_or_create_score, save_score, reset_score
from mad_libs import start_mad_libs
from hangman import start_hangman
from trivia import start_trivia
from navigator import navigator_menu


def pause():
    """
    Pause program flow until the user presses Enter.

    Used to create a clean transition between game sessions
    before returning to the main navigator menu.
    """
    input("\n[Press Enter to return to the menu]")



def play_games():
    """
    Main loop for the Word Game Hub.

    Responsibilities:
        - Load or initialize persistent score data.
        - Display and route user selections through the navigator menu.
        - Execute the selected game (Mad Libs, Hangman, Trivia).
        - Update and save score statistics after each session.
        - Handle user requests to reset all stats.
        - Cleanly exit on user request or keyboard interrupt.

    This function represents the central controller of the app,
    coordinating user flow, persistent storage, and modular game files.
    """

    print("=== Welcome to Word Games Prototype ===")

    score_data = load_or_create_score()
    print(f"📊 Current Stats -> Total Sessions: {score_data['total_sessions']}")

    while True:
        game_choice = navigator_menu()

        # === Game Options ===
        if game_choice == "mad_libs":
            print("🎭 Starting Mad Libs...")
            start_mad_libs()
            score_data["mad_libs"] += 1

        elif game_choice == "hangman":
            print("🪓 Starting Hangman...")
            start_hangman()
            score_data["hangman"] += 1

        elif game_choice == "trivia":
            print("🧠 Starting Trivia...")
            start_trivia()
            score_data["trivia"] += 1

        elif game_choice == "reset":
            confirm = input("Are you sure you want to reset all stats? (y/n): ").strip().lower()
            if confirm == "y":
                score_data = reset_score()
                print("✅ Stats reset successfully!")
            else:
                print("❌ Reset cancelled.")
            continue

        elif game_choice == "exit":
            print("👋 Goodbye! Thanks for playing.")
            break

        # === Save progress ===
        score_data["total_sessions"] += 1
        save_score(score_data)

        pause()

    # Final save on exit
    save_score(score_data)


if __name__ == "__main__":
    try:
        play_games()
    except KeyboardInterrupt:
        print("\nSession ended by user. Saving progress...")
