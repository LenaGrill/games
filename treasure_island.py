print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

import time

def print_slow(str): # this function is to slow down the printing time, so that it looks like written on a typewriter
    for letter in str:
        print(letter, end = '', flush = True)
        time.sleep(3./30)

answer = input("Are you ready?")
answer = answer.lower()

if answer == "yes" or answer =="y" or answer == "":
  print("Let's continue:")
else:
  print("Then try again later.")
  exit()
  
print_slow("You wake up lying on a sandy beach. You are stranded on a deserted island. From the beach, there is a small path leading into the woods. ")
print_slow("You follow the path for several hundred meters until you reach a fork. ")
print_slow("Right hand, the path continues and is getting even wider. On the left hand, there is an animal track which leads into the thicket. Which way do you want to go? \n")
left_or_right = input("Do you choose left or right? \n").lower()

if left_or_right == "left":
  print_slow("You walk along a hidden path and you arrive at a river. \n")
  swim_or_wait = input("Do you want to swim or wait for a ferry? Write \"swim\" or \"wait\" \n").lower()
else:
  print_slow("You just fell into a hole. Game over!") 
  exit()

if swim_or_wait == "wait":
  print_slow("You stand around and wait for a while. After some time, a boat arrives and takes you to the other side. Continuing your journey, you stand suddenly in front of a house that appeared out of nowhere. It has three colored doors. ")
  print_slow("A yellow, shiny door invites you to enter. Do you dare? A red door dangorously reminds you of hell. Could this be the right way to go? A rather plain, blue door is also there. Could be something wrong with the unremarkable? \n")
  
  door_choice = input("Do you choose the yellow, red or blue door? \n").lower()
else:
  print_slow("You start swimming in the cold water. You get attacked by a Piranha. Game over!")
  exit()

if door_choice == "red":
  print_slow("You were right to be alarmed by the color. You just walked into an oven and you are burnt by fire. Game over!")
  
elif door_choice == "yellow":
  print_slow("You just found the treasure! Congratulations! You win!")

elif door_choice == "blue":
  print_slow("You enter a dark room. You don't see anything but hear scary noises. You are attacked and eaten by beasts. Game over!")
  
else:
  print_slow("Game over!")
    