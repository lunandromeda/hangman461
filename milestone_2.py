import random

# Task 1: Create list of favourite fruits
def get_favourite_fruits():
    return ['banana', 'strawberry', 'mango', 'watermelon', 'grapes']

# Task 2: Select a random fruit from the list
def choose_random_fruit(fruit_list):
    return random.choice(fruit_list)

# Task 3: Prompt user to guess a letter
def get_user_guess():
    guess = input("Guess a letter: ")
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Invalid input. Please enter a single letter: ")  
    return guess

# Main function
if __name__ == "__main__":
    #Task 1
    fruit_list = get_favourite_fruits()
    print("Favourite fruits: ", fruit_list)
    #Task 2
    random_fruit = choose_random_fruit(fruit_list)
    print("Random fruit selected: ", random_fruit)
    #Task 3
    user_guess = get_user_guess()
    print(f"You entered: {user_guess}")