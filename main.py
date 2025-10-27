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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

income = 0

machine_is_on = True

# TODO: 1. Print of all coffee machine resources
def report():
    print("Water: {}ml\nMilk: {:0}ml\nCoffee: {}g\nIncome: ${:.2f}".format(resources["water"], resources["milk"], resources["coffee"], income))

# TODO: 2. process payment
def checkout(order, ingredients):
    global income
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    income += MENU[order]["cost"]
    print(f"Here is your {order} 🍵. Enjoy!")

# TODO: 3. start the machine and check resources sufficient to make drink order.
def start(order):

    cost = float(MENU[order]["cost"])
    ingredients = MENU[order]["ingredients"]

    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return

    print(f"The cost will be ${cost}")
    print("Please insert coins...")
    quarters = int(input("How many quarters?:")) * 0.25
    dimes = int(input("How many dimes?:")) * 0.10
    nickles = int(input("How many nickles?:")) * 0.05
    pennies = int(input("How many pennies?:")) * 0.01

    coins = quarters + dimes + nickles + pennies

    if coins < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(coins - cost, 2)
        print("The total cost deducted from your coins and here is your change ${:.2f}".format(change))
        checkout(order, ingredients)

# TODO: 4. Creating a while loop to keep asking the user for new order
while machine_is_on:
    prompt = input("What would you like? (espresso/latte/cappuccino):").lower()

    if prompt in list(MENU.keys()) or prompt == "off" or prompt == "report":
        # TODO: 5. Turn off the Coffee Machine by entering “ off ” to the prompt or print report if requested.
        if prompt == "off":
            machine_is_on = False
            print("The coffee machine is turned off!")
        elif prompt == "report":
            report()
        else:
            start(prompt)
    else:
        print("Wrong input, please check your input and try again.")

