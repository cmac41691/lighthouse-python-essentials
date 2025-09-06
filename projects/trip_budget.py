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
    {"hotel": "Delta", "cost": 50},
    {"hotel": "Four Seasons", "cost": 250},
    {"hotel": "Fairmont", "cost": 150}
]

hotel_price = 0  # default
hotel_budget = float(input("Enter your hotel budget: "))
while hotel_budget <= 0:
    print("Budget must be positive, try again.")
    hotel_budget = float(input("Enter your hotel budget: "))

affordable_hotels = []
for inn in inns:
    if inn["cost"] <= hotel_budget:
        print(f"{inn['hotel']} - ${inn['cost']} [OK]")
        affordable_hotels.append(inn)
        hotel_price = inn["cost"]  # take the last affordable hotel cost
    else:
        print(f"{inn['hotel']} - ${inn['cost']} [Too expensive]")

# Step 3: Subtotal and tax
food_cost = float(input("Enter your food budget: "))
subtotal = flight_cost + food_cost + hotel_price
tax_rate = 0.14
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

# Step 4: Print result
print("\n--- Trip Summary ---")
print(f"Hello {name}, here are your trip details:")
print(f"  Flight:   ${flight_cost:.2f}")
print(f"  Hotel:    ${hotel_price:.2f}")
print(f"  Food:     ${food_cost:.2f}")
print(f"  Subtotal: ${subtotal:.2f}")
print(f"  Tax:      ${tax_amount:.2f}")
print(f"  Total:    ${total:.2f}")
