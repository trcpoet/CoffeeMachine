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

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:#order_ingredients[item] = water,milk,coffee of choice, resources[item] = water,milk,coffee of resources. #item would be equal to water
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough #Stays true until the if statement gets activated

#TODO 5: Create a function to process the coins
def process_coins():
    """Returns the total calculated from the coins inserted."""
    print("Please insert coins")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many quarters?")) * 0.01
    return total

#TODO 6: Check if transaction is successful
def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit  += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. ${money_received} refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")

is_on = True
#TODO 1a. Check the user’s input to decide what to do next
#TODO 1b. The prompt should show every time action has completed
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    #TODO 2a.Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        is_on = False
    #TODO 3a. Print Report
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else: #TODO 4 Check if resources are sufficient
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']): #Takes values of ingredient from drink which is = to MENU[choice]
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

