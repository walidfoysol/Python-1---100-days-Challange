

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    choice = input(f"What would you like? ({menu.get_items()}):")
    if choice == "off":
        print("Turning off the coffee machine.")
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    menu_item = menu.find_drink(choice)
    if not menu_item or not coffee_maker.is_resource_sufficient(menu_item):
        continue
    if money_machine.make_payment(menu_item.cost):
        coffee_maker.make_coffee(menu_item)
