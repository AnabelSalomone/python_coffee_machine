class MachineItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Drink(MachineItem):
    def __init__(self, name, price, extra="none"):
        MachineItem.__init__(self, name, price) #Difference with super()?
        self.extra = extra

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
extras.append(MachineItem("Milk", 0.50))
extras.append(MachineItem("Cream", 0.75))
extras.append(MachineItem("Sugar", 0.10))
extras.append(MachineItem("No thanks", 0.00))

machine_on = True
valid_entry = False
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
    
    while not valid_entry:
        try:
            choice = int(input("What do you choose? "))
            if choice <= len(drinks):
                valid_entry = True
            else:
                print("Invalid input")
                valid_entry = False
        except Exception: 
            #it doesn't catch the ctrl+c command so the user can quit
            print("Invalid input")

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
        
        try: 
            extra_choice = int(input("Would you like some extras?"))
            if extra_choice <= len(extras):
                basket.append(extras[extra_choice -1])
                wants_extra = False
        except Exception:
            print("\n Invalid Input")


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





