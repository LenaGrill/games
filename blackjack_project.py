############### Blackjack Project #####################

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from blackjack_logo import logo
from random import randrange

def card_choice(): 
  """ this function randomly pics a card from cards """
  x = randrange(0, max)
  chosen_card = cards[x]
  return chosen_card

def deal_card(a, b):
  """ uses card_choice to pic a new card and adds cards and score to previous results """
  new_card = card_choice()
  a += new_card
  b.append(new_card)
  return new_card, a, b

def final_print(current_cards, current_score, computer_cards, computer_score):
  """shows final cards and points for player and computer"""
  print(f"Your final hand: {current_cards}, final score: ", current_score)
  print(f"Computer's final hand: {computer_cards}, computer's final score: ", computer_score)

def handout_player():
  """ gives out first two cards player """
  card1 = card_choice()
  card2 = card_choice()
  current_score = card1 + card2
  current_cards = [card1, card2]
  print(f"Your cards: {current_cards}, current score: ", current_score)
  return current_score, current_cards

def handout_computer():
  """ gives out first two cards computer """
  computer_card1 = card_choice()
  computer_card2 = card_choice()
  computer_score = computer_card1 + computer_card2
  computer_cards = [computer_card1, computer_card2]
  print(f"Computer's first card: {computer_card1}")
  return computer_score, computer_cards

def check_ace(a, b):
  """checks if ace is present. If yes and when score is above 21, 11 is replaced by 1"""
  new_cards = []
  for card in a:
    if card == 11 and b > 21:
      card = 1
    else:
      card = card
    new_cards.append(card)
  return new_cards

def blackjack(player_won, computer_won):
  """this function is the actual game and returns nr of games won + 1"""
  current_score, current_cards = handout_player()
  current_cards = check_ace(current_cards, current_score)
  computer_score, computer_cards = handout_computer()
  computer_cards = check_ace(computer_cards, computer_score)
  
  # detects blackjack:
  if computer_score == 21:
    print("Opponent has Black Jack! You lose!")
    computer_won += 1
    return player_won, computer_won
  elif current_score == 21:
    print("Black Jack! You win!")
    player_won += 1
    return player_won, computer_won
  
  answer = "y"
  while answer == "y":
    answer = input("Type 'y' to get another card, type 'n' to pass.")
    if answer == "y":
      new_card, current_score, current_cards = deal_card(current_score, current_cards)
      print(f"Your new card is {new_card}. Current score: ", current_score)
      if current_score > 21:
        final_print(current_cards, current_score, computer_cards, computer_score)
        print("You went over, you lose!")
        computer_won += 1
        answer = "n"    
    elif answer == "n":
      while computer_score < 16:
        new_card, computer_score, computer_cards = deal_card(computer_score, computer_cards)
      print(f"computer's score: {computer_score}")
      if computer_score > 21 and current_score <= 21:
        final_print(current_cards, current_score, computer_cards, computer_score)
        print("Opponent went over, you win!")
        player_won += 1
      elif computer_score <= 21 and computer_score > current_score:
        final_print(current_cards, current_score, computer_cards, computer_score)
        print("You lose!")
        computer_won += 1
      elif computer_score <= 21 and computer_score < current_score:
        final_print(current_cards, current_score, computer_cards, computer_score)
        print("You win!")
        player_won += 1
      elif computer_score <= 21 and computer_score == current_score:
        final_print(current_cards, current_score, computer_cards, computer_score)
        print("Draw!")
  return player_won, computer_won

# starts the blackjack game by asking for a game and ends it by returning number of winnings
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
max = len(cards) # returns the number of items in cards
game_on = "y"
computer_won = 0
player_won = 0
while game_on == "y":
  game_on = input("\n Do you want to play a game of Black Jack? Type 'y' or 'n'") 
  if game_on == "y":
    player_won, computer_won = blackjack(player_won, computer_won)
  else:
    print(f"Player won {player_won} times")
    print(f"Opponent won {computer_won} times")
    print("Good Bye!")
