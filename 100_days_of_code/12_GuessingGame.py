from random import randint
from Art.art import guessing_game_logo
D_LEVEL = 5
E_LEVEL = 10


def set_difficulty():
    level = input("Set the level E or D of the difficulty\n")
    level.lower()
    if level == "e":
        return E_LEVEL
    else:
        return D_LEVEL


def check_asnwer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print("Correct")


def game():
    print(guessing_game_logo+"\n")
    print("Welcome to the guessing game")
    answer = randint(1, 100)
    turns = set_difficulty()
    print(f"You have {turns} attempts")
    print("Choose a number between 1 and 100")
    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left")
        while True:
            try:
                guess = int(input("Number: "))
                break  # If the input is successfully converted to an integer, exit the loop
            except ValueError:
                print("Choose only numbers")
        turns = check_asnwer(guess, answer, turns)
        if turns == 0:
            print("You run out of turns YOU LOST")
            return
        elif guess != answer:
            print("Guess again")

game()
