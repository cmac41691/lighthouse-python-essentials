def navigator_menu():
    """
    Display the game selection menu and return a choice identifier.

    Returns:
        str: One of the following keys:
            - "hangman"
            - "mad_libs"
            - "trivia"
            - "reset"
            - "exit"

    This function loops until the user enters a valid option.
    It isolates all menu logic so the main game loop remains clean.
    """

    
    while True:
        print("\n=== Game Selection Menu ===")
        print("1. hangman")
        print("2. Mad Libs")
        print("3. Trivia")
        print("4. Reset Stats")
        print("5. Exit")

        user_choice = input("Choose 1-5: ").strip()

        if user_choice == "1":
            return "hangman"
        elif user_choice == "2":
            return "mad_libs"
        elif user_choice == "3":
            return "trivia"
        elif user_choice == "4":
            return "reset"
        elif user_choice == "5":
            return "exit"
        else:
            print("Invalid choice. Please try again.")
