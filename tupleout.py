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

# Store players and scores in a dictionary
if player_count == 2:
    players = {player_1: 0, player_2: 0}
else:
    players = {player_1: 0, player_2: 0, player_3: 0}

# Sets score to win the game
target_score = 50

# Loops the game until a winner is determined
game_over = False
while not game_over:
    # This will loop each player through their turns
    for current_player in players:
        print(f'\n{current_player}, please begin your turn!')
        print("Current Scores: ")
        for name, score in players.items():
            print(f' {name}: {score}')

        # A turn will start with a dice roll
        dice, tupled_out, turn_score = dice_roll()

        # Asks if the player wants to reroll
        while not tupled_out:
            reroll = input("\nWould you like to roll again? ('y' or 'n'): ")
            
            # Runs through user input to see if a reroll will happen
            if reroll == "y":
                # Checks if dice are fixed before it lets you continue
                fixed_values = []
                for die in dice:
                    if dice.count(die) > 1:
                        fixed_values.append(die)
                # Rerolls dice with fixed values ignored (if necessary)
                if len(fixed_values) > 0:
                    dice, tupled_out, turn_score = dice_roll(fixed_dice=fixed_values)
                else:
                    dice, tupled_out, turn_score = dice_roll()
            elif reroll == "n":
                # This will result in no reroll and the end of a turn, and it will then add the score
                print(f'\n{current_player} scored {turn_score} on this turn.')
                break
            else:
                print("Please respond with either 'y' or 'n'")
        # If tupled out, the score for the turn is 0.
        if tupled_out:
            turn_score = 0

        # Add the score from the turn to the player's total
        players[current_player] = players[current_player] + turn_score
        print(f'{current_player} now has a total score of: {players[current_player]}')

        # Checks if the player has now reached the target score
        if players[current_player] >= target_score:
            print(f"\n {current_player} wins with {players[current_player]} points!")
            game_over = True
            break
