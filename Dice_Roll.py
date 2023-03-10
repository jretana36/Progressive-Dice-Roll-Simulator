import time
import random
print("Welcome to the dice roll simulator!")
minimum_Value = 1
maximum_Value = 6
roll_dice_Again = "yes"
while roll_dice_Again == "yes" or roll_dice_Again == "y":
    print("Currently rolling the dice...")
    time.sleep(1.5)
    print("Still rolling the dice...")
    time.sleep(1.5)
    print("The values of the dice are :")
    print(random.randint(minimum_Value, maximum_Value))
    print(random.randint(minimum_Value, maximum_Value))
    roll_dice_Again = input("Would you like to roll again?")
