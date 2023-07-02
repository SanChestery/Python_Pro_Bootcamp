from art import logo, vs
from game_data import data
from os import system
import random

not_finished = True
counter = 0

comparer_A = random.choice(data)
comparer_same = True
while comparer_same:
    comparer_B = random.choice(data)
    if comparer_A != comparer_B:
        comparer_same = False

system('cls')
print(logo)

while not_finished:
    print(f"Compare A: {comparer_A['name']}, a {comparer_A['description']}, from {comparer_A['country']}.")
    print(vs)
    print(f"Against B: {comparer_B['name']}, a {comparer_B['description']}, from {comparer_B['country']}.")

    not_char = True
    while not_char:
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer == "a":
            not_char = False
            answer = comparer_A

        elif answer == "b":
            not_char = False
            answer = comparer_B

        else:
            print(f"\n{answer.upper()} is not valid!")

    if comparer_A['follower_count'] > comparer_B['follower_count']:
        more = comparer_A
    elif comparer_A['follower_count'] < comparer_B['follower_count']:
        more = comparer_B
    else: 
        print("They are the same!")

    if answer == more: 
        counter += 1
        system('cls')
        print(logo)
        print(f"You are right! Current score: {counter}.")
        comparer_A = more
        comparer_same = True
        while comparer_same:
            comparer_B = random.choice(data)
            if comparer_A != comparer_B:
                comparer_same = False
    else: 
        print(f"Sorry, that's wrong. Final score: {counter}")
        not_finished = False


