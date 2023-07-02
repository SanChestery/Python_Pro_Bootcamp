from art import logo
import random
from os import system

print(logo)
print("I'm thinking of a number between 1 and 100.")

def check(num, guess):
    if num == guess:
       print(f"You got it! The answer was {guess}.")
       return True
    elif num > guess:
        print("Too low.\nGuess again.")
        return False
    elif num < guess:
        print("Too high.\nGuess again,") 
        return False

attempts = 0
num = random.randint(1, 100)
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
    if difficulty == "easy" or difficulty == "hard":
        break
    else:
        print("Input not valid. Type 'easy' or 'hard'!")
        system('sleep 2')
        system('cls')

print(f"Psssst, the correct answer is {num}")

if difficulty == "easy": 
    attempts = 10
else: 
    attempts = 5

for att in range(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if check(num, guess):
        break
    attempts -= 1

if attempts == 0: 
    print("You've run out of guesses, you lose.")