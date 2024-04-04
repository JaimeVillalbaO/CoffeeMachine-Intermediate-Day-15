from dicc_day15 import MENU, resources, COINS, LOGO

def report():
    for k in resources:
            if k == 'coffee':
                print(f'{k}: {resources[k]} gr')
            else :
                print(f'{k}: {resources[k]} ml')
          
    print(f'Money: ${money} \n')

def check_ingredients(order):
    for k in resources:
        if resources[k] < MENU[order]["ingredients"][k]: 
            return(f'Sorry there is not enough {k}.')
              
        else: 
            return '\nOk, your product is avalible.\n'

def change_funct(order):
    for k in COINS :
        bill = COINS[k]*int(input(f'How many {k}? ')) 
    return bill - MENU[order]['cost']

def remain_ingredients(order):
    for k in resources:
        resources[k] =  resources[k] - MENU[order]["ingredients"][k]
    return resources
    

money = 0
bill = 0
order_again = True
print(LOGO)
while order_again:
    order = input('What would you like? (espresso/latte/cappuccino): ').lower()
    
    if order == 'off': 
        break

    if order == 'report':
        report()
        continue
    
    else: 
        print(check_ingredients(order))
        if (check_ingredients(order)) != '\nOk, your product is avalible.\n':
           continue

    print('Please insert your coins: ')
    
    change = change_funct(order)

    if change < 0 :
        print('\nSorry you do not have enough money. \n')
        continue

    print(f'\nHere is ${change} in change. ')

    print(f'Here is you {order}. Enjoy !!! ☕\n')

    money += MENU[order]['cost']

    remain_ingredients(order)



