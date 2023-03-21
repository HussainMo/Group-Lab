## Rock, Paper, Scissors Game

### Algorithmic Standpoint
**An algorithmic explanation of how the "Rock, Paper, Scissors" game works:**

First step is to define our three possible options/input: "rock", "paper", and "scissors".
We need to add a variable called "running" and set it to True to ensure that the game keeps running until the user decides otherwise.

We need to add a while loop and set "running" as the condition, so the game runs until the user chooses to quit.

In each iteration, the script generates a random option among "rock", "paper", and "scissors" [random.choice()" function]. Then asks a user to enter "rock", "paper", or "scissors" by displaying the message "Enter rock, paper or scissors:" and store it in the variable called "player".

Next step is to check if the entry value is a valid option by starting a nested while loop with the condition "while player not in options". If the player's choice is invalid, prompt them to enter a valid option until they do so.

Once the player has entered a valid option, compare their choice and the computer's (random) choice.

Then we use conditional statements to compare the player's and the computer's choice to find the winner according to:
-	If both the player and computer make the same choice, it is a tie.
-	If the player chooses "rock" and the computer chooses "scissors", the player wins.
-	If the player chooses "paper" and the computer chooses "rock", the player wins.
-	If the player chooses "scissors" and the computer chooses "paper", the player wins.
-	Otherwise, the computer wins.

After that a message will be shown and indicating the result ("You Win!" or "Loser HaHa!").

Finally, by displaying the "Wanna play again? (y/n): " message, asks the user for the another round. If the user chooses to quit, set "running" to False to exit the loop and print out the message "Nice playing with you!"

</br>
</br>

### Roles and Responsibilities
We are a group of two. Hossein is responsible for app developing and Ariyan is a QA Tester. However, it doesn't mean that we didn't help each other. In other words, we worked on this project side by side regardless of our actual role.


</br>
</br>

### Game Flowchart

</br>

![R_P_S](http://nouvinmedia.com/wp-content/uploads/2023/03/Flowchart.png)

</br>

<div align="center">
 Rock, Paper, Scissors Game Flowchart
</div>

