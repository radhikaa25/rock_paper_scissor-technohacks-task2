import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    choices = ["Rock", "Paper", "Scissors"]
    
    while True:
        user_choice = input("Your turn: ")
        if user_choice in ("1", "2", "3"):
            user_choice = choices[int(user_choice) - 1]
            break
        else:
            print("Invalid input. Please enter a number from 1 to 3.")
    
    computer_choice = random.choice(choices)
    
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("Computer wins!")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break