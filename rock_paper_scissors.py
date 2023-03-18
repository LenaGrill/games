import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

random_choice = random.randrange(0, 2) # randomly selects one of three numbers

if random_choice == 0:
  computers_choice = rock
elif random_choice == 1:
  computers_choice = paper
elif random_choice == 2:
  computers_choice = scissors

users_input = input("do you choose rock, paper or scissors? ")
users_input = users_input.lower()
if users_input == "rock":
  users_choice = rock
elif users_input == "paper":
  users_choice = paper
elif users_input == "scissors":
  users_choice = scissors
else:
  print("You wrote an invalid input, you lose!")
  exit()
print("Your choice: ", users_choice)
print("Computers choice: ", computers_choice)

if users_choice == computers_choice:
  print("Draw!")
elif users_choice == rock and computers_choice == paper:
  print("You lose!")
elif users_choice == rock and computers_choice == scissors:
  print("You win!")
elif users_choice == paper and computers_choice == scissors:
  print("You lose!")
elif users_choice == paper and computers_choice == rock:
  print("You win!")
elif users_choice == scissors and computers_choice == rock:
  print("You lose!")
elif users_choice == scissors and computers_choice == paper:
  print("You win!")