import random


# guess by the computer, you decide when it guesses your number.
def guessNumber(x):

    global number_guess
    low_number = 1
    high_number = x
    feedback = ""

    while feedback != "c":
        if low_number != high_number:
            number_guess = random.randint(low_number, high_number)
        else:
            guess = low_number
        feedback = input(f"is {number_guess} too high(h), low(l) or correct(c): ")

        if feedback == "h":
            high_number = number_guess - 1
        elif feedback == "l":
            var = low_number == number_guess + 1
    print(f"Correct guess😂! {number_guess}.")


guessNumber(100)
