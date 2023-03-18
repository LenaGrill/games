
import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for letter in chosen_word: # for each letter in the chosen_word, a blank is added to "display"
  display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower() # asks the user to guess a letter, makes it lower case and assigns it to a variable

    for position in range(word_length):  #Check guessed letter
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess: 
          if display[position] == "_":
            display[position] = letter
          elif display[position] == guess:
            print(f"The chosen letter is {guess}, you have chosen this letter before.")

    
    if guess not in chosen_word: # Check if user is wrong and if yes, reduce number of lives
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}.")

    print(f"{' '.join(display)}") # Joins all the items in the list and turns it into a String

    if "_" not in display: # Check if user has got all letters
        end_of_game = True
        print("You win.")

    print(stages[lives])

