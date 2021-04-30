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
#print(words)


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

    elif len(word) == 6 or len(word) == 7:
        medium_words.append(word)

    elif len(word) >= 8:
        long_words.append(word)

    else: 
        pass

# class Game:
    # def choose_difficulty():
    #     difficulty_choice = [easy, medium, hard]
    #     input()
    #     return choice

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

mystery_word = pick_mystery_word()

print(mystery_word)
pick_a_word()
print(split(mystery_word))
# class Player:
#     def round():
#         pass
#     def guess():
#         guesses = ("8")
#         while guesses < 8:
#         # while answer != True: #for max 8 guesses
#             if guess == correct_letter:
#         #         print()#display blank spaces other than correct letter guessed and - 1 guess
#             elif guess != correct_letter:
#         #         print("Wrong. Guess Again") #ask for input and - one guess
#             elif guess == repeat_guess:
#         #         print("Letter guessed. Go again") and - one guess
#             elif guess == too_many_letters:
#         #         print("Too many letters") and - one guess
#         else:
#         #         print("Maximum guesses exceded. Sorry, try again.") 

# def win_or_lose():
#     reveal_the_answer
#     input("do you want to play again")
#     #if yes run new game

    
# def wheel_of_fortune():
#     intro()
#     Game.pick_a_word()

# wheel_of_fortune()






