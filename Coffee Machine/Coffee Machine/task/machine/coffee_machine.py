amountOfWater = 400
amountOfMilk = 540
amountOfCB = 120
amountOfCups = 9
amountOfMoney = 550

def greeting():
    print('''The coffee machine has:
    {water} of water
    {milk} of milk
    {cb} of coffee beans
    {cups} of disposable cups
    {money} of money
    '''.format(water = amountOfWater, milk = amountOfMilk, cb = amountOfCB, cups = amountOfCups, money = amountOfMoney))

def espresso():
    global amountOfWater
    global amountOfCB
    global amountOfMoney
    global amountOfCups

    amountOfWater -= 250
    amountOfCB -= 16
    amountOfMoney += 4
    amountOfCups -= 1

    return greeting()

def latte():
    global amountOfWater
    global amountOfMilk
    global amountOfCB
    global amountOfMoney
    global amountOfCups

    amountOfWater -= 350
    amountOfMilk -= 75
    amountOfCB -= 20
    amountOfMoney += 7
    amountOfCups -= 1

    return greeting()

def cappuccino():
    global amountOfWater
    global amountOfMilk
    global amountOfCB
    global amountOfMoney
    global amountOfCups

    amountOfWater -= 200
    amountOfMilk -= 100
    amountOfCB -= 12
    amountOfMoney += 6
    amountOfCups -= 1

    return greeting()

greeting()

choice = input('Write action (buy, fill, take): ')

if choice == 'buy':
    buyChoice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
    if buyChoice == '1':
        espresso()
    elif buyChoice == '2':
        latte()
    elif buyChoice == '3':
        cappuccino()
    else:
        print('You entered wrong number. Please try later!')

elif choice == 'fill':
    additionalWater = int(input('Write how many ml of water do you want to add:'))
    amountOfWater += additionalWater

    additionalMilk = int(input('Write how many ml of milk do you want to add:'))
    amountOfMilk += additionalMilk

    additionalCB = int(input('Write how many grams of coffee beans do you want to add:'))
    amountOfCB += additionalCB

    additionalCups = int(input('Write how many disposable cups of coffee do you want to add:'))
    amountOfCups += additionalCups

    greeting()

else:
    print(f'I gave you ${amountOfMoney}')
    amountOfMoney = 0
    greeting()
