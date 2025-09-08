# Chapter 2 - String Operations

message = "Python is fun!"

# Accessing characters
print("First character:", message[0])
print("Last character:", message[-1])

# Slicing
print("First 6 characters:", message[:6])
print("From index 7 to end:", message[7:])

# Length
print("Length of message:", len(message))

# Changing case
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title Case:", message.title())

# Checking content
print("Starts with 'Py'?", message.startswith("Py"))
print("Ends with 'fun!'?", message.endswith("fun!"))
