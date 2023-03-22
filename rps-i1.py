#!/usr/bin/env python3
import random


'''
This is an implementation of the classic "Rock, Paper, Scissors" game in Python. 
The game developed in single player mode and the user should competes against the computer. 
The app asks a user to enter their desired choice among rock, paper, or scissors. Then
randomly chooses an option for the computer too. After that, the app determines the winner
based on the game's rules, and finally offers to play again by asking a yes or no question.
This app  doesn't offer any graphical interface or complex features.
Date: March 22, 2023
'''

options = ("rock", "paper", "scissors") # list of options for the computer
running = True

while running:
	# Set the player's choice to None
    player = None
    # Computer randomly choices among rock", "paper", and "scissors" # This will choose a random option from your list for the computer
    computer = random.choice(options)

    # Looping through until the player enters a valid choice among rock", "paper", and "scissors"
    while player not in options:
        player = input("Enter rock, paper or scissors): ")

    # Print lout both Player and Computer's choices    
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # Checking the winning condition
    if player == computer:
        print("That's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("Loser HaHa!")

    # Asking the player if they want to play again, and breaking the loop otherwise
    if not input("Wanna play again? (y/n): ") == "y":
        running = False

print("Nice playing with you!")