#Import random module to randomly select choices for computer's input
import random

#Wins, Ties and Losses are kept track in the global scope to avoid refreshing
wins = 0
losses = 0
ties = 0

#The game is inside a loop that will continue until the player decides to quit the game
while True:
    choices = ["rock", "paper", "scissors"]
    replay_choices = ["yes", "no"]
    player_selection = None
    computer_selection = random.choice(choices)
    replay_game = None
    
#validates the player selection to ensure it is only a choice in the choices variable
    while player_selection not in choices: 
        player_selection = input("Please select rock, paper, or scissors: ").lower()
        
#Tie scenario that encompasses all posible ties
    if player_selection == computer_selection:
        print("Player: " + player_selection)
        print("Computer: " + computer_selection)
        print("Tie!")
        ties = ties + 1
#Win/Loss Scenarios for a player choice that displays the player and computer's choice and evaluates the two against each other to tally up wins, losses, and ties   
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
#informs the player their total wins, losses, and ties           
    print("Current Score: Wins: " + str(wins) + " Losses: " + str(losses) + " Ties: " + str(ties))
#asks the player to replay the game, validating to only yes or no choices. If no is selected the game stops
    while replay_game not in replay_choices:
        replay_game =  input("Play Again? Yes/No: ").lower()
    
    if replay_game == "no":
         break