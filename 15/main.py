MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(choices):
    global resources
    for element in MENU[choices]['ingredients']:
        if resources[element] < MENU[choices]['ingredients'][element]:
            print(f"Sorry, there is not enough {element}")
            return False
    return True

def resource_depletion(choices):
    global resources
    for element in MENU[choices]['ingredients']:
        resources[element] -= MENU[choices]['ingredients'][element]


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        print("Please insert coins.")
        given = 0.00
        assurance = check_resources(choice)
        if not assurance:
            continue

        given += int(input("How many quarters?: ")) * 0.25
        given += int(input("How many dimes?: ")) * 0.1
        given += int(input("How many nickle?: ")) * 0.05
        given += int(input("How many pennies?: ")) * 0.01
        given = given - MENU[choice]["cost"]

        if given < 0:
            print("Sorry, that's not enough money. Money refunded.")
            given = 0

        profit += MENU[choice]["cost"]
        resource_depletion(choice)

        if given > 0:
            print(f"Here is {given:.2f}$ in change")
            print(f"Here is your {choice} ☕ Enjoy!")

    elif choice == "report":
        print(f"Water = {resources['water']} \nMilk = {resources['milk']} \nCoffee = {resources['coffee']} \nMoney = {profit}")
    elif choice == "off":
        print("turning off the coffee machine.")
        break

