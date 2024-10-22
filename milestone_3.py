import random

# List of favourite fruits
favorite_fruits = ['banana', 'strawberry', 'mango', 'watermelon', 'grapes']

# Function to choose a random word from favourite fruits
def select_random_word():
    return random.choice(favorite_fruits)

# Function to check if guessed letter is in the word
def check_guess(guess, secret_word):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Function to ask for user input and validate the guess
def ask_for_input(secret_word):
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess, secret_word)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Main function to start the game
def start_game():
    secret_word = select_random_word()
    print("A word has been chosen from the list of favourite fruits.")
    ask_for_input(secret_word)

# Start the game
if __name__ == "__main__":
    start_game()