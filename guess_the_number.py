from guess_the_number_art import logo
from random import randrange

def check_answer(guess, number, attempts):
    if guess > number:
        attempts += -1
        print("Too high.")
    elif guess < number:
        attempts += -1
        print("Too low.")
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        exit()
    return attempts

def guess():
    guess = input("Make a guess:")
    if guess is int:
        pass
    else:
        exit()

def easy(number, easy_attempts):
    while easy_attempts > 0:
        print(f"You have {easy_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        # guess()
        # still missing: check if int was added and catch string input
        easy_attempts = check_answer(guess, number, easy_attempts)
    print("No attempts left. You lose!")
    return False

def hard(number, hard_attempts):
    while hard_attempts > 0:
        print(f"You have {hard_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        hard_attempts = check_answer(guess, number, hard_attempts)
    print("No attempts left. You lose!")
    return False

print(logo)
number = randrange(1, 101)
# print(f"The number is {number}")
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
easy_attempts = 10
hard_attempts = 5

game_is_on = True
while game_is_on:
    chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print("")
    if chosen_difficulty == "easy":
        easy(number, easy_attempts)  
    elif chosen_difficulty == "hard":
        hard(number, hard_attempts)
    else:
        print("Wrong answer, please try again.")
        
        
        