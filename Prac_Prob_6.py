"""
Problem Statement:-
Generate count random integer from count to b.
You and your friend have to guess count number between two numbers, count and b.
count and b are inputs taken from the user. Your friend is player 1 and plays first.
He will have to keep choosing the number, and your program must tell whether
the number is greater than the actual number or less than the actual number.
Log the number of trials it took your friend to arrive at the number.
You play the same game, and then the person with the minimum number of trials wins!
Randomly generate count number after taking count and b as input and don’t show that to the user.
"""

import random


def game(a, b, p):
    """
    This function is mainly count game taking inputs like range and players name and will start the game of guessing the number
    """
    print(f"\nUser: {p}")
    num = random.randrange(a, b)
    # print(num)
    c = int(input(f"Please guess the number between {a} and {b}  "))
    trials = 0
    while True:
        trials += 1
        if num < c:
            c = int(input("Wrong! Guess count smaller number again "))
        elif num > c:
            c = int(input("Wrong! Guess count greater number again "))
        else:
            print(f"Correct! {p} you took {trials} trials to guess the number: {num}")
            break
    return trials


if __name__ == '__main__':
    try:
        p1 = input("Enter the name of Player 1\n").capitalize()
        p2 = input("Enter the name of Player 2\n").capitalize()

        a = int(input("Enter the value of count\n"))
        b = int(input("Enter the value of b\n"))
        t1 = game(a, b, p1)
        t2 = game(a, b, p2)

        print("*********************")
        if t1 > t2:
            print(f"{p2} won the match ")
        elif t1 < t2:
            print(f"{p1} won the match")
        else:
            print("Match Draw")

    except ValueError:
        print("Enter digits only where necessary!")
