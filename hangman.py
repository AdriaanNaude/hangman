import re
import random

word_list = {
    1:"animal",
    2:"read",
    3:"man"
}

word = word_list[random.randrange(1,4)]
word_length = len(word)

print("The word length is: " + str(word_length))

point = 0
guess = 0


def loop(user_input, word):
    while guess <= 6:

    r_expresion(user_input, word)


def r_expresion(user_input, word):
    regex = rf"{user_input}"

    if re.search(regex, word):
        return true
    else:
        return false

def keuse(point, guess):
    if guess == 6:
        print("guesses done")
    if point == word_length:
        print("You win " + point + " " + word)

