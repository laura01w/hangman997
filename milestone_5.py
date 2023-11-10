
import random

# create Hangman class
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        #initialise 'word' attribute by picking randomly from list
        self.word = random.choice(self.word_list)
        #initialise word_guessed attribute with '_' for each letter not yet guessed
        self.word_guessed = ['_' for  _ in self.word]
        #initialise num_letters attribute for number of unique letters in word
        self.num_letters = len(set(self.word))
        #initialise list_of_guesses attribute as an empty list
        self.list_of_guesses = []

#create check_guess method in Hangman class
    def check_guess(self, guess):
        guess = guess.lower() #convert to lower class
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")

        #replace '_' with the correct guessed letters
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

#create ask_for_input method in Hangman class
    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Guess a letter: ")
            guess = guess.lower()
            
            if not len(guess) == 1 and guess.isalpha():
                print("Invalid input. Please enter a single alphabetical character.") # loop continues until valid input
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess) #calls check_guess method
                self.list_of_guesses.append(guess) #add the guess to the list of guesses

# create play_game function
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)

    while True:
        if game.num_lives <= 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulation. You won the game!')
            break
                  
#test the game
random_word_list = ['sofa', 'table', 'chair','phone']
play_game(random_word_list)



