import random

def roll_dice():
    return random.randint(1, 6)

while True:
    user = input("Roll the dice? (yes/no): ").lower()
    
    if user == "yes":
        dice = roll_dice()
        print("🎲 You got:", dice)
        
    elif user == "no":
        print("Thanks for playing!")
        break
    
    else:
        print("Invalid input! Please type yes or no.")