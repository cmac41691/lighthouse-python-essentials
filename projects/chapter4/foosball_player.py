players = ["Striker Sam", "Goalie Gina", "Rocket Ralph", "Twister Tina"]


while True:
    action = input("add, remove, change, or quit: ")

    if action == "quit":
        break

    if action == "add":
        user = input("Enter the player's name: ")
        players.append(user)

    elif action == "remove":
        user = input("Enter the name to remove: ")
        if user in players:
            players.remove(user)
        else:
            print("That player is not in the list.")

    elif action == "change":
        index = int(input("Enter the index of the player to replace: "))
        new_name = input("Enter the new player's name: ")
        players[index] = new_name

    else:
        print("Invalid action. Try again.")

print(f"Final team: {players}")
