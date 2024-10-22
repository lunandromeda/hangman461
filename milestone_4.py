import random

# Step 1: Define the Hangman class
class Hangman:
# Step 2: Define the __init__ method
    def __init__(self, word_list, num_lives=5):
        # Step 3: Initialise the attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))  # Unique letters to be guessed
        self.list_of_guesses = []

# Trying it out
if __name__ == "__main__":
    word_list = ['banana', 'strawberry', 'mango', 'watermelon', 'grapes']
    game = Hangman(word_list)
    
    print(f"Word to guess: {game.word}")
    print(f"Word guessed so far: {game.word_guessed}")
    print(f"Number of unique letters: {game.num_letters}")
    print(f"Number of lives: {game.num_lives}")
    print(f"List of guesses: {game.list_of_guesses}")
