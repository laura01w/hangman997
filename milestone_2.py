import random

# create a list containing 5 fruits
fruits = ['kiwi','lemon','blueberry','mango','cherry']

# assign fruit list to new variable
word_list = fruits
print(word_list)

# choose a random word from the list
# create the random.choice method 
# and pass word_list variable into the choice method
word = random.choice(word_list)
print("Randomly selected fruit:", word)

# ask user for an input of single letter
# assign input to variable called guess
guess = input("Please enter a single letter: ")

# create conditional checks for the input
# use if statement
# .isalpha to check its alphabetical character
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# initialise new git repo
# stage, commit and push changes to GitHub repo


