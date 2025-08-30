# Trip Budget Calculator (prototype)

# Step 1: Collect user input
name = input("Enter your name: ")

flight_cost = float(input("Please put in the cost:"))
while flight_cost > 1000:
    print("That's too much, please try again.")
    flight_cost = float(input("Put in the cost:"))

print("Excellent! your flight is booked under $1000")

# Step 2: Hotels stored as list of dictionaries
inns = [
    {"hotel": "Delta", "cost": 50},
    {"hotel": "Four Seasons", "cost": 250},
    {"hotel": "Fairmont", "cost": 150}
]

# Loop (work in progress)
resources = 200

for inn in inns:
    if inn["cost"] <= resources:
        print(f"{inn['hotel']} - ${inn['cost']} [OK]")
    else:
        print(f"{inn['hotel']} - ${inn['cost']} [Too expensive]")


# Step 3: Placeholder subtotal & tax
subtotal = 0
# subtotal = flight_cost + inn_cost + food_cost
# total = subtotal + (subtotal * tax_rate)

tax_rate = 0.14   # placeholder

# Step 4: Print result
# print(f"Hello {name}, your trip will cost ${total:.2f}")
