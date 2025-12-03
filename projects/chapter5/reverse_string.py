# Reverse String — Lighthouse Labs Challenge

text = input("Enter in a word or sentence: ")

reversed_text = ""

for i in range(len(text) - 1, -1, -1):       
    reversed_text += text[i]

print(f"Here's the text but reversed: {reversed_text}")
