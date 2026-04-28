import numpy as np
def dice_roll(fixed_dice=None):
    """
    Rolls up to 3 dice, keeping any fixed dice in place. Fixed dice are dice that have the same value as one other die. If all 3 match, the turn will be worth 0.

    Parameters:
        fixed_dice (list): a list of fixed die values to keep, or None if none need to be marked as fixed.

    Returns:
        tuple: (dice, tupled_out, turn_score)
            - dice (list): List of 3 die values
            - tupled_out (bool): True if all 3 dice are the same
            - turn_score (int): Sum of dice (0 if tupled out)

    # Tests
    # result = dice_roll()
    # print(result)        # expected: a tuple of (list of 3 ints, bool, int)
    # result = dice_roll(fixed_dice=[5, 5, 2])
    # print(result[0])     # expected: first two dice should still be 5 and 5
    """

    # Gets range of rollable numbers
    numpy_numbers = np.arange(1, 7)

    # Determines if there are any fix dice already, and if not it rolls all 3 fresh
    if fixed_dice is None:
        dice = [int(x) for x in np.random.choice(numpy_numbers, size=3, replace=True)]
    else:
        # Only rerolls dice that aren't fixed
        dice = [int(x) for x in np.random.choice(numpy_numbers, size=3, replace=True)]
        for i in range(len(fixed_dice)):
           dice[i] = int(fixed_dice[i])

    # Checks which dice are fixed
    fixed_values = []
    for die in dice:
        if dice.count(die) > 1:
            fixed_values.append(die)

    # Display all 3 die and MARK WHICH ARE FIXED

    print("\nYour dice:")
    for i in range(3):
        if dice[i] in fixed_values:
            print(f"  Die {i+1}: {dice[i]}  [FIXED]")
        else:
            print(f"  Die {i+1}: {dice[i]}")

    # Checks if the dice will tuple out
    tupled_out = (dice[0] == dice[1] == dice[2])
    if tupled_out:
        print("You tupled out! You score 0 points this turn.")
        return (dice, True, 0)

    # Calculate turn score
    turn_score = int(dice[0] + dice[1] + dice[2])

    return (dice, False, turn_score)
