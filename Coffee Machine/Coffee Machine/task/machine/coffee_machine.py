print('''Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!''')

amountOfWater = int(input('Write how many ml of water the coffee machine has:'))
amountOfMilk = int(input('Write how many ml of milk the coffee machine has:'))
amountOfCB = int(input('Write how many ml of coffee beans the coffee machine has:'))
wantedCoffee = int(input('Write how many cups of coffee you will need:'))

def howManyCoffee(water, milk, cb):
    count = 0

    while water >= 200 and milk >= 50 and cb >= 15:

        water -= 200
        milk -= 50
        cb -= 15

        count += 1

    return count

noOfCups = howManyCoffee(amountOfWater, amountOfMilk, amountOfCB)
remaindingCups = noOfCups - wantedCoffee

if remaindingCups > 0:
    print('Yes, I can make that amount of coffee (and even {} more than that)'.format(remaindingCups))
elif noOfCups == wantedCoffee:
    print('Yes, I can make that amount of coffee')
else:
    print(f'No, I can make only {noOfCups} cups of coffee')
