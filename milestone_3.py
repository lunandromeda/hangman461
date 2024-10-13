secret_word = 'apple' # The word that needs to be guessed

while True: # Continuous Loop
    # Ask user to guess a letter
    guess = input("Guess a letter: ")

    # Check if the input is a single letter
    if len(guess) == 1 and guess.isalpha():
        # If the input is a single letter, print the letter
        break
    else:
        # If the input is not a single letter, print an error message
        print("Invalid letter. Please, enter a single alphabetical character.")

# The loop will continue to run until the user enters a single letter
print(f"You enetered a valid letter: {guess}")

# Check if the guessed letter is in the secret word
if guess in secret_word:
    # If true, print a success message
    print(f"Good guess! {guess} is in the word.")
else:
    # If false, print a failure message
    print(f"Sorry, {guess} is not in the word. Try again.")