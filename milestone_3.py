while True: # Continuous Loop
    # Step 2: Ask user to guess a letter
    guess = input("Guess a letter: ")

    # Step 3: Check if the input is a single letter
    if len(guess) == 1 and guess.isalpha():
        # Step 4: If the input is a single letter, print the letter
        break
    else:
        #Step 5: If the input is not a single letter, print an error message
        print("Invalid letter. Please, enter a single alphabetical character.")

# The loop will continue to run until the user enters a single letter
print(f"You enetered a valid letter: {guess}")