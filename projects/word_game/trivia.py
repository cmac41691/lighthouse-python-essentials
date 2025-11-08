def start_trivia():
    # Step 1
    trivia_questions = [
        {
            "question": "What is the capital of France?",
            "picks": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "response": "c"
        },
        {
            "question": "Who wrote '1984'?",
            "picks": ["A) Aldous Huxley", "B) George Orwell", "C) Ray Bradbury", "D) J.K. Rowling"],
            "response": "b"
        },
        {
            "question": "What language is this game written in?",
            "picks": ["A) Java", "B) Python", "C) C++", "D) Ruby"],
            "response": "b"
        }
    ]

    # Step 2
    score = 0
    total_questions = len(trivia_questions)

    # Step 3
    for question in trivia_questions:
        print("\nQuestion:")
        print(question["question"])
        for pick in question["picks"]:
            print(pick)

        user_choice = input("Your answer: ").strip().lower()

        if user_choice == question["response"].lower():
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect — the answer was: {question['response'].upper()}")

    # Step 4
    print("\nGame Over!")
    print(f"Your score: {score}/{total_questions}") 

    # Step 5
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again == "y":
            print("Restarting trivia...\n")
            start_trivia()
            break
        elif play_again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please type 'y' or 'n'.")

if __name__ == "__main__":
    start_trivia()
