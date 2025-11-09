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

### ✅ 2025-11-09 — Phase 3: Persistent Score System (JSON Integration)


## Highlights

Designed a JSON-based persistence layer to save and load player progress across sessions.
Wrote pseudocode prototypes for two helper functions:
load_or_create() — initializes or loads score_data.json.
save_score() — writes updated results back to disk.


Defined an extensible JSON schema:
{
  "mad_libs": 0,
  "hangman": 0,
  "trivia": 0,
  "total_sessions": 0
}
Verified understanding of the json and os modules through documentation research.

Planned integration into the main game hub (word_game.py) for next phase.

## Reflection
This was a big leap. I used official Python documentation to independently design a working persistence system.
It showed I can research, interpret, and apply technical references on my own — a key step toward backend-level thinking.

## Next Goals (Phase 4 – Planned)
- Connect load_or_create() and save_score() with the main Word Game Hub.
- Display cumulative results after each session.
- Implement error handling for missing or corrupted JSON data.
- Consider expanding the format for future leaderboard or database support.


## Key Takeaways

- Learned practical file handling using context managers (with open).
- Understood the flow of reading/writing structured data with json.dump / json.load.
- Practiced designing reusable, modular utility functions.
- Reinforced the ability to build solutions directly from official documentation.

Optional polish: color output or difficulty selector (easy/medium/hard) 


---

💭 I think in pseudocode, build with intent, and refine through practice.  
AI helps me reason faster, not skip the work.  
Each project documents real self-taught progress.

