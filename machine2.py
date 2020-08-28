class Drink:
    def __init__(self, name, price, extra="none"):
        self.name = name
        self.price = price
        self.extra = extra

class Extra:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def get_price(acc, drink, extra = 0):
    total_price = acc + drink.price + extra.price
    return total_price

drinks = []
drinks.append(Drink("Capuccino", 2.50))
drinks.append(Drink("Coffee with milk", 2.00))
drinks.append(Drink("Espresso", 1.30))
drinks.append(Drink("Mint tea", 1.90))
drinks.append(Drink("Cocoa", 2.20))

extras = []
extras.append(Extra("Milk", 0.50))
extras.append(Extra("Cream", 0.75))
extras.append(Extra("Sugar", 0.10))
extras.append(Extra("No thanks", 0.00))

machine_on = True
total = 0
basket = []


print("Welcome to the Coffee Machine")
print("---" * 7)

while machine_on:
    print("What would you like to drink?")
    for i in range(len(drinks)):
        drink = drinks[i]
        print( str(i+1) + " - " + drink.name, "for", drink.price)
    print()

    choice = int(input("What do you choose? "))
    while choice > len(drinks):
        choice = int(input("Please, select a valid number: "))

    basket.append(drinks[choice -1])
    print("\n Your basket:")
    for item in basket:
        print("- ", item.name)

    print()
    
    wants_extra = True
    while wants_extra:
        for i in range(len(extras)):
            extra = extras[i]
            if extra.name == "No thanks":
                print("4 - No thanks")
            else:
                print(str(i+1) + " - Add ", extra.name, " for ", extra.price)
        
        extra_choice = int(input("Would you like some extras?"))
        if extra_choice > len(extras):
            extra_choice = int(input("Please select a valid number"))
        
        basket.append(extras[extra_choice -1])
        
        wants_extra = False


    print()

    total = get_price(total, drinks[choice - 1], extras[extra_choice - 1])
    print("Your total: " + str("{:.2f}".format(total)), "\n")

    print("Would you like something else? ")
    something_else = input("Press Y to continue, or any key to exit ")
    if something_else.upper() == "Y":
        machine_on = True
    else:
        machine_on = False

print("Goodbye")



