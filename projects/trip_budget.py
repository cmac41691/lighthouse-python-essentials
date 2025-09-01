# Trip Budget Calculator (barebones prototype)

# Step 1: Collect user input
name = input("Enter your name: ")

flight_cost = float(input("Enter flight cost: "))
while flight_cost > 1000:
    print("Too expensive, try again.")
    flight_cost = float(input("Enter flight cost: "))
print("Flight accepted under $1000")

# Step 2: Hotels stored as list of dictionaries
inns = [
    {"hotel": "Delta",        "cost":  50},
    {"hotel": "Four Seasons", "cost": 250},
    {"hotel": "Fairmont",     "cost": 150},
]

hotel_pick  = None
hotel_price = None

# Budget for hotels (+ validation)
hotel_budget = float(input("Enter your hotel budget: "))
while hotel_budget <= 0:
    print("Budget must be positive, try again.")
    hotel_budget = float(input("Enter your hotel budget: "))

# --- NEW: Hotel price validation (try/except) ---
# This does not change your loop logic; it simply demonstrates
# validating a single price the user types in.
while True:
    try:
        hotel_price = float(input("Enter a hotel price to validate (0–2000): "))
        if 0 <= hotel_price <= 2000:
            print("That's a valid price range.")
            break
        else:
            print("Price must be between 0 and 2000.")
    except ValueError:
        print("Please enter a number like 199.99")

# Loop through hotels (basic filter)
for inn in inns:
    if inn["cost"] <= hotel_budget:
        print(f'{inn["hotel"]} - ${inn["cost"]} [OK]')
    else:
        print(f'{inn["hotel"]} - ${inn["cost"]} [Too expensive]')

# Step 3: Subtotal and tax placeholder
food_cost = float(input("Enter your food budget: "))
subtotal  = flight_cost + food_cost   # (hotel cost not added yet)
tax_rate  = 0.14
# total = subtotal + (subtotal * tax_rate)

# Step 4: Print result (placeholder)
# print(f"Hello {name}, your trip will cost ${total:.2f}")
