# Task 1
favourite_fruits = ['banana', 'strawberry', 'mango', 'watermelon', 'grapes']
word_list = favourite_fruits
print(word_list)

# Task 2
import random

word = random.choice(word_list)
print(word)

# Task 3
guess = input("Please enter a single letter: ")
while len(guess) != 1 or not guess.isalpha():
          guess = input("Invalid input. Please enter a single letter: ")

print(f"You entered: {guess}")