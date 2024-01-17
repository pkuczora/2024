class CoffeeMachine:
    def __init__(self, money, water, milk, beans, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups

    def remaining(self):
        # global money, water, milk, beans, cups
        print("The coffee machine has:")
        print(f"""{self.water} ml of water""")
        print(f"""{self.milk} ml of milk""")
        print(f"""{self.beans} of coffee beans""")
        print(f"""{self.cups} disposable cups""")
        print(f"""${self.money} of money""")
        self.menu()

    def menu(self):
        # global money, water, milk, beans, cups
        chose_action = input("Write action (buy, fill, take, remaining, exit): ")
        if chose_action == "buy":
            self.cafe()
        elif chose_action == "fill":
            self.fill()
        elif chose_action == "take":
            self.take()
        elif chose_action == "remaining":
            self.remaining()
        elif chose_action == "exit":
            self.turn_off()
        else:
            self.menu()

    def fill(self):

        water_increase = int(input("Write how many ml of water you want to add:"))
        milk_increase = int(input("Write how many ml of milk you want to add:"))
        beans_increase = int(input("Write how many grams of coffee beans you want to add:"))
        cups_increase = int(input("Write how many disposable cups you want to add:"))
        self.water = self.water + water_increase
        self.milk = self.milk + milk_increase
        self.beans = self.beans + beans_increase
        self.cups = self.cups + cups_increase
        self.menu()


    def cafe(self):

        which_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")

        if which_coffee == "1":
            water_needed = 250
            beans_needed = 16
            cups_needed = 1
            cost = 4
            if self.water < water_needed:
                print("Sorry, not enough water!")
                self.menu()
            elif self.beans < beans_needed:
                print( "Sorry, not enough beans!" )
                self.menu()
            elif self.cups < cups_needed:
                print( "Sorry, not enough cups!" )
                self.menu()
            else:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - water_needed
                self.beans = self.beans - beans_needed
                self.money += cost
                self.cups -= 1
                self.menu()
        elif which_coffee == "2":
            water_needed = 350
            milk_needed = 75
            beans_needed = 20
            cups_needed = 1
            cost = 7
            if self.water < water_needed:
                print("Sorry, not enough water!")
                self.menu()
            elif self.beans < beans_needed:
                print( "Sorry, not enough beans!" )
                self.menu()
            elif self.milk < milk_needed:
                print( "Sorry, not enough milk!" )
                self.menu()
            elif self.cups < cups_needed:
                print( "Sorry, not enough cups!" )
                self.menu()
            else:
                print( "I have enough resources, making you a coffee!" )
                self.water = self.water - water_needed
                self.milk = self.milk - milk_needed
                self.beans = self.beans - beans_needed
                self.money += cost
                self.cups -= 1
                self.menu()
        elif which_coffee == "3":
            water_needed = 200
            milk_needed = 100
            beans_needed = 12
            cups_needed = 1
            cost = 6
            if self.water < water_needed:
                print("Sorry, not enough water!")
                self.menu()
            elif self.beans < beans_needed:
                print( "Sorry, not enough water!" )
                self.menu()
            elif self.milk < milk_needed:
                print( "Sorry, not enough milk!" )
                self.menu()
            elif self.cups < cups_needed:
                print( "Sorry, not enough cups!" )
                self.menu()
            else:
                print( "I have enough resources, making you a coffee!" )
                self.water = self.water - water_needed
                self.milk = self.milk - milk_needed
                self.beans = self.beans - beans_needed
                self.money += cost
                self.cups -= 1
                self.menu()
        elif which_coffee == "back":
            self.menu()

    def take(self):

        print(f"I gave you ${self.money}")
        self.money = 0
        print("")
        self.menu()

    def turn_off(self):
        exit


new_machine = CoffeeMachine(550, 400, 540, 120, 9)
new_machine.menu()


