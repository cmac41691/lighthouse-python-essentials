# Lighthouse Python Essentials

Welcome to my solutions and notes from the **Programming Essentials with Python** course by [Lighthouse Labs](https://free-courses.lighthouselabs.ca/courses/programming-essentials-with-python).

## 📚 About the Course
This free, beginner-friendly course teaches Python fundamentals through interactive lessons and small, hands-on challenges.

## 🚀 What I Learned
- Variables, data types, and string manipulation  
- Conditional logic and loops  
- Functions and return values  
- Lists and basic data structures  
- Error handling and debugging  
- Building a mini-project from scratch  

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
**Coady MacLellan** — _aspiring developer & lifelong learner_

---
## 🎮 Projects — Word Game Hub (Phase 1)
This mini-project brings together multiple text-based games — **Mad Libs** and **Hangman** — into one Python-powered hub.  
It’s the capstone for the course’s “Functions” and “Error Handling” lessons.

### 🧩 Key Features
- **Error Handling:** Prevents crashes with `try/except ValueError`  
- **Session Scoring:** Tracks how many games you play per session  
- **Replay System:** Lets players continue or exit gracefully  
- **Modular Design:** Each game lives in its own Python file (`mad_libs.py`, `hangman.py`)  
- **Stable Runtime:** Tested for invalid inputs and stable control flow 

### ⚙️ How to Run
```bash
cd projects/word_game
python word_game.py

## 📁 Project Layout
projects/
└── word_game/
    ├── mad_libs.py        # Start function for Mad Libs
    ├── hangman.py         # Start function for Hangman
    ├── trivia.py          # Trivia mini-game (Phase 2)
    ├── storage.py         # Persistent save/load system
    ├── word_game.py       # Main game hub (menu, error handling, score)
    └── README.md


---

### 🧩 **Section 5 — Update Log (Phases 2–4)**
```markdown
## 🧾 Update Log

### 🕹 2025-11-08 — Phase 2 (Trivia Integration)
- Added `trivia.py` mini-game module  
- Linked into hub menu under option (3)  
- Verified stable gameplay and replay logic  

### 💾 Phase 4 — Persistent Score System
The Word Game Hub now includes a **JSON-based persistence layer** to save player stats between sessions.

#### 🧠 Features
- Automatically loads or creates `score_data.json` on startup  
- Tracks cumulative progress for  
  - `mad_libs`, `hangman`, `trivia`, `total_sessions`  
- Saves updated results after each session  
- Displays live scoreboard after every exit or replay cycle  

#### ⚙️ Technical Summary
| File | Purpose |
|------|----------|
| `storage.py` | Handles JSON read/write functions |
| `word_game.py` | Central hub that calls save/load logic |
| `score_data.json` | Stores persistent player data |

#### 🧩 Example Output
📊 Current Stats → Total Sessions: 3
🎭 Starting Mad Libs…
Game Over!
Your Score: 3/3

=== Final Session Score ===
Mad Libs: 4 | Hangman: 2 | Trivia: 3 | Total Sessions: 3

✅ Status: Phase 4 completed successfully — persistent storage verified under stress testing.

## 🧩 Phase 5 — Persistent Save + Reset Integration (2025-11-30)
### Summary
Phase 5 added a robust **reset-stats feature** and improved JSON save persistence, letting players wipe their progress safely without breaking gameplay.

### Highlights
- New menu option **“Reset Stats (Option 4)”**  
- Added `reset_score()` helper in `storage.py`  
- Confirmation prompt to prevent accidental wipes  
- Auto-save updates after reset or session end  
- Updated `.gitignore` to exclude `score_data.json`  
- JSON save file verified under stress conditions  

### Example
Would you like to reset your stats? (y/n): y
✅ Stats have been reset successfully!

✅ Phase 5 complete — system is now fully persistent and player-friendly.


## 🌱 Next Phase (Phase 6 Preview)
**Focus:** UI/UX polish and error-handling refinement  
**Goals:**  
- Improve print formatting and colorized output  
- Add return-to-menu option after each game  
- Replace generic exceptions with specific handlers  
- Optional ASCII banner for Word Game Hub title  

---

## 📌 Notes
This repo will continue to evolve as I complete future phases and transition toward the Meta Backend Developer certification.  
Stay tuned for Phase 6 — UI Refactor and Testing phase!

---
 

