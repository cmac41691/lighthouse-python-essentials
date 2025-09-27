# Tax Calculator Program

try:
    # Ask the user for the original amount
    user_amount = float(input("Please enter the amount: "))
    print(f"You put in: {user_amount}")
    print(f"The exact amount is: {user_amount}")
except ValueError:
    print("Incorrect input. Enter a valid number.")
    exit()  # exit program if invalid input

# Calculate tax at 13%
tax_amount = user_amount * 0.13

# Calculate total including tax
tax_amount_total = user_amount + tax_amount

# Output results (rounded to 2 decimal places)
print(f"The tax for {user_amount:.2f} is {tax_amount:.2f}")
print(f"The total with tax is {tax_amount_total:.2f}")
