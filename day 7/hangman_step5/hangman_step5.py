#Step 5

import random
import hangman_art
import hangman_words
from os import system

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    system('cls')

    if guess in guesses:
        print(f"You already tried '{guess}'!")
    else:
        guesses += guess

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"'{guess}' is not part of the word!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was: {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])