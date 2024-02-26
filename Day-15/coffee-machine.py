## Requirements


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
    "milk": 100,
    "coffee": 100,
    }

total_money_recieved = 0

def make_coffe():

    user_request = input("\n What would you like? (espresso/latte/cappuccino): \n")
    user_request.lower()
    

    if user_request not in ["off", "report", "espresso", "latte", "cappuccino"]:
        print("\nSorry please enter either espresso, latte or cappuccino)\n")
        return make_coffe()
    elif user_request == "off":
        return
    elif user_request == "report":
        print(resources)
        print(f"money received = ${round(total_money_recieved, ndigits=2)}")
        return make_coffe()

    resources_needed = MENU[user_request]["ingredients"]
    money_needed = MENU[user_request]['cost']
    total_given = 0

    # check it can be made or not
    for i in resources:
            for x in resources_needed:
                if i == x:
                    if resources[i] < resources_needed[x]:
                        print(f"sorry there's not enough {i}, please order something else.")
                        return make_coffe()
                    
    # check payment request
    quarters = input("How many Quarters?: ")
    nickles = input("How many nicles?: ")
    dimes = input("How many dimes?: ")
    pennies = input("How many pennies?: ")

    quarters = int(quarters) * 0.25
    nickles = int(nickles) * 0.10
    dimes = int(dimes) * 0.05
    pennies = int(pennies) * 0.01

    total_given = quarters + nickles + dimes + pennies
    # add to report

    if total_given < money_needed:
        print("sorry not enough money. \n Money refunded.\n")
        return make_coffe()
    else:
        print(f"Here's your change ${round(total_given - money_needed, ndigits=2)}")
    
    # Time to sort resources
    def handle_resources():
        global resources
        global total_money_recieved
        total_money_recieved += money_needed
        for i in resources:
            for x in resources_needed:
                if i == x:
                    resources[i] = resources[i] - resources_needed[x]
        print(f"Here's your {user_request.title()}, enjoy!!")     
        return make_coffe()
    

    handle_resources()
    

    
    
    
    
          
    


    # if resources["water"] < resources_needed["water"]:
    #     print("sorry not enough water")
    #     return make_coffe()
    # elif resources["milk"] < resources_needed["milk"]:
    #     print("sorry not enough milk")
    #     return make_coffe()
    # elif resources["coffee"] < resources_needed["coffee"]:
    #     print("sorry not enough milk")
    #     return make_coffe()
    # else:
    #     print("here you go!")
    #     return 

make_coffe()


# coin operated 
    # penny = 0.01
    # Dime = 0.1
    # nickel = 0.05
    # quarter = 025

# Requirements
# 1) Print a report on resource left - e.g. water and milk left
#   if you type report it will display the report with how much money left

# 2) Check sufficient resources left to make coffee
# check resources against resource and gives user feedbacks

# 3) Can process coins claculate change and if there's enough

# 4) make coffee and deduct resources 
