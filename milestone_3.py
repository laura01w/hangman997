# create while loop and set to True (so stays as loop)
# ask user to guess a letter
# assign input to variable

import random
secret_word = 'apple'

# create functions to organise up code

# define function to check guess is in word
def check_guess(guess):
    guess = guess.lower() #convert to lower case
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

#define function to ask for input
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        guess = guess.lower()
        
        if len(guess) == 1 and guess.isalpha():
            break  # Break the loop if the guess is a single alphabetical character
        else:
            print("Invalid input. Please enter a single alphabetical character.") # loop continues until valid input
            
        check_guess(guess) #call check_guess function

ask_for_input()



