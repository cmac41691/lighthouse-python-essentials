# Strings Are Special Lists — Lighthouse Labs Exercise

text = input("Enter text: ")
character = input("Enter a single character to count: ")

count = 0

for c in text:
    if c == character:
        count += 1

print(f"'{character}' appears {count} times.")
