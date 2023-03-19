import random


# Rock Paper Scissor Game!
def rockgame():
    user_input: str = input("Rock(r), Scissors(s) or Paper(p)? ").lower()
    machine = random.choice(['r', 's', 'p'])

    if user_input == machine:
        return "It's a tie! 😇"

    return "You won! 😍" if is_win(user_input, machine) else "You lost, 😒."


def is_win(player1, player2):
    # return True if player wins.
    if (player1 == 'r' and player2 == 's') or (player1 == 'p' and player2 == 'r') \
            or (player1 == 's' and player2 == 'p'):
        return True


print(rockgame())
