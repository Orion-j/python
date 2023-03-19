import random


# guess a random number, taken input from user.

def guess(y):
    random_number = random.randint(1, y)
    # set number guessed to zero(0).
    player_guess = 0
    while player_guess != random_number:
        player_guess = int(input("guess a number: "))
        if player_guess < random_number:
            print("number low, another try!")
        elif player_guess > random_number:
            print("high number, try again.")

    print(f"Great you guessed right, it is {player_guess}!")


# guess in the range of 1 to 10.
guess(10)  # any value can be put in the argument.
