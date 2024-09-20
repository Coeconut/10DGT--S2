# Guess the number
# Author: Andrew Coe
# Date: 20/09/2024
# Version: 1.0


# Different types of variables
# Store a number


import random

play = True
high_score = ()

while play:
    num = random.randint(1,50)
    max_attepts = 5
    attempts = 0
    guess = None
    score = None

    print("Guess the Number between the numbers 1 and 50 in 5 attempts\n")

    while guess != num and attempts < max_attepts:
        attempts += 1
        print ("")
        print ("Attempt",attempts)
        guess = int(input("Guess:"))
        if num > guess:
            print ("higher")
        elif num < guess:
            print ("lower")
        else:
            print ("You win")
            if score < high_score:
                high_score = score
                print ("New High Score!")

    if guess != num:
        print("You lose, The number was:", num)

    again=str(input("Do you want to play again, type y/n "))
    if again == "n":
        play = False