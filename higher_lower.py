from random import randrange
from higher_lower_art import logo, vs
from higher_lower_game_data import data
from os import system

# to find out length of the data set, len function was used
# print(len(data))

def choose_number():
  """ create random number called chosen_number """
  chosen_number = randrange(0, 50)
  return chosen_number

def choose_dataset(chosen_number):
  """ function to choose random dataset from game_data using chosen_number """
  chosen_dataset = data[chosen_number]
  return chosen_dataset

def first_entry():
  """ function to select first dataset for the game"""
  choiceA = (choose_number())
  A = choose_dataset(choiceA)
  a = A['follower_count']
  return A, a

def game(A, a, score):
  """ this is the function for the actual game """

  # select second dataset for comparison
  choiceB = (choose_number())
  B = choose_dataset(choiceB)
  b = B['follower_count']

  # print dataset A
  print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")

  print(vs)
  # print dataset B
  print(f"Against B: {B['name']}, {B['description']}, {B['country']}")

  # ask for input higher or lower
  answer = input("Who has more followers? Type 'A' or 'B': ")
  system('cls') # clears the screen
  print(logo) # prints the logo again

  # selection will be evaluated and score increased, if True: 
  if answer == 'A' and a > b:
    score += 1
    print(f"You are right! Current score: {score}")
    A, a = B, b
    return True, A, a, score
  elif answer == 'A' and a < b:
    print(f"Sorry, that's wrong. Final score: {score}")
    return False, A, a, score
  elif answer == 'B' and a > b:
    print(f"Sorry, that's wrong. Final score: {score}")
    return False, A, a, score
  elif answer == 'B' and a < b:
    score += 1
    print(f"You are right! Current score: {score}")
    A, a = B, b
    return True, A, a, score
  else:
    print("Wrong input or same dataset was randomly selected twice. Please try again.")
    A, a = B, b
    return True, A, a, score

# the actual start of the program
print(logo)
A, a = first_entry()
score = 0
play = True
while play == True:
  play, A, a, score = game(A, a, score)
