# 🐍 Lighthouse Python Essentials — Learning Journey & Projects
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Student-Lighthouse%20Labs-orange">
  <img src="https://img.shields.io/badge/Status-In%20Progress-success">
</p>

Welcome to my repository documenting my progress through **Programming Essentials with Python** by Lighthouse Labs.  
This repo contains my daily exercises, pseudocode practice, and multi-file projects — all structured the way I think and work as a self-taught backend developer.
---

## 📚 About the Course
This free, hands-on course builds Python fundamentals from the ground up.  
My workflow throughout the course:

> **Pseudocode → Python → Test → Refine → Commit**

This approach strengthens my ability to write clean, modular code with intention — not guesswork.
---

## 🧠 What I've Learned
- Variables, expressions, and data types  
- Strings and user input  
- Conditional logic & branching  
- Looping patterns (for/while)  
- Functions, parameters, return values  
- Modular programming  
- Error handling & defensive input validation  
- JSON persistence and basic state management  
- Writing maintainable, multi-file Python programs
---

## 🗂 Repository Structure
```plaintext
lighthouse-python-essentials/
│
├── chapter5/                  # Looping, iteration, small challenges
├── chapter6/                  # Functions, modularization
│
└── projects/
    └── word_game/             # Final multi-file project
        ├── mad_libs.py
        ├── hangman.py
        ├── trivia.py
        ├── navigator.py       # Modular game selection menu
        ├── storage.py         # JSON persistence + reset system
        ├── word_game.py       # Main hub controller
        └── score_data.json    # Auto-generated save file

---

# ✅ **SECTION 5 — Featured Project (Word Game Hub)**

```markdown
---

# 🎮 **Featured Project — Word Game Hub**

The Word Game Hub is the capstone project for this course, expanded far beyond its original scope into a **fully modular, scalable Python application**.
### 🔧 Core Features
- **Navigator menu** from a dedicated module (`navigator.py`)
- **Pause system** for clean UX between rounds
- **Three games**: Mad Libs, Hangman, Trivia  
- **Persistent JSON save file** tracks:
  - Mad Libs plays  
  - Hangman plays  
  - Trivia plays  
  - Total sessions  
- **Reset feature** with confirmation  
- **Error handling** to prevent invalid input crashes  
- **Graceful shutdown** with `KeyboardInterrupt` support  
---

### 💾 Persistence System
Implemented using `storage.py`:
- `load_or_create_score()`  
- `save_score()`  
- `reset_score()`  

This is my first step into **stateful backend-style programming**.
---

### ▶️ How to Run
```bash
cd projects/word_game
python word_game.py

---



---

## 🧾 Update Log (Phases 1–6)

### **Phase 2 — Trivia Game Added**
- Created `trivia.py`
- Integrated into menu & scoring system

### **Phase 4 — JSON Save System**
- Introduced persistent score tracking  
- Added session scoreboard  
- Stress-tested repeated writes

### **Phase 5 — Reset System**
- Added `reset_score()`  
- Safe confirmation prompt  
- Improved file generation logic  

### **Phase 6 — Major Refactor (2025-12-14)**
feat(word_game): integrate navigator menu and pause system
feat(navigator): add modular game selection interface
refactor(storage): finalize score loading, saving, and reset logic

**Highlights**
- Fully modular navigator interface  
- Smooth UX with pause system  
- Cleaned main game loop  
- Storage system validated end-to-end  

**Result**  
> The Word Game Hub now behaves like a real application — modular, maintainable, and easy to extend.
---

# ✍️ Author
**Coady MacLellan**  
Self-taught developer • Backend-focused thinker • Lifelong learner  

This repo represents my disciplined workflow, commitment to clean coding habits, and steady growth toward becoming a professional backend developer.
