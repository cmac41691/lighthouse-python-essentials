# Exercise: Tax Calculator
# -------------------------
# Goal: Ask the user for an amount, apply tax, and show the final total.

# 1. Ask the user for the original amount (use input()).
#    👉 Google: "python input convert to float"

# 2. Decide on a tax rate (e.g., 13% or 0.13).
#    👉 Google: "python percentage calculation"

# 3. Calculate the tax amount and add it to the original.
#    👉 Google: "python arithmetic operators + - * /"

# 4. Print out the result in a clear way.
#    👉 Google: "python f-string format number"

# Example (don’t copy, just for reference in your head):
# If the user enters 100 and tax is 13%, result should be 113.0

# Write your code below:
# Step 1: Ask the user for the original amount
try:
    user_amount = float(input("Please enter the amount: "))
    print(f"You put in: {user_amount}")
    print(f"The exact amount is: {user_amount}")
except ValueError:
    print("Incorrect input. Enter a valid number.")

# Step 2: Decide on a tax rate
user_amount = float(input("Enter an amount: "))

tax_amount = user_amount * 0.13
tax_amount_total = user_amount + tax_amount

print(f"The tax for {user_amount} is {tax_amount}")
print(f"The total with tax is {tax_amount_total}")