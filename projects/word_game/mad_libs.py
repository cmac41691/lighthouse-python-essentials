# Project: Mad Libs
# ------------------
# Goal: Build a simple Mad Libs generator that asks the user for words 
# and fills them into a story template.

# Step 1: Create a story template with blanks
# 👉 Google: "python f-string user input"
# Example: "Just as I arrived at {place}, I realized I had forgotten my {object}."

# Step 2: Ask the user for inputs
# 👉 Google: "python input string"
# - Ask for a place
# - Ask for an object
# - (add more as you like)

# Step 3: Insert user inputs into the story
# 👉 Google: "python f-string format variables"
# - Replace placeholders with user input

# Step 4: Print the completed story
# 👉 Google: "python print formatted string"
# Step 1 & 2: Collect user inputs
player_character = input("Enter in your character's name: ")
starting_item_one = input("Enter in your starting item: ")
starting_item_two = input("Enter in your secondary item: ")
starting_zone = input("Enter where your adventure begins: ")

# Step 3: Insert inputs into story using f-string
hero_journey = f"""
As you awake from resting, {player_character}, you begin your quest in {starting_zone}.
Armed with your {starting_item_one} and {starting_item_two},
a world of exploration awaits you!
"""

# Step 4: Print the completed story
print(hero_journey)
