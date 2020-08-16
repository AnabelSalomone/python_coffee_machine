class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

def get_price(acc, drink):
    total_price = acc + drink.price
    return total_price

drinks = []
drinks.append(Drink(1, "Capuccino", 2.50))
drinks.append(Drink(2, "Coffee with milk", 2.00))
drinks.append(Drink(3, "Espresso", 1.30))
drinks.append(Drink(4, "Mint tea", 1.90))
drinks.append(Drink(5, "Cocoa", 2.20))

machine_on = True
total = 0

print("Welcome to the Coffee Machine")
print("---" * 7)
print("Chat would you like to drink?")
for drink in drinks:
    print(str(drink.code) + " - " + drink.name)
print()

while machine_on:
    choice = int(input("What do you choose? "))
    while choice > len(drinks):
        choice = int(input("Please, select a valid number: "))

    total = get_price(total, drinks[choice - 1])

    print("Your total: " + str("{:.2f}".format(total)))
    print("Would you like something else? ")
    something_else = input("Press Y to continue, or any key to exit ")
    if something_else == "Y":
        machine_on = True
    else:
        machine_on = False

print("Goodbye")



