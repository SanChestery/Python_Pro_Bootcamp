from art import logo
from os import system

def new_bidder():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids[name] = bid

def winner():
    highest_bid = 0
    winner_name = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner_name = bidder

    print(f"The winner is {winner_name} with a bid of ${highest_bid}")

bids = {}
finished = False

print(logo)
print("Welcome to the secret auction program.")
while not finished:
    new_bidder()

    other = input("Are there other bidders? Type 'yes' or 'no': ").lower()
    system('cls')
    if other == "no":
        winner()
        finished = True