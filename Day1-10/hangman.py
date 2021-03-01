# Basic Algorithm....time to make it shiny
# word = "happy"
# len_word = len(word)
# count = len_word
# blank_word = "_" * len_word
# print(blank_word)
# while blank_word.count("_") != 0 and count != 0:
#     letter = input("Give a letter: ").lower()
#     if letter in word:
#         position = word.index(letter)
#         word = word[:position] + "_" + word[position+1:]
#         blank_word = blank_word[:position] + letter + blank_word[position+1:]
#         print(blank_word)
#         count -= 1


import random
words_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(words_list)
print(chosen_word)
guess = input("Guess a letter: ").lower()
if guess in chosen_word:
    print("yes")
