text = input("Please enter a word or sentence:")
new_text = ""

vowels = "aeiouAEIOU"

for c in text:
    if c in vowels:   
        new_text += c

print(f"the new text: '{new_text}' ")
