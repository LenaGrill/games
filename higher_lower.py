from random import randrange
from higher_lower_art import logo, vs
from higher_lower_game_data import data

print(logo)
# print(len(data))

def choose_number():
  """ create random number called chosen_number """
  chosen_number = randrange(0, 50)
  return chosen_number

def choose_person(chosen_number):
  """ function to choose random person from game_data using chosen_number """
  chosen_person = data[chosen_number]
  return chosen_person

def first_entry():
  """ function to create first entry for the game"""
  choiceA = (choose_number())
  A = choose_person(choiceA)
  a = A['follower_count']
  return A, a


def game(A, a, score):

  choiceB = (choose_number())
  B = choose_person(choiceB)
  b = B['follower_count']

  # print person A data
  print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")

  print(vs)
  # print person B data
  print(f"Against B: {B['name']}, {B['description']}, {B['country']}")

  # ask for input higher or lower
  print(a, b)
  answer = input("Who has more followers? Type 'A' or 'B': ")

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


# if right, choose next random person and repeat above
A, a = first_entry()
score = 0
play = True
while play == True:
  play, A, a, score = game(A, a, score)
