import os 
import numpy as np
from diceroll import dice_roll
# Ask the user for how many people are going to play. (Set to at max 2-3)
while True:
    try:
        player_count = int(input("How many players are playing?\nEither 2 players or 3 players can play: "))

        if player_count == 2:
            player_1 = input("What is the name for this player? ")
            player_2 = input("Now what is the name for the second player? ")
            break
        elif player_count == 3:
            player_1 = input("What is the name for this player? ")
            player_2 = input("Now what is the name for the second player? ")
            player_3 = input("Lastly, what is the name of the third player? ")
            break
        else:
            print("Invalid input for player count. Please enter 2 or 3.") # Update later to automate
    except ValueError:
        print("Invalid input. Please enter a number:\n")
# Code to "Randomly" generate numbers on the dies 1-6
turn_score = 0
added_score = 0
total_score = 0


# Code to make it "Roll Dice" (radomly generate number)

result = dice_roll()

# Code to make it Tuple out if 3 of the same numbers are generated 



#




# 




# Winning Code (target score wins 50)