# 📈 Python Essentials Progress Log

This file documents my progress through the **Programming Essentials with Python** course by Lighthouse Labs. Each section includes what I learned, notes, and reflection on what I found most useful.

---

## 🗓 Session 0: Course Enrollment & Setup
- Signed up for **Programming Essentials with Python** (Lighthouse Labs)
- Reviewed syllabus and lesson structure
- Prepared `progress.md` for tracking
- Ready to begin Lesson 1 on next study day


---

## 📆 Everyday Python
> (Mark each one complete when done ✅)

- [✅] Lesson 1: Your First Lines of Python  
- [✅] Lesson 2: Working with Variables  
- [✅] Lesson 3: Strings and Input  
- [ ] Lesson 4: Decisions and Conditions  
- [ ] Lesson 5: Loops and Repetition  
- [ ] Lesson 6: Functions and Reuse  
- [ ] Final Project: Word Game

---

---

### ✅ 2025-11-15 — Phase 4: Persistent Save System (Integrated with Word Game)

**Highlights**
- Added **`storage.py`** as a standalone persistence module for saving and loading player data.  
- Implemented two key functions:
  - `load_or_create_score()` → initializes or loads `score_data.json`.  
  - `save_score()` → writes updates back to disk after each session.  
- Integrated persistence into `word_game.py`:
  - Displays total sessions at program start.
  - Updates counts for **Mad Libs**, **Hangman**, and **Trivia** each time a game is played.
  - Saves all changes seamlessly between runs.
- Confirmed import and function calls work cleanly — no runtime errors or circular imports.
- Prepared printout templates for **final scoreboard display** after each session.

**Reflection**
> This update marks my first full implementation of a persistent data layer.  
> I now understand how to handle **file I/O**, **JSON serialization**, and **state management** between sessions — key backend fundamentals.  
> Seeing the game remember player progress made everything feel *real* — like I built an actual app.

**Next Goals (Phase 5 – Planned)**
- Add visual scoreboard formatting (📊 emojis and clean alignment).  
- Implement error handling for missing or corrupted JSON data.  
- Experiment with loading trivia questions from external JSON packs.  
- Optional: extend save system for multi-player profiles.

**Key Takeaways**
- Learned how to separate logic into **modular files** (`storage.py`, `word_game.py`, etc.).  
- Applied **open/read/write** patterns using context managers.  
- Strengthened understanding of **JSON** and structured data manipulation.  
- Reached the point where the project behaves like a real, persistent application.

Optional polish: color output or difficulty selector (easy/medium/hard) 


---

💭 I think in pseudocode, build with intent, and refine through practice.  
AI helps me reason faster, not skip the work.  
Each project documents real self-taught progress.

