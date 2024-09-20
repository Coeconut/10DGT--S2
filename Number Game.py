# Guess the number
# Author: Andrew Coe
# Date: 20/09/2024
# Version: 1.1


import random

play = True
high_score = float('inf')

while play:
    num = random.randint(1, 100)
    max_attepts = 10
    attempts = 0
    guess = None
    score = None

    print("\nGuess the Number between the numbers 1 and 100 in 10 attempts\n")

    while guess != num and attempts < max_attepts:
        attempts += 1
        print (f"Attempt",attempts)
        guess = int(input("Guess:"))
        if num > guess:
            print ("higher")
        elif num < guess:
            print ("lower")
        else:
            score = attempts
            print ("You win, your score is",score)
            if high_score > score:
                high_score = score
                print ("Your New High Score is",high_score)

    if guess != num:
        print("You lose, The number was: {num}")

    again=str(input("Do you want to play again, type y/n "))
    if again == "n":
        play = False
        print("You lose, The number was:", num)

    again=str(input("Do you want to play again, type y/n "))
    if again == "n":
        play = False
