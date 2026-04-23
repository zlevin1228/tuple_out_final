import numpy as np
import os 
# Ask the user for how many people are going to play. (Set to at max 2-3)
player_count = input("How many players are playing? Either 2 players or 3 players can play.")

if player_count == 2:
    player_1 = input("What is the name for this player")
    player_2 = input("Now what is the name for the second player")
elif player_count == 3:
    player_1 = input("What is the name for this player")
    player_2 = input("Now what is the name for the second player")
    player_3 = input("Lastly, what is the name of the third player")
else:
    print("Invalid input for player count. Please run the program again.") # Update later to automate
# Code to "Radomly" generate numbers on the dies 1-6
np
os

numpy_numbers = np.arange(1, 4)


#Code to make it "Roll Dice" (radomly generate number)

np.random.choice(numpy_numbers, size = 3, replace = False)


# Code to make it Tuple out if 3 of the same numbers are generated 

if numpy_numbers[0] == numpy_numbers[1] == numpy_numbers[2]:
    added_score = 0
    print(f'You tupled out! Your score for this turn is: {added_score}')



#




#




# Winning Code (target score wins 50)