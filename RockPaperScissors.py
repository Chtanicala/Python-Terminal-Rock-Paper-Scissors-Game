#Import random module to randomly select choices for computer's input
import random

#Wins, Ties and Losses are kept track in the global scope to avoid refreshing
wins = 0
losses = 0
ties = 0

while True:
    choices = ["rock", "paper", "scissors"]
    replay_choices = ["yes", "no"]
    player_selection = None
    computer_selection = random.choice(choices)
    replay_game = None
    

    while player_selection not in choices: 
        player_selection = input("Please select rock, paper, or scissors: ").lower()

    if player_selection == computer_selection:
        print("Player: " + player_selection)
        print("Computer: " + computer_selection)
        print("Tie!")
        ties = ties + 1
        
    elif player_selection == "rock":
            if computer_selection == "paper": 
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Lose!")
                losses += 1
                
            if computer_selection == "scissors":
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Won!")
                wins += 1
                
    elif player_selection == "scissors":
            if computer_selection == "rock": 
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Lose!")
                losses += 1
                
            if computer_selection == "paper":
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Won!")
                wins += 1
                
    elif player_selection == "paper":
            if computer_selection == "scissors": 
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Lose!")
                losses += 1
                
            if computer_selection == "rock":
                print("Player: " + player_selection)
                print("Computer: " + computer_selection)
                print("You Won!")
                wins += 1
                
    print("Current Score: Wins: " + str(wins) + " Losses: " + str(losses) + " Ties: " + str(ties))

    while replay_game not in replay_choices:
        replay_game =  input("Play Again? Yes/No: ").lower()
    
    if replay_game == "no":
         break