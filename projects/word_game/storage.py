# storage.py
import json
import os

SAVE_FILE = "projects/word_game/score_data.json"

def load_or_create_score():
    """Load existing score data or create a new one."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    else:
        data = {"mad_libs": 0, "hangman": 0, "trivia": 0, "total_sessions": 0}
        save_score(data)
        return data

def save_score(data):
    """Save current score data to JSON."""
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def reset_score():
    """Reset all score values to zero and save."""
    data = {"mad_libs": 0, "hangman": 0, "trivia": 0, "total_sessions": 0}
    save_score(data)
    return data
