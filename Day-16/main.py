from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

item = []
# call list of items for user

def get_item():
    global item
    item = input(menu.get_items())
    item.lower()


if item == "report":
    coffeemaker.report()
    money_machine.report()


# collect drink object
drink = menu.find_drink(item)

#check sufficient conditions
if coffeemaker.is_resource_sufficient(drink) == False:
    print("Please pick another item")


if money_machine.make_payment(drink.cost) ==  False:
    print("not enough coins, money refunded")

# make drink
coffeemaker.make_coffee(drink)



