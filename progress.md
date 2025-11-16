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
### ✅ 2025-11-16 — Phase 4: Persistent JSON Integration & Data Validation

**Highlights**
- Fully integrated `storage.py` into the Word Game hub for persistent session data.  
- Implemented JSON save/load system using `load_or_create_score()` and `save_score()` functions.  
- Verified long-term data consistency under stress tests — score tracking and replay cycles remained stable.  
- Added session summary output showing total games played across all runs.  
- Polished replay flow and ensured graceful termination logic (`break` handling fixed).  

**Reflection**
> Today marks the completion of the persistence system — the project now retains progress between sessions like a real-world app.  
> What began as a simple word-based prototype now functions as a modular, state-driven Python program with backend-style behavior.  
> Each phase built on solid pseudocode planning, documentation research, and practical testing — the foundation of professional software development.

**Next Goals (Phase 5 — Planned)**
- Add ASCII or color-coded scoreboard UI.  
- Introduce difficulty levels (Easy / Medium / Hard).  
- Prototype optional leaderboard system using local file ranking.  
- Conduct final code cleanup, docstrings, and internal QA pass.  

**Key Takeaways**
- Achieved a clean modular architecture across four files (`word_game.py`, `mad_libs.py`, `hangman.py`, `trivia.py`, `storage.py`).  
- Learned practical persistence via JSON — lightweight but production-relevant.  
- Strengthened understanding of loops, file handling, and data reliability under stress.  
- Reinforced “pseudocode → implementation → refinement” workflow discipline.

> 💡 *"Self-taught doesn’t mean alone — it means building your own map and refining it every step of the way."*

---


Optional polish: color output or difficulty selector (easy/medium/hard) 


---

💭 I think in pseudocode, build with intent, and refine through practice.  
AI helps me reason faster, not skip the work.  
Each project documents real self-taught progress.

