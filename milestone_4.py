import random

# Defining class
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))  # Unique letters to be guessed
        self.list_of_guesses = []

    # Method to check if guessed letter is in the word
    def check_guess(self, guess):
        guess = guess.lower()  # Convert guess to lowercaseb
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # For loop to replace underscores with correct guessed letter
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess  # Replace "_" with guessed letter
            print(f"Current word: {''.join(self.word_guessed)}")
            # Reduce the number of unique letters remaining
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1  # Decrease life for evry incorrect guess
            print(f"You have number of lives left: {self.num_lives}")
    
    # Method to ask for input from user
    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")

            # Check if guess is a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            # Check if the letter was already guessed
            elif guess in self.list_of_guesses:
                print("You have already tried that letter. Try again.")
            # Valid guess made
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)  # Append guess to list of guesses
                break  # Exit the loop after a valid guess

# Trying it out
if __name__ == "__main__":
    word_list = ['banana', 'strawberry', 'mango', 'watermelon', 'grapes']
    game = Hangman(word_list)
    
    print(f"The word is: {''.join(game.word_guessed)}")
    game.ask_for_input()

