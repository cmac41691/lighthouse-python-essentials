# Exercise: Bill Splitter
# ------------------------
# Goal: Ask the user for a total bill and the number of people,
# then calculate how much each person should pay.

# Step 1: Ask the user for the total bill.
# 👉 Google: "python input float conversion"

# Step 2: Ask how many people are splitting the bill.
# 👉 Google: "python input convert to int"

# Step 3: Divide the total bill by the number of people.
# 👉 Google: "python division operator / in python"

# Step 4: Print the result in a clear way.
# 👉 Google: "python f-string format 2 decimal places"

# Example (don’t copy, just for reference in your head):
# If bill = 100 and 4 people, each should pay 25.00

# Write your code below:
# Step 1: Ask the user for the total bill
users_bill = input("Enter the bill total: ")
try:
    total_bill = float(users_bill)
    print("Entered number as float:", total_bill)
except ValueError:
    print("Invalid input. Please enter a valid bill amount.")

# Step 2: Ask how many people are splitting the bill
total_people = input("Enter the number of people: ")
try:
    people_split = int(total_people)
    print("Entered number of people:", people_split)
except ValueError:
    print("Invalid input. Please enter a whole number.")

#Step 3: Divide the total bill by the number of people.
amount_per_person = total_bill/people_split
print(amount_per_person)

tip_amount = total_bill * 0.13
print(tip_amount)
