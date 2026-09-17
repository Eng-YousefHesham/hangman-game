import random


class WordBank:
    def __init__(self):
        self.words = ["algorithm", "bytecode", "recursion", "debugger", "chocolate", "pyramid", "mountain", "umbrella", "elephant", "volcano", "guitar"]

    def choose_random_word(self):
        return random.choice(self.words)