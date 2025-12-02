# Making New Data — Lighthouse Labs Exercise

number = int(input("Enter a positive number: "))

total = 0

for n in range(1, number + 1):
    total += n

print(f"The sum of all numbers up to {number} is: {total}")
