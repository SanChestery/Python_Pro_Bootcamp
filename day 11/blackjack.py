import random
from os import system
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def show_cards(score_player, cards_player, cards_computer):

    for card in cards_player:
        score_player += card
    print(f"Your cards: {cards_player}, current score: {score_player}")
    print(f"Computer's first card: {cards_computer[0]}")

def check_win(score_player, cards_player, score_computer, cards_computer):
    print(f"Your final cards: {cards_player}, final score: {score_player}")
    print(f"Computer's final cards: {cards_computer}, Computer's score: {score_computer}")
    if score_player == 21 or (score_player < 21 and score_player > score_computer):
        print("You won!")
    elif score_player == score_computer:
        print("Draw!")
    else:
        print("Computer wins!")

def play():
    cards_player = []
    cards_computer = []
    score_player = 0
    score_computer = 0

    print(logo)

    cards_player.append(deal_card())
    cards_player.append(deal_card())
    cards_computer.append(deal_card())
    cards_computer.append(deal_card())
    

    for card in cards_computer:
        score_computer += card
    
    while score_computer < 17:
        new_card = deal_card()
        cards_computer.append(new_card)
        score_computer += new_card
        

    cards_not_finished = True
    while cards_not_finished:
        show_cards(score_player, cards_player, cards_computer)  
        want_another_card = input("Do you want to take another card? Type 'y' or 'n': ")
        if want_another_card == "y":
            cards_player.append(deal_card())
        else:
            check_win(score_player, cards_player, score_computer, cards_computer)
            cards_not_finished = False
              


not_finished = True
while not_finished:
    another_play = input("\nDo you want to play a game of Black Jack? Type 'y' or 'n': ")
    if another_play == "y":
        cards_player = []
        cards_computer = []
        cards_not_finished = True
        system('cls')
        play()
    elif another_play == "n":
        not_finished = False
        print("Bye!")
    else:
        system('cls')
        print(f"Input '{another_play}' is not valid!")
        
