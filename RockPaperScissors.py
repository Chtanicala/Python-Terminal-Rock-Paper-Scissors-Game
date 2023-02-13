#Make a rock paper scissors game
#prompts the user to input their choice as rock, paper, or scissors and will accept nothing else
#evaluates this choice a against a random selection from these choices and decides the winner.
#Stores record, and loops back

import random

choices = ["rock", "paper", "scissors"]
#substitute this with string format to allow easier subsitution

player_selection = None

computer_selection = random.choice(choices)

while player_selection not in choices: 
    player_selection = str(input("Please select rock, paper, or scissors: ")).lower


def rps_game():
    total_score = 0
    if player_selection() == "rock" and computer_selection() == "paper":
        print("You Lose!")
        total_score = total_score -1
        print("Your total score is " + str(total_score))
    elif player_selection() == "rock" and computer_selection() == "scissors":
        print("You Won!")
        total_score = total_score +1
        print("Your total score is " + str(total_score))
    elif player_selection() == "rock" and computer_selection() == "rock":
        print("Tie!")
        total_score = total_score +0
        print("Your total score is " + str(total_score))
    elif player_selection() == "scissors" and computer_selection() == "paper":
        print("You Won!")
        total_score = total_score +1
        print("Your total score is " + str(total_score))
    elif player_selection() == "scissors" and computer_selection() == "rock":
        print("You Lose!")
        total_score = total_score -1
        print("Your total score is " + str(total_score))
    elif player_selection() == "scissors" and computer_selection() == "scissors":
        print("Tie!")
        total_score = total_score +0
        print("Your total score is " + str(total_score))
    elif player_selection() == "paper" and computer_selection() == "rock":
        print("You Won!")
        total_score = total_score +1
        print("Your total score is " + str(total_score))
    elif player_selection() == "paper" and computer_selection() == "paper":
        print("Tie!")
        total_score = total_score +0
        print("Your total score is " + str(total_score))
    elif player_selection() == "paper" and computer_selection() == "scissors":
        print("You Lose!")
        total_score = total_score -1
        print("Your total score is " + str(total_score))

rps_game()