import random
from hangman_art import stages, logo
from hangman_words import word_list
chosen_word = random.choice(word_list)
print(logo)
print(chosen_word)
display = []
lives = 6
end_of_game = False
for x in range(len(chosen_word)):
    display.append("_")
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        if guess not in display:
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
            print(f"{''.join(display)}")
        else:
            print(f"You have already guessed {guess}")
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        print(f"{''.join(display)}")
        print(stages[lives])
        lives -= 1
    if display.count("_") == 0:
        end_of_game = True
        print("You won!")
    elif lives == -1:
        print("You lost!")
        end_of_game = True
