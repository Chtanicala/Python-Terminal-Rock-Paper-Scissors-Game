#Make a rock paper scissors game
#prompts the user to input their choice as rock, paper, or scissors and will accept nothing else
#evaluates this choice a against a random selection from these choices and decides the winner.
#Stores record, and loops back

import random

while True:
    choices = ["rock", "paper", "scissors"]
    player_selection = None
    computer_selection = random.choice(choices)
    total_score = 0

    while player_selection not in choices: 
        player_selection = input("Please select rock, paper, or scissors: ").lower()

    if player_selection == computer_selection:
        print("Player: " + player_selection)
        print("Computer: " + computer_selection)
        print("Tie!")
    if player_selection == "rock":
            if computer_selection == "paper": 
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Lose!")

                total_score = total_score -1
                print("Your total score is " + str(total_score))
            if computer_selection == "scissors":
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Won!")
                
                total_score = total_score +1
                print("Your total score is " + str(total_score))

