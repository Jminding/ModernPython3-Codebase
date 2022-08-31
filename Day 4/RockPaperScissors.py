import random

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

user_wins = 0
computer_wins = 0

while True:
    user_choice = input("Input 'rock', 'paper', or 'scissors': ")
    if user_choice not in choices:
        print("Invalid.")

    print(f"Computer: {computer_choice}")
    print(f"Player: {user_choice}")

    if user_choice == "rock" and computer_choice == "paper":
        print("Computer wins!")
        computer_wins += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("Player wins!")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("Player wins!")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Computer wins!")
        computer_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Player wins!")
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Computer wins!")
        computer_wins += 1
    else:
        print("Tie!")
    
    print(f"{user_wins} - {computer_wins}")

    if user_wins >= 2:
        print("The Player is the winner!")
        break
    elif computer_wins >= 2:
        print("The Computer is the winner!")
        break
