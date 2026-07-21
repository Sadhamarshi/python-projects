import random
from words import words


class Hangman:

    def __init__(self):
        self.word = random.choice(words)
        self.guessed_letters = []
        self.attempts = 6

    def display_word(self):
        display = ""

        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print(display)

    def guess_letter(self, letter):

        if letter in self.guessed_letters:
            print("Letter already guessed.")
            return

        self.guessed_letters.append(letter)

        if letter not in self.word:
            self.attempts -= 1
            print("Wrong Guess!")

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def play(self):

        print("===== HANGMAN GAME =====")

        while self.attempts > 0:

            self.display_word()

            print(f"Attempts Left: {self.attempts}")

            guess = input("Guess a Letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Enter a single alphabet.\n")
                continue

            self.guess_letter(guess)

            if self.is_won():
                print(f"\nCongratulations! The word was '{self.word}'.")
                return

            print()

        print(f"You Lost! The word was '{self.word}'.")