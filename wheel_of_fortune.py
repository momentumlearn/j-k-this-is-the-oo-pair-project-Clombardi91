import random

# create wheel of fortune game
# computer will randomly choose from a [] of words/must use .lower
# display number of letters in word for user
# for players turn, 1 guess per turn 
# create while loop for player's turn 
# if letter is guessed correctly, print letter
# elif, print "Wrong. Guess again"

fileObject = open("words.txt", "r")
lines = fileObject.readlines()
words = [line[:-1] for line in lines]



def intro():
    print()
    line ="""THIS IS WHEEL OF FORTUNE!\n 
            You will have a chance to guess a random word.\n
            Start by guessing a vowel and then a consonant.\n
            You will be given 8 chances to guess the word correctly.\n
            The letter guessed correctly will display in the blank spaces for the word.\n
            Good luck and have fun!\n"""
    print(line)


short_words = []
medium_words = []
long_words = []

for word in words:
    if len(word) == 4 or len(word) == 5:
        short_words.append(word)
        # return short_words
    elif len(word) == 6 or len(word) == 7:
        medium_words.append(word)
        # return medium_words
    elif len(word) >= 8:
        long_words.append(word)
        # return long_words
    else: 
        pass

def difficulty_choice():
    user_choice = input("Choose a difficutly:  ENTER  1 for Easy, 2 for Normal, or 3 for Challenging:  ")
    return user_choice

def game_mode_pick(difficulty_choice):
    if difficulty_choice == "1":
        return short_words
    elif difficulty_choice == "2":
        return medium_words
    elif difficulty_choice == "3":
        return long_words

    else: 
        input("Choose a difficutly:  ENTER  1 for Easy, 2 for Normal, or 3 for Challenging:  ")

def pick_a_word():
        word_bank = []
        print(len(random.choice(medium_words)))
        # return answer
        # print(answer)

def pick_mystery_word():
        word_bank = medium_words
        return random.choice(word_bank)

def split(word):
    return list(word)

choice = difficulty_choice()

mystery_word = pick_mystery_word()

intro

print(mystery_word)
pick_a_word()
print(split(mystery_word))










