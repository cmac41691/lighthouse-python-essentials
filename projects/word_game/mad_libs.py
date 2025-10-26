# Project: Mad Libs
# ------------------
# Goal: Build a simple Mad Libs generator that asks the user for words 
# and fills them into a story template.


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
print("/n=== Hero's Tale Start ===/n")
print(hero_journey)
print("=== THE END ===")