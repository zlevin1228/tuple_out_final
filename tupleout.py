from diceroll import dice_roll
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ask the user for how many people are going to play (2 or 3 players)
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
            print("Invalid input for player count. Please enter 2 or 3.")
    except ValueError:
        print("Invalid input. Please enter a number:\n")

# Store players and their scores in a dictionary
if player_count == 2:
    players = {player_1: 0, player_2: 0}
else:
    players = {player_1: 0, player_2: 0, player_3: 0}

# Tracks score history each turn for the end game visualization
score_history = {player_1: [0], player_2: [0]}
if player_count == 3:
    score_history[player_3] = [0]

# Sets the target score to win
target_score = 50

# Main game loop - continues until someone reaches the target score
game_over = False
while not game_over:
    for current_player in players:
        print(f'\n{current_player}, please begin your turn!')
        print("Current Scores:")
        for name, score in players.items():
            print(f'  {name}: {score}')

        # Each turn starts with a fresh dice roll
        dice, tupled_out, turn_score = dice_roll()

        # Player can keep rerolling until they tuple out or choose to stop
        while not tupled_out:
            reroll = input("\nWould you like to roll again? ('y' or 'n'): ")

            if reroll == "y":
                # Check which dice are fixed (matching values)
                fixed_values = []
                for die in dice:
                    if dice.count(die) > 1:
                        fixed_values.append(die)
                # Reroll with fixed dice locked in if any exist
                if len(fixed_values) > 0:
                    dice, tupled_out, turn_score = dice_roll(fixed_dice=fixed_values)
                else:
                    dice, tupled_out, turn_score = dice_roll()
            elif reroll == "n":
                print(f'\n{current_player} scored {turn_score} on this turn.')
                break
            else:
                print("Please respond with either 'y' or 'n'")

        # Tupling out means 0 points for the turn
        if tupled_out:
            turn_score = 0

        # Add turn score to the player's total and record it
        players[current_player] = players[current_player] + turn_score
        print(f'{current_player} now has a total score of: {players[current_player]}')
        score_history[current_player].append(players[current_player])

        # Check if the player has reached the target score
        if players[current_player] >= target_score:
            print(f"\n{current_player} wins with {players[current_player]} points!")
            print("\nFinal Scores:")
            for name, score in players.items():
                print(f"  {name}: {score}")

            # Save game result to file
            with open("gameresults.txt", "a") as records_file:
                records_file.write("------ Game Result ------\n")
                records_file.write(f"Winner: {current_player}\n")
                for name, score in players.items():
                    records_file.write(f"  {name}: {score}\n")
                records_file.write("\n")

            # Display all past game records
            print("\n--- Past Game Records ---")
            with open("gameresults.txt", "r") as records_file:
                for line in records_file:
                    print(line)

            # Pad score histories to equal length for the DataFrame
            max_turns = max(len(score_history[name]) for name in score_history)
            for name in score_history:
                while len(score_history[name]) < max_turns:
                    score_history[name].append(score_history[name][-1])

            # Build DataFrame and plot score progression
            score_df = pd.DataFrame(score_history)
            score_df.index.name = "Turn"
            sns.lineplot(data=score_df)
            plt.title("Score Progression")
            plt.xlabel("Turn")
            plt.ylabel("Total Score")
            plt.show()

            game_over = True
            break