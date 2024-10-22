import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))  # Unique letters to be guessed
        self.list_of_guesses = []

    # Step 1: Method to check if the guessed letter is in word
    def check_guess(self, guess):
        guess = guess.lower()  # Converts the guess to lowercase
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1  # Decrease life for every incorrect guess
            print(f"Number of lives left: {self.num_lives}")
    
    # Step 2: Method to ask for input from the user
    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")

            # Check if guess is a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            # Check if the letter was already guessed
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            # Valid guess
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)  # Appends guess to the list of guesses
                break  # Exit the loop after a valid guess is made

# Trying it out
if __name__ == "__main__":
    word_list = ['banana', 'strawberry', 'mango', 'watermelon', 'grapes']
    game = Hangman(word_list)
    
    print(f"The word is: {''.join(game.word_guessed)}")
    game.ask_for_input()
