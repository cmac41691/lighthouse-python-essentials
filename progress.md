# 📈 Python Essentials Progress Log

This file documents my progress through the **Programming Essentials with Python** course by Lighthouse Labs. Each section includes what I learned, notes, and reflection on what I found most useful.

---

### 2025-11-16 — Started Lesson 5 (Loops & Repetition)

**Setup**
- Created new directory: `chapter5/`
- Added files for each section (intro_to_looping.py, making_new_data.py, iterating_over_range.py, exercise_actors.py, strings_as_lists.py)
- Beginning Looping & Iterating chapter — same workflow: pseudocode → Python → test → commit.


---

## 📆 Everyday Python
> (Mark each one complete when done ✅)

- [✅] Lesson 1: Your First Lines of Python  
- [✅] Lesson 2: Working with Variables  
- [✅] Lesson 3: Strings and Input  
- [✅] Lesson 4: Decisions and Conditions  
- [ ] Lesson 5: Loops and Repetition  
- [ ] Lesson 6: Functions and Reuse  
- [ ] Final Project: Word Game

---
---

### 🧩 2025-11-16 — Phase 4: Persistent Storage System Complete  

**Highlights**  
- Added a dedicated `storage.py` module for **saving and loading score data** using JSON.  
- Implemented new functions:  
  - `load_or_create_score()` → Automatically creates `score_data.json` if none exists.  
  - `save_score()` → Updates player progress after each session.  
- Integrated persistent tracking into `word_game.py` with per-game stats (Mad Libs / Hangman / Trivia / Total Sessions).  
- Updated `.gitignore` to exclude runtime files (`score_data.json`) and IDE/system files.  
- Refactored and cleaned menu logic, ensuring data saves safely between runs.  
- Verified JSON durability under multiple test loops — no corruption or overwrite errors detected.  

**Reflection**  
> This phase marked my **first true step into stateful Python programming** — adding persistence and modular design.  
> The Word Game Hub now stores player progress just like a production app.  
> It’s a big confidence boost seeing data persist beyond runtime and integrating cleanly across modules.  

**Next Goals (Phase 5 – Prototyping)**  
- Add simple text-based stats dashboard (display cumulative results).  
- Improve menu visuals (ASCII art / colors).  
- Add difficulty or “best of X rounds” mode for trivia.  
- Begin design of save-slot prototype (for future user profiles).  

---

💭 *Each phase builds my confidence — from pseudocode, to loops, to full-scale modular design.  
This milestone shows I can handle persistent data like a backend developer in training.*

---


Optional polish: color output or difficulty selector (easy/medium/hard) 


---

💭 I think in pseudocode, build with intent, and refine through practice.  
AI helps me reason faster, not skip the work.  
Each project documents real self-taught progress.

