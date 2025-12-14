# storage.py
import json
import os

SAVE_FILE = "projects/word_game/score_data.json"

def load_or_create_score():
    """
    Load existing score data from 'score_data.json'.

    Returns:
        dict: A dictionary containing counters for:
            - mad_libs
            - hangman
            - trivia
            - total_sessions

    If the file does not exist, a new structure is created and saved.
    This ensures the app always has a valid score dataset.
    """

    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    else:
        data = {"mad_libs": 0, "hangman": 0, "trivia": 0, "total_sessions": 0}
        save_score(data)
        return data

def save_score(score_data):
    """
    Save the current score dictionary to 'score_data.json'.

    Args:
        score_data (dict): Updated statistics to persist.

    Ensures the user’s progress is retained across sessions.
    """

    with open(SAVE_FILE, "w") as f:
        json.dump(score_data, f, indent=4)

def reset_score():
    """
    Reset all game statistics back to zero.

    Returns:
        dict: A fresh score structure with all counters set to 0.

    Also writes the reset structure to the persistent JSON file.
    """

    data = {"mad_libs": 0, "hangman": 0, "trivia": 0, "total_sessions": 0}
    save_score(data)
    return data
