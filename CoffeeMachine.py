class CoffeeMachine:
    COST_CHART = [
        {"item": "espresso", "item_type": 1, "WATER_QUANTITY": 250, "MILK_QUANTITY": 0, "COFFEE_QUANTITY": 16, "cost": 4},
        {"item": "latte", "item_type": 2, "WATER_QUANTITY": 350, "MILK_QUANTITY": 75, "COFFEE_QUANTITY": 20, "cost": 7},
        {"item": "cappuccino", "item_type": 3, "WATER_QUANTITY": 200, "MILK_QUANTITY": 100, "COFFEE_QUANTITY": 12,
        "cost": 6}
        ]

    def __init__(self, water, milk, coffee, cups, cash):
        self.available_water = water
        self.available_milk = milk
        self.available_coffee = coffee
        self.available_disposable_cups = cups
        self.available_cash = cash
        self.action = ""

    def display_available(self):
        print("The coffee machine has:")
        print(str(self.available_water), "of water")
        print(str(self.available_milk), "of milk")
        print(str(self.available_coffee), "of coffee beans")
        print(str(self.available_disposable_cups), "of disposable cups")
        print(str(self.available_cash), "of money")

    def take_input(self):
        self.action = input("Write action (buy, fill, take, remaining, exit):").strip()
        if self.action == 'take':
            self.action_take()
        elif self.action == 'buy':
            self.action_buy()
        elif self.action == 'fill':
            self.action_fill()
        elif self.action == 'remaining':
            self.action_remaining()
        elif self.action == 'exit':
            return 'exit'
        else:
            print("Invalid Action")
            return 'exit'

    def action_take(self):
        print("I gave you $", str(self.available_cash))
        self.available_cash = 0

    def action_fill(self):
        self.available_water += int(input("Write how many ml of water do you want to add:").strip())
        self.available_milk += int(input("Write how many ml of milk do you want to add:").strip())
        self.available_coffee += int(input("Write how many grams of coffee beans do you want to add:").strip())
        self.available_disposable_cups += int(input("Write how many disposable cups do you want to add:").strip())
        
    def check_resources_available(self, item_type):   
        flag = False
        for c in CoffeeMachine.COST_CHART:
            if c['item_type'] == item_type:
                if self.available_water - c['WATER_QUANTITY'] < 0:
                    print("Sorry, not enough water!")
                    flag = True
                elif self.available_milk - c['MILK_QUANTITY'] < 0:
                    print("Sorry, not enough milk!")
                    flag = True
                elif self.available_coffee - c['COFFEE_QUANTITY'] < 0:
                    print("Sorry, not enough coffee beans!")
                    flag = True
                elif self.available_disposable_cups == 0:
                    print("Sorry, not enough disposable cups")
                    flag = True
                else:
                    print("I have enough resources, making you a coffee!")
                    flag = False
        return flag

    def dispense_coffee(self, item_type):
        flag = self.check_resources_available(item_type)
        if not flag:
            for c in CoffeeMachine.COST_CHART:
                if c['item_type'] == item_type:
                    self.available_coffee -= c['COFFEE_QUANTITY']
                    self.available_milk -= c['MILK_QUANTITY']
                    self.available_disposable_cups -= 1
                    self.available_water -= c['WATER_QUANTITY']
                    self.available_cash += c['cost']
                    
    def action_buy(self):
        type_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:").strip()
        if type_of_coffee == 'back':
            pass
        else:
            self.dispense_coffee(int(type_of_coffee))

    def action_remaining(self):
        self.display_available()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    op = coffee_machine.take_input()
    if op == 'exit':
        break

