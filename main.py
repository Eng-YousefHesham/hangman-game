from word_bank import WordBank
from hangman import Hangman
from game_history import GameHistory


if __name__ == "__main__":
    bank = WordBank()
    history = GameHistory()

    play_again = "yes"
    while play_again == "yes":
        word = bank.choose_random_word()
        game = Hangman(word)

        while not game.is_won() and not game.is_lost():
            print(game.get_display_word())
            print("Attempts remaining:", game.attempts_remaining)
            print("Guessed letters:", game.get_guessed_letters_display())

            letter = input("Guess a letter: ").lower()
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a one letter character")
                continue
            game.guess(letter)

        if game.is_won():
            print("You won! The word was:", game.word)
        else:
            print("You lost! The word was:", game.word)

        history.add_record(game.word, game.is_won(), game.attempts_remaining)

        play_again = input("Play again? (yes/no): ").lower()

    print("Thanks for playing!")
    history.show_summary()