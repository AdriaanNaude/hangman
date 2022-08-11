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

#point = 0
guess = 0



def r_expresion(user_input, word):
    regex = rf"^{user_input}$"

    if re.match(regex, word):
        print("Match")
    else:
       print("No match")

while guess < 10:
    user_stdin = input("Your")
    
    r_expresion(user_stdin, word)

"""
def resultate(point, guess):
    if guess == 6:
        print("guesses done")
    if point == word_length:
        print("You win " + point + " " + word)

def keuse():
    y_n = input(">Do you want to retry\n[y/n]: ")
    if y_n == "y" | y_n == "Y":
        loop()
    else:
        print("goodbye")
"""
