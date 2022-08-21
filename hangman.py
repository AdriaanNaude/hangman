import re
import random

word_list = {
    1:"animal",
    2:"read",
    3:"man",
    4:"fan"
}

word = word_list[random.randrange(1,5)]
word_length = len(word)

print("The word length is: " + str(word_length))

kans = 0

def r_expresion(user_input, word):
    regex = rf"^{word}$"

    if re.match(regex, user_input):
        print("Match")
    else:
       print("No match")
        

def loop(x):
    while x < 10:
        user_init = input("Your guess: ")
        x+=1
        if user_init == "q":
            ptint("Exiting")
            break
        r_expresion(user_init, word)

loop(kans)
