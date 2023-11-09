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

# ask user for an input
# use input() to ask for a single letter
# assign input to variable called guess

guess = input("Please enter a single letter: ")



