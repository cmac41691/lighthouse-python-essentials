
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

# Step 4: Print the result in a clear way.
print(f"\n--- Bill Summary ---")
print(f"Bill total: ${total_bill:.2f}")
print(f"Tip amount (13%): ${tip_amount:.2f}")
print(f"Total with tip: ${(total_bill + tip_amount):.2f}")
print(f"Each person owes: ${amount_per_person:.2f}")

