# Tuple Out Dice Game

## What is This?
This is a 2-3 player dice game where players take turns rolling three dice to score 
points. The first player to reach 50 points wins!

## Features
- Supports 2 or 3 players
- Fixed dice are clearly marked as [FIXED] during rerolls
- Current scores are displayed at the start of each turn
- Game results are saved to gameresults.txt after each game, keeping records across 
  multiple games
- A score progression chart is displayed at the end of each game showing how each 
  player's score changed over time

## How to Run
1. Open a terminal
2. Navigate to the folder using the cd command
3. Run the program using 'python tupleout.py'
4. Follow the prompts to set up and play the game

## Required Libraries
Before running, make sure you have the following libraries installed:

    conda install numpy pandas seaborn matplotlib

## How to Play
- Enter the number of players (2 or 3) and each player's name
- Each turn, your three dice are automatically rolled
- Any two dice with matching values are marked as [FIXED] and cannot be rerolled
- Enter 'y' to reroll non-fixed dice, or 'n' to keep your current score
- If all three dice match at any point, you "tuple out" and score 0 for that turn
- The first player to reach 50 points wins!

## Files
- tupleout.py — main game file
- diceroll.py — handles dice rolling logic
- gameresults.txt — created automatically to store past game results

## Things to Note
- Close the chart window at the end of the game to fully exit the program
- Any outstanding characters used in the terminal may end the program