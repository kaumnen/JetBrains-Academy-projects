class CoffeeMachine:

    currentState = 123

    def __init__(self, amountOfWater, amountOfMilk, amountOfCB, amountOfCups, amountOfMoney):

        self.amountOfWater = amountOfWater
        self.amountOfMilk = amountOfMilk
        self.amountOfCB = amountOfCB
        self.amountOfCups = amountOfCups
        self.amountOfMoney = amountOfMoney

    def greeting(self):
        print('''\nThe coffee machine has:
    {water} of water
    {milk} of milk
    {cb} of coffee beans
    {cups} of disposable cups
    ${money} of money
        '''.format(water = self.amountOfWater, milk = self.amountOfMilk, cb = self.amountOfCB, cups = self.amountOfCups, money = self.amountOfMoney))

    def espresso(self):

        self.amountOfWater -= 250
        if self.amountOfWater < 0:
            self.amountOfWater += 250
            return 'Sorry, not enough water!'

        self.amountOfCB -= 16
        if self.amountOfCB < 0:
            self.amountOfCB += 16
            return 'Sorry, not enough coffee beans!'

        self.amountOfCups -= 1
        if self.amountOfCups < 0:
            self.amountOfCups += 1
            return 'Sorry, not enough cups!'

        self.amountOfMoney += 4

        return 'I have enough resources, making you a coffee!'

    def latte(self):

        self.amountOfWater -= 350
        if self.amountOfWater < 0:
            self.amountOfWater += 350
            return 'Sorry, not enough water!'

        self.amountOfMilk -= 75
        if self.amountOfMilk < 0:
            self.amountOfMilk += 75
            return 'Sorry, not enough milk!'

        self.amountOfCB -= 20
        if self.amountOfCB < 0:
            self.amountOfCB += 20
            return 'Sorry, not enough coffee beans!'

        self.amountOfCups -= 1
        if self.amountOfCups < 0:
            self.amountOfCups += 1
            return 'Sorry, not enough cups!'

        self.amountOfMoney += 7

        return 'I have enough resources, making you a coffee!'

    def cappuccino(self):

        self.amountOfWater -= 200
        if self.amountOfWater < 0:
            self.amountOfWater += 200
            return 'Sorry, not enough water!'

        self.amountOfMilk -= 100
        if self.amountOfMilk < 0:
            self.amountOfMilk += 100
            return 'Sorry, not enough milk!'

        self.amountOfCB -= 12
        if self.amountOfCB < 0:
            self.amountOfCB += 12
            return 'Sorry, not enough coffee beans!'

        self.amountOfCups -= 1
        if self.amountOfCups < 0:
            self.amountOfCups += 1
            return 'Sorry, not enough cups!'

        self.amountOfMoney += 6

        return 'I have enough resources, making you a coffee!'

    def workingState(self):

        while self.currentState != None:

            choice = input('Write action (buy, fill, take, remaining, exit): ')

            if choice == 'buy':

                self.currentState = 'buying'

                buyChoice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
                if buyChoice == '1':
                    print(self.espresso())
                elif buyChoice == '2':
                    print(self.latte())
                elif buyChoice == '3':
                    print(self.cappuccino())
                else:
                    print('You entered wrong number. Please try later!')

            elif choice == 'fill':

                self.currentState = 'filling'

                additionalWater = int(input('Write how many ml of water do you want to add:'))
                self.amountOfWater += additionalWater

                additionalMilk = int(input('Write how many ml of milk do you want to add:'))
                self.amountOfMilk += additionalMilk

                additionalCB = int(input('Write how many grams of coffee beans do you want to add:'))
                self.amountOfCB += additionalCB

                additionalCups = int(input('Write how many disposable cups of coffee do you want to add:'))
                self.amountOfCups += additionalCups

            elif choice == 'take':

                self.currentState = 'taking'

                print(f'I gave you ${self.amountOfMoney}')
                self.amountOfMoney = 0

            elif choice == 'remaining':

                self.currentState = 'printing'

                self.greeting()

            elif choice == 'exit':
                self.currentState = None

coffeemachine = CoffeeMachine(400, 540, 120, 9, 550)
coffeemachine.workingState()
