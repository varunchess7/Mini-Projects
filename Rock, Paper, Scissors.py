import random

choices = {"Rock", "Paper", "Scissors"}
player_choice = input("Player Choice: ")
computer_choice = random.choice(choices)
print("Computer Choice: ", computer_choice)

if player_choice == "Rock" and computer_choice == "Rock":
    print("Tie")
elif player_choice == "Paper" and computer_choice == "Paper":
    print("Tie")
elif player_choice == "Scissors" and computer_choice == "Scissors":
    print("Tie")
elif player_choice == "Rock" and computer_choice == "Paper":
    print("Computer Wins!")
elif player_choice == "Rock" and computer_choice == "Scissors":
    print("Player Wins!")
elif player_choice == "Paper" and computer_choice == "Rock":
    print("Player Wins!")
elif player_choice == "Paper" and computer_choice == "Scissors":
    print("Computer Wins!")
elif player_choice == "Scissors" and computer_choice == "Rock":
    print("Computer Wins!")
elif player_choice == "Scissors" and computer_choice == "Paper":
    print("Player Wins")