# 📈 Python Essentials Progress Log

This file documents my progress through the **Programming Essentials with Python** course by Lighthouse Labs. Each section includes what I learned, notes, and reflection on what I found most useful.

---

### ✔ Completed Lesson 6 — Functions & Reuse
**Date:** 2025-12-??  

**Completed Exercises**  
- `introduction_to_functions.py` — simple_function  
- `defining_and_calling.py` — say_hello(), greet_user()  
- `parameters_and_return_values.py` — add_number(), calculate_area()  
- `exercise_functions.py` — celsius_to_fahrenheit(), is_even(), repeat_text()  

**Skills Learned**  
- Defining and calling functions  
- Using parameters  
- Returning values from functions  
- Writing modular, reusable code  
- Using pseudocode to structure logic  
- Understanding input, output, and flow  
- Using docstrings to improve readability  
- Testing individual functions  
- Strengthening backend fundamentals  

**Reflection**  
This chapter helped solidify my understanding of functions and how they structure programs.  
Pseudocode made each exercise easier to break down, and I can see my logic improving with every file.  
Completing Lesson 6 prepares me for the final Word Game work and the upcoming Interlude repo before starting Meta Backend.


### ✔ Completed Lesson 5 (Loops & Repetition)

**Completed Exercises**
- `intro_to_looping.py`
- `making_new_data.py`
- `iterating_over_range.py`
- `exercise_actors.py`
- `string_as_lists.py`

**Completed Challenges**
- countdown
- sum up to n
- count even numbers
- count character in string
- extract vowels
- reverse string

---


---

## 📆 Everyday Python
> (Mark each one complete when done ✅)

- [✅] Lesson 1: Your First Lines of Python  
- [✅] Lesson 2: Working with Variables  
- [✅] Lesson 3: Strings and Input  
- [✅] Lesson 4: Decisions and Conditions  
- [✅] Lesson 5: Loops and Repetition  
- [✅] Lesson 6: Functions and Reuse  
- [ ] Final Project: Word Game

---
---

### Phase 5: Persistent Save + Reset System

- Added support for a reset option in the main menu.
- Data persistence is handled through `storage.py` using JSON.
- Players can now clear all progress safely without breaking the game.

**Key Functions**
- `load_or_create_score()` → Loads existing or creates a new save file.
- `save_score()` → Saves current progress automatically after each session.
- `reset_score()` → Wipes the JSON file to default zero values on user confirmation.
 

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

Continuing workflow: pseudocode → Python → test → commit.