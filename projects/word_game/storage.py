# storage.py
import json
import os

def load_or_create_score():
    """Load score data if it exists, otherwise create a new one."""
    if os.path.exists("score_data.json"):
        with open("score_data.json", "r") as json_file:
            score_data = json.load(json_file)
            print("Loaded existing score data:", score_data)
            return score_data
    else:
        score_data = {
            "mad_libs": 0,
            "hangman": 0,
            "trivia": 0,
            "total_sessions": 0
        }
        with open("score_data.json", "w") as json_file:
            json.dump(score_data, json_file, indent=4)
        print("Created new score file.")
        return score_data


def save_score(score_data):
    """Save updated score data to JSON file."""
    with open("score_data.json", "w") as json_file:
        json.dump(score_data, json_file, indent=4)
    print("Scores saved successfully!")
