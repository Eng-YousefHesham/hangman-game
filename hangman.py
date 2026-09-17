class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.attempts_remaining = 6

    def guess(self, letter):
        self.guessed_letters.append(letter)
        if letter not in self.word:
            self.attempts_remaining -= 1

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def is_lost(self):
        return self.attempts_remaining <= 0

    def get_display_word(self):
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display

    def get_guessed_letters_display(self):
        display = ""
        for letter in self.guessed_letters:
            display += letter + ", "
        return display