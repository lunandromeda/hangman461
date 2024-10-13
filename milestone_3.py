# Define the secret word
secret_word = 'apple'

# Function to check if the guessed letter is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Function to ask for user input and validate the guess
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Call the function to start the process
ask_for_input()