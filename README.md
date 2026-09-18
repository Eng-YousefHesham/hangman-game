# Hangman Game

A text based Hangman game built in Python using Object-Oriented Programming. The player guesses letters to reveal a hidden word before running out of attempts, with session history tracking across multiple rounds.

## Features

- Classic Hangman gameplay with a 6-attempt limit
- Random word selection from a built-in word list
- Input validation (rejects numbers, symbols, and multi-character input)
- Case-insensitive letter guessing
- Tracks and displays already-guessed letters each turn
- Play multiple rounds in one session
- End-of-session game history summary (word, result, attempts remaining per round)

## Concepts Demonstrated

- Object-Oriented Programming (classes, objects, `self`, constructors)
- Separation of concerns across multiple classes and files
- Control flow (`while` loops, `if/elif/else`)
- Lists, dictionaries, and string manipulation
- List comprehensions and the `all()` function
- f-strings and the `enumerate()` function
- Basic input validation and error handling

## Project Structure
hangman-game/
├── word_bank.py # WordBank class - stores and selects words
├── hangman.py # Hangman class - core game logic
├── game_history.py # GameHistory class - tracks session results
├── main.py # Entry point - runs the game loop


## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository: "https://github.com/Eng-YousefHesham/hangman-game.git"
3. Navigate into the project folder and run:


## Example Gameplay
Attempts remaining: 6
Guessed letters:
Guess a letter: g

_ _ _ _ _ _ g
Attempts remaining: 6
Guessed letters: g,
Guess a letter: t
...


## Author

Yousef Hesham
linkedin: "linkedin.com/in/yousef-hesham-60a50b27b/?skipRedirect=true"












