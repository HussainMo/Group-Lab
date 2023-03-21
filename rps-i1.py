#!/usr/bin/env python3
import random


'''
This is an implementation of the classic "Rock, Paper, Scissors" game in Python. 
The game developed in single player mode and the user should competes against the computer. 
The app asks a user to enter their desired choice among rock, paper, or scissors. Then
randomly chooses an option for the computer too. After that, the app determines the winner
based on the game's rules.
This app doesn't offer any graphical interface or complex features.
Date: March 22, 2023
'''


options = ("rock", "paper", "scissors") # list of options for the computer
running = True

player = None
computer = random.choice(options) # This will choose a random option from your list for the computer

# Looping through until the player enters a valid choice among rock", "paper", and "scissors"
while player not in options:
    player = input("Enter rock, paper or scissors): ")

# Print out both Player and Computer's choices    
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

print("Nice playing with you!")
