from os import system
from data import MENU, resources

def report(res): 
    print(f"Water: {res['water']}ml\nMilk: {res['milk']}ml\nCoffee: {res['coffee']}g\nMoney: ${res['money']}")

def check_resources(res, order):
    if res['water'] == 0 or res['milk'] == 0 or res['coffee'] == 0:
        print("Please come later, we need to refill.")
        exit()    
    elif res['water'] < order['water']:
        print("Sorry there is not enough Water.")
        return False
    elif res['milk'] < order['milk']:
        print("Sorry there is not enough Milk.")
        return False
    elif res['coffee'] < order['coffee']:
        print("Sorry there is not enough Coffee.")
        return False
    else:
        return True

def change(order):
    # Insert all coins
    print("Please insert coins.")
    quaters = int(input("how many quaters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    # Calculate 
    res = quaters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if res == order['cost']:
        print("Thank you that's perfect")
        return True
    elif res > order['cost']:
        print(f"Here is ${round((res - order['cost']), 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coff(res, order):
    res['water'] -= order['ingredients']['water']
    res['milk'] -= order['ingredients']['milk']
    res['coffee'] -= order['ingredients']['coffee']
    res['money'] += order['cost']


system('cls')
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
            if check_resources(state_resources, MENU[choice]['ingredients']):  
                if change(MENU[choice]):
                    make_coff(state_resources, MENU[choice])
                    print(f"Here is your {choice}. Enjoy!")
                
            in_wrong = False
        else:
            print(f"Sorry, {choice} is not a valid input.")
