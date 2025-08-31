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

resources = float(input("Enter your hotel budget: "))
while resources <= 0:
    print("Budget must be positive, try again.")
    resources = float(input("Enter your hotel budget: "))

# Loop through hotels (basic filter)
for inn in inns:
    if inn["cost"] <= resources:
        print(f"{inn['hotel']} - ${inn['cost']} [OK]")
    else:
        print(f"{inn['hotel']} - ${inn['cost']} [Too expensive]")

# Step 3: Subtotal and tax placeholder
food_cost = float(input("Enter your food budget: "))
subtotal = flight_cost + food_cost   # hotel cost not added yet
tax_rate = 0.14
# total = subtotal + (subtotal * tax_rate)

# Step 4: Print result (placeholder)
# print(f"Hello {name}, your trip will cost ${total:.2f}")

