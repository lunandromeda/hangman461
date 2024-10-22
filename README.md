# Hangman Game by Lauren Salmon

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
  - [Milestone 2](#milestone-2)
  - [Milestone 3](#milestone-3)
  - [Milestone 4](#milestone-4)
- [File Structure of the Project](#file-structure-of-the-project)
- [License](#license)

## Description

# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

- In **milestone 2**, we started with a basic game where the user guesses letters from a fixed list of fruits.
- In **milestone 3**, the game evolved into a Hangman game where a word is chosen, and the user guesses letters until they reveal the whole word or make too many incorrect guesses.
- In **milestone 4**, the game progresses further by introducing the concept of a class-based structure. 

The aim of the project is to reinforce Python concepts, such as:
- Loops (`while`, `for`)
- Input validation (`input()`, `isalpha()`)
- String manipulation and comparison
- Functions and modular code
- Randomised selection of elements

### What I Learned
- How to break down a problem into smaller, manageable functions.
- Validating user input to ensure correct behavior.
- Handling string operations in Python.
- Building a basic game flow with user interaction and error handling.

## Installation

### Requirements:
- **Python 3.x**

To run the project locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/lunandromeda/hangman461.git
```
2. Navigate into the project directory:
```bash
cd hangman461
```
3. Run the milestone scripts:
```bash
python milestone_2.py
```
OR
```bash
python milestone_3.py
```
OR
```bash
python milestone_4.py
```

## Usage

### Milestone 2
In **milestone 2**, the user is prompted to guess a letter from a randomly chosen word from a list of fruits. The game checks whether the guessed letter is part of the word and provides feedback.

**Example Output:**
```
Please enter a single letter: a 
Good guess! a is in the word.
```

### Milestone 3
In **milestone 3**, the game simulates the Hangman game. A secret word is predefined, and the user has to guess letters one by one. The game checks if the guessed letter is correct and continues until the word is guessed or too many incorrect guesses are made.

The game has the following features:
- It validates the user's input (must be a single alphabetical character).
- It checks if the guessed letter is in the secret word.
- The game will continue prompting for guesses until the user enters a valid guess.

**Example Output:**
```
Guess a letter: a 
Good guess! a is in the word.

Guess a letter: z Sorry, z is not in the word. Try again.
```

### Milestone 4
In **milestone 4**, the game progresses further by introducing the concept of a class-based structure. The Hangman game is now implemented using a Python class, encapsulating the logic and state within an object-oriented framework. The user must continue to guess letters but the structure is more maintainable and scalable.

Features:
- The game is implemented within a Hangman class.
- The game randomly selects a word from a predefined word list.
- The word is represented by underscores (_), which are replaced by correctly guessed letters.
- The number of lives is reduced when the user makes an incorrect guess.
- The game tracks and handles repeated guesses.
- If the guess is correct, the underscores are replaced with the guessed letter at the correct positions.
- The game ends when the word is completely guessed or when the user runs out of 'lives'.

**Example Output:**
```
The word is: _ _ _ _ _ _
Please guess a letter: a
Good guess! a is in the word.
Current word: _a_a_a
```

```
Please guess a letter: z
Sorry, z is not in the word.
You have 4 lives left.
```

## File Structure of the Project
```
├── milestone_2.py  # Basic fruit guessing game 
├── milestone_3.py  # Hangman game with validation 
├── milestone_4.py  # Hangman game with class-based structure
└── README.md       # Project documentation
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
