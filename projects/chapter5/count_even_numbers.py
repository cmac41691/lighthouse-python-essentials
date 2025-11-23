# attempt 2025-11-23   
number = input("Enter in a number that's positive:")

try:
    limit = int(number)
    count_even = 0

    for n in range(1, limit + 1):
        if n % 2 == 0:
            count_even += 1

    print(f"There are {count_even} even numbers between 1 and {limit}.")

except:
    print("That isn't a number, try again")
