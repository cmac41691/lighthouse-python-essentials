# Chapter 2: Strings

## Introduction to Strings
- Strings are text data, enclosed in quotes (`" "` or `' '`).
- Can be combined using `+` (concatenation).
- Can be repeated using `*`.

Example:
```python
first_name = "Ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name
print(full_name)  
# Output: Ada Lovelace

echo = "Python! " * 3
print(echo)  
# Output: Python! Python! Python!

long_text = """This is a multi-line string.
It can span across several lines.
Great for paragraphs or formatted text."""

print(long_text)
# Output:
# This is a multi-line string.
# It can span across several lines.
# Great for paragraphs or formatted text.

## String Operations

message = "Python is fun!"
print(message[0])     # Output: P
print(message[-1])    # Output: !
print(message[:6])    # Output: Python
print(message[7:])    # Output: is fun!


## Length & Case
print(len(message))        # Output: 13
print(message.upper())     # Output: PYTHON IS FUN!
print(message.lower())     # Output: python is fun!
print(message.title())     # Output: Python Is Fun!

## Checking Content
print(message.startswith("Py"))   # Output: True
print(message.endswith("fun!"))   # Output: True

## Key Takeaways
- Strings are sequences → they can be indexed and sliced like lists.
- Useful built-in methods include .replace(), .upper(), .lower(), .startswith(), .endswith().
- Multi-line strings make it easier to handle paragraphs of text.
- Testing small snippets in the terminal helps build intuition.