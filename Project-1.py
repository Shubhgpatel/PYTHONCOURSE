# Project 1 : SNAKE,WATER AND GUN GAME

import random 

computer = random.choice(["s", "w", "g"])
you = input("Your Turn : Snake(s) Water(w) or Gun(g) ? :")

if computer == you:
    print("The game is a tie")
    print(f"Computer chose {computer} and You chose {you}")
elif computer == "s" and you == "w":
    print("You Lose")
    print(f"Computer chose {computer} and You chose {you}")
elif computer == "s" and you == "g":
    print("You Win")
    print(f"Computer chose {computer} and You chose {you}")
elif computer == "w" and you == "g":
    print("You Lose")
    print(f"Computer chose {computer} and You chose {you}")
elif computer == "w" and you == "s":
    print("You Win")
    print(f"Computer chose {computer} and You chose {you}")
elif computer == "g" and you == "s":
    print("You Lose")
    print(f"Computer chose {computer} and You chose {you}")
elif computer == "g" and you == "w":
    print("You Win")
    print(f"Computer chose {computer} and You chose {you}")
else:
    print("Invalid Input")
    print("Please enter s for Snake, w for Water and g for Gun")

