#!/usr/bin/env python3
import random


'''
This is an development of the classic "Rock, Paper, Scissors" game in Python. 
The game developed in single player mode and the user should competes against the computer. 
The app asks a user to enter their desired choice among rock, paper, or scissors. Then
randomly chooses an option for the computer too. After that, the app determines the winner
based on the game's rules.
This app doesn't offer any graphical interface or complex features.

Date: March 22, 2023
'''

options = ("rock", "paper", "scissors") # List of options for computer
computer = random.choice(options # This will choose a random option from your list for the computer
