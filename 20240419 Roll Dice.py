# Want to create a roll a dice feature for numbers between 1 to 12. The number will have to be random. 

import random

def roll_dice():
    return random.randint(1, 12) # This function generates a random integer bewteen 1 and 12.

dice_roll = roll_dice() # This encapsulates the above logic, and calling it assigns a random number to the dice_roll variable

print("The dice rolled: ", dice_roll) # The result is printed to the console.

