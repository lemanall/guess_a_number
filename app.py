import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer,turns):
    if guess > answer:
        print("Too high!")

        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"Correct! Answer is {answer}")


def set_difficulty():
    level= input("Choose your difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():

    print('Welcome to the number guessing game!')
    print("I'm thinking of a number between 1 and 100!")

    answer = random.randint(1, 100)
    print(f"The correct answer is {answer}")
    turns = set_difficulty()
    print(f"You have {turns} guesses left.")

    guess = 0
    while guess != answer:

        guess = int(input("Make a guess: "))
        check_answer(guess, answer, turns)


game()