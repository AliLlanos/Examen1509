 import random

class GetRandomWord:
    def __init__(self):
        self.words = ["pepe", "casa", "padre", "marido", "mujer", "hombre"]

    def get_word(self):
        return random.choice(self.words)


class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed = []

    def guess(self, letter):
        if letter in self.word:
            self.guessed.append(letter)
            print("You guessed the letter!")
        else:
            print("You guessed wrong!")
            if letter in self.guessed:
                print("You already guessed that letter")

    def get_status(self):
        print("Guess the word:")
        for letter in self.word:
            if letter in self.guessed:
                print(letter, end="")
            else:
                print("_", end="")
        print('\n')

    def check_if_player_won(self):
        return all(letter in self.guessed for letter in self.word)



class PlayGame:
    def __init__(self):
        self.word = GetRandomWord().get_word()
        self.hanged = Hangman(self.word)

    def play(self):
        while True:
            self.hanged.get_status()
            letter = input("adivina una letra: ")
            self.hanged.guess(letter)
            if self.hanged.check_if_player_won():
                print("You won!")
                break



if __name__== "__main__":
    game = PlayGame()
    game.play()

