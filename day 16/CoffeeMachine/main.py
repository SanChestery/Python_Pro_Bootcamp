from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

not_finished = True
while not_finished:

    ''' Define new order Object '''
    order = Menu()

    ''' Choose Item '''
    items = order.get_items()
    choice = input(f"What would you like? {items}?: ").lower()
    if choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif choice == "off":
        not_finished = False
    else:
        drink = order.find_drink(choice)
        if drink == None:
            continue

        ''' Check if the resources are enough '''
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)

