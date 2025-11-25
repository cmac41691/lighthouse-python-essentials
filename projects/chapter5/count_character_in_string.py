text = input(" Please enter in a word or sentence:")

character = input("Enter in a single character to search:")

count = 0

for c in text:
    if c == character:
        count += 1

print(f"The Character '{character}' appears {count} times")
