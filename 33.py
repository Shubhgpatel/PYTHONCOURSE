import random as r

number = r.randint(1,100)
a = -1
guesses = 0
while(a != number):
    guesses += 1

    a = int(input("Guess the number : "))
    if(a < number):
        print("Higher number please")
    else:
        print("Lower Number Please")

print(f"You have guesed the {number} correctly in {guesses} attempts")