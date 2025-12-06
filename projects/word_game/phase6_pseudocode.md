# 🧩 Phase 6 — Word Game Hub (UI/UX Refactor & Error Handling)

## 🎯 Goal
Refactor and polish the Word Game Hub for better visual flow, improved error handling, and a more structured user experience.  
This phase builds on Phase 5 and sets the foundation for future testing and polish.

---

## 🧠 Pseudocode Overview
```plaintext
START

DISPLAY "🎮 WORD GAME HUB ==="
DISPLAY "Welcome back, player!"
DISPLAY divider line "============================"

# --- Load Persistent Data ---
TRY
    LOAD score_data FROM "score_data.json"
    DISPLAY "Loaded saved stats successfully!"
EXCEPT FileNotFoundError
    CREATE score_data = {
        "mad_libs": 0,
        "hangman": 0,
        "trivia": 0,
        "total_sessions": 0
    }
    DISPLAY "No previous save found — new data file created."
END TRY

# --- Main Menu Loop ---
WHILE True:
    CLEAR screen or print newlines
    DISPLAY banner "=== MAIN MENU ==="
    DISPLAY "1. Play Mad Libs"
    DISPLAY "2. Play Hangman"
    DISPLAY "3. Play Trivia"
    DISPLAY "4. Reset Stats"
    DISPLAY "5. Exit"
    PRINT divider line

    PROMPT player_choice = input("Choose 1–5: ")

    # --- Handle Menu Options ---
    TRY
        IF player_choice == "1":
            DISPLAY "🎭 Starting Mad Libs..."
            CALL start_mad_libs()
            INCREMENT score_data["mad_libs"]

        ELIF player_choice == "2":
            DISPLAY "👻 Starting Hangman..."
            CALL start_hangman()
            INCREMENT score_data["hangman"]

        ELIF player_choice == "3":
            DISPLAY "🧠 Starting Trivia..."
            CALL start_trivia()
            INCREMENT score_data["trivia"]

        ELIF player_choice == "4":
            DISPLAY "⚙️ Reset all stats?"
            PROMPT confirm = input("(y/n): ").lower()
            IF confirm == "y":
                FOR each key IN score_data:
                    score_data[key] = 0
                SAVE score_data TO "score_data.json"
                DISPLAY "✅ Stats reset successfully!"
            ELSE:
                DISPLAY "Reset cancelled."

        ELIF player_choice == "5":
            DISPLAY "👋 Thanks for playing!"
            BREAK

        ELSE:
            RAISE ValueError("Invalid menu option")

    EXCEPT ValueError AS error:
        DISPLAY f"⚠️ Error: {error}"
        DISPLAY "Please enter a number between 1–5."

    FINALLY:
        INCREMENT score_data["total_sessions"]
        SAVE score_data TO "score_data.json"
        DISPLAY current totals for all games
        PROMPT "Press Enter to return to menu ..."

# --- End Program ---
DISPLAY "Session complete. Final totals saved!"
END

## Implementation Notes
- Maintain existing modular imports (storage.py, mad_libs.py, hangman.py, trivia.py).
- Use consistent indentation and clear menu spacing.
- Focus on readable prompts and graceful exits.
- Confirm score_data.json writes occur only after valid input or reset.
- Future: add color output or ASCII banner for polish.