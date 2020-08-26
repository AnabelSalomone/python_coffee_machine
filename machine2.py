class Drink:
    def __init__(self, code, name, price, extra="none"):
        self.code = code
        self.name = name
        self.price = price
        self.extra = extra

class Extra:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

def get_price(acc, drink, extra = 0):
    total_price = acc + drink.price + extra.price
    return total_price

drinks = []
drinks.append(Drink(1, "Capuccino", 2.50))
drinks.append(Drink(2, "Coffee with milk", 2.00))
drinks.append(Drink(3, "Espresso", 1.30))
drinks.append(Drink(4, "Mint tea", 1.90))
drinks.append(Drink(5, "Cocoa", 2.20))

extras = []
extras.append(Extra(1, "Milk", 0.50))
extras.append(Extra(2, "Cream", 0.75))
extras.append(Extra(3, "Sugar", 0.10))
extras.append(Extra(4, "No thanks", 0.00))

machine_on = True
total = 0
basket = []


print("Welcome to the Coffee Machine")
print("---" * 7)

while machine_on:
    print("What would you like to drink?")
    for drink in drinks:
        print(str(drink.code) + " - " + drink.name, "for", drink.price)
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
        for item in extras:
            if item.name == "No thanks":
                print("4 - No thanks")
            else:
                print(item.code, " - Add ", item.name, " for ", item.price)
        
        extra_choice = int(input("Would you like some extras?"))
        if extra_choice > len(extras):
            extra_choice = int(input("Please select a valid number"))
        
        basket.append(extras[choice -1])
        
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



