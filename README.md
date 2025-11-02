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

- 2025-11-02 — Phase 1 (Stability Update)
- Added error handling for invalid menu input
- Introduced session scoring system
- Integrated replay loop for smoother UX
- Verified game hub runs without breaking logic

🌱 Phase 2 Goals (Next Steps)

- Add a third mini-game (e.g., Word Guess or Trivia).

- Implement persistent scoring with file storage (save/load progress).
- Add main menu ASCII art or styled UI for flair.
- Refactor constants (menu text, messages) into reusable variables.
- Begin unit testing for modular validation.