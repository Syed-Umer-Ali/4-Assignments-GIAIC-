import random

def roll_dice():
    return random.randint(1, 6)

def simulate_rolls():
    for roll_number in range(1, 4):  # Roll dice three times
        die1 = roll_dice()
        die2 = roll_dice()
        print(f"Roll {roll_number}:\n Die 1 = {die1},\n Die 2 = {die2}")

simulate_rolls()