# Lighthouse Python Essentials

Welcome to my solutions and notes from the **Programming Essentials with Python** course by [Lighthouse Labs](https://free-courses.lighthouselabs.ca/courses/programming-essentials-with-python).

## 📚 About the Course

This is a free, beginner-friendly course designed to teach the fundamentals of Python programming through interactive lessons and hands-on challenges.

## 🚀 What I Learned

- Variables, data types, and string manipulation  
- Conditional logic and loops  
- Functions and return values  
- Lists and basic data structures  
- Error handling and debugging  
- Working on a mini project  

## 🧠 Goals for This Repo

- Reinforce Python fundamentals  
- Practice clean and readable code  
- Track my progression as a self-taught developer  

## 📁 Structure
/lighthouse-python-essentials
├── lessons/ # Completed exercises and notes
├── projects/ # Final projects or challenges
├── README.md
└── .gitignore

## ✍️ Author

Coady MacLellan — _aspiring developer & lifelong learner_

---

## 📌 Notes

This repo will grow as I complete the course. Stay tuned for updates!

---

## 🎮 Projects — Word Game Hub (Phase 1)

This mini-project brings together multiple text-based games — **Mad Libs** and **Hangman** — into one Python-powered hub.  
It’s the capstone for the course’s “Functions” and “Error Handling” lessons.

### 🧩 Key Features
- **Error Handling:** Prevents crashes with `try/except ValueError` when invalid menu input is entered.  
- **Session Scoring:** Tracks how many games you play per session.  
- **Replay System:** Gives players the choice to continue or exit gracefully.  
- **Modular Design:** Each game lives in its own Python file (`mad_libs.py`, `hangman.py`), imported into `word_game.py`.  
- **Stable Runtime:** Tested for invalid inputs and stable control flow.  

---

### ⚙️ How to Run
```bash
cd projects/word_game
python word_game.py

📁 Project Layout
projects/
└── word_game/
    ├── mad_libs.py        # Start function for Mad Libs
    ├── hangman.py         # Start function for Hangman
    ├── word_game.py       # Main game hub (menu, error handling, score)
    └── README.md

🧾 Update Log

- 2025-11-08 — Phase 2 (Trivia Integration)
- Added trivia.py mini-game module.
- Linked into hub menu under option (3).
- Verified stable gameplay and replay logic.

🌱 Phase 3 Goals (Next Steps)

- Add persistent scoring system (save to JSON/text). 
- Expand question banks for Trivia dynamically.
- Introduce ASCII art menu.
- Implement unit testing for reliability checks.
---

## 💾 Persistent Score System (Phase 4)

The Word Game Hub now includes a **JSON-based persistence layer** to save player stats between sessions.

### 🧠 Features
- Automatically loads or creates `score_data.json` on startup.  
- Tracks cumulative progress for:
  - `mad_libs`
  - `hangman`
  - `trivia`
  - `total_sessions`
- Saves updated results after each session.  
- Displays a live scoreboard after every exit or replay cycle.

### ⚙️ Technical Summary
| File | Purpose |
|------|----------|
| `storage.py` | Handles JSON read/write functions |
| `word_game.py` | Central hub that calls save/load logic |
| `score_data.json` | Stores persistent player data |

### 🧩 Example Output
📊 Current Stats → Total Sessions: 3

🎭 Starting Mad Libs…
Game Over!
Your Score: 3/3

=== Final Session Score ===
Mad Libs: 4 | Hangman: 2 | Trivia: 3 | Total Sessions: 3


### ✅ Status
> Phase 4 completed successfully — persistent storage verified under stress testing.  
> Phase 5 will focus on UI/UX and leaderboard enhancements.
