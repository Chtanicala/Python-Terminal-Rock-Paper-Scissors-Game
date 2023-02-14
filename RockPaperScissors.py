#Make a rock paper scissors game
#prompts the user to input their choice as rock, paper, or scissors and will accept nothing else
#evaluates this choice a against a random selection from these choices and decides the winner.
#Stores record, and loops back

import random

while True:
    choices = ["rock", "paper", "scissors"]
    replay_choices = ["yes", "no"]
    player_selection = None
    computer_selection = random.choice(choices)
    total_score = 0
    replay_game = None

    while player_selection not in choices: 
        player_selection = input("Please select rock, paper, or scissors: ").lower()

    if player_selection == computer_selection:
        print("Player: " + player_selection)
        print("Computer: " + computer_selection)
        print("Tie!")
    elif player_selection == "rock":
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
    elif player_selection == "scissors":
            if computer_selection == "rock": 
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Lose!")

                total_score = total_score -1
                print("Your total score is " + str(total_score))
            if computer_selection == "paper":
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Won!")

                total_score = total_score +1
                print("Your total score is " + str(total_score))
    elif player_selection == "paper":
            if computer_selection == "scissors": 
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Lose!")

                total_score = total_score -1
                print("Your total score is " + str(total_score))
            if computer_selection == "rock":
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Won!")

                total_score = total_score +1
                print("Your total score is " + str(total_score))

    while replay_game not in replay_choices:
        replay_game =  input("Play Again? Yes/No: ").lower()
    
    if replay_game == "no":
         break