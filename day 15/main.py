from os import system
from data import MENU, resources

def report(res): 
    print(f"Water: {res['water']}ml\nMilk: {res['milk']}ml\nCoffee: {res['coffee']}g\nMoney: ${res['money']}")

def check_resources(res, order):
    if res['water'] < order['water']:
        print("Sorry there is not enough Water.")
        return 1
    elif res['milk'] < order['milk']:
        print("Sorry there is not enough Milk.")
        return 1
    elif res['coffee'] < order['coffee']:
        print("Sorry there is not enough Coffee.")
        return 1
    else:
        return 0

state_resources = resources
state_resources['money'] = 0

not_finished = True
while not_finished:
    in_wrong = True
    while in_wrong:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            in_wrong = False
            not_finished = False
            break
        elif choice == "report":
            report(state_resources)
            in_wrong = False
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            check_resources(state_resources, MENU[choice]['ingredients'])
            in_wrong = False
        else:
            print(f"Sorry, {choice} is not a valid input.")
