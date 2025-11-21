# newer version - 2025-11-21      
number = input("Enter in a positive number: ")

try:
    limit = int(number)

    total = 0

    for n in range(1, limit + 1):
        total += n  # this keeps n in check

    print(f"The sum of all numbers up to {limit} is: {total}")

except:
    print("That's not a number, try again")
