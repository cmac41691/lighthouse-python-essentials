# Chapter 2 - Exercise: String Replacement

journey = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""

# Fixing the bad lyrics using replace
fixed = journey.replace("tone", "town")
fixed = fixed.replace("whirl", "world")
fixed = fixed.replace("tray", "train")
fixed = fixed.replace("seedy", "city")
fixed = fixed.replace("Bored", "Born")

print("Original Lyrics:\n")
print(journey)

print("\nFixed Lyrics:\n")
print(fixed)
