from guess_the_number_art import logo
from random import randrange

print(logo)
number = randrange(1, 101)
print(f"The number is {number}")

def easy():
    easy_attempts = 10
    while easy_attempts > 0:
        print(f"You have {easy_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess > number:
            easy_attempts += -1
            print("Too high.")
        elif guess < number:
            easy_attempts += -1
            print("Too low.")
        elif guess == number:
            print(f"You got it! The answer was {number}")
            exit()
    return False

def hard():
    hard_attempts = 5
    while hard_attempts > 0:
        print(f"You have {hard_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess > number:
            hard_attempts += -1
            print("Too high.")
        elif guess < number:
            hard_attempts += -1
            print("Too low.")
        elif guess == number:
            print(f"You got it! The answer was {number}")
            exit()
    return False

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
  
game_is_on = True
while game_is_on:
    chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print("")
    if chosen_difficulty == "easy":
        easy()  
    elif chosen_difficulty == "hard":
        hard()
    else:
        print("Wrong answer, please try again.")
        
        
        