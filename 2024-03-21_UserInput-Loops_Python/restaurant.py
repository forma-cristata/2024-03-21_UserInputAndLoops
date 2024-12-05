from pizza import Pizza
from tabulate import tabulate
from time import sleep
import os

PIZZA_PRICING_NAME = ("small", "medium", "large")
PIZZA_PRICING_PRICES = (10, 12, 14)
AVAILABLE_TOPPINGS = ('pepperoni', 'mushrooms', 'onions', 'sausage', 'extra cheese')
TOPPING_PRICE = 2
IDEAL_SLEEP_TIME = 0.3
DELIVERY_FEE = 5


def PrintSizes():
    menu = [[PIZZA_PRICING_NAME[0], PIZZA_PRICING_PRICES[0]], 
            [PIZZA_PRICING_NAME[1], PIZZA_PRICING_PRICES[1]],
            [PIZZA_PRICING_NAME[2], PIZZA_PRICING_PRICES[2]]]
    menu_header = ['SIZE', 'PRICE']
    print(tabulate(menu, headers=menu_header, tablefmt="grd") + '\n')

def PrintToppings():
    toppings = [[f"${TOPPING_PRICE}", AVAILABLE_TOPPINGS[0]],
                ['', AVAILABLE_TOPPINGS[1]],
                ['', AVAILABLE_TOPPINGS[2]],
                ['', AVAILABLE_TOPPINGS[3]],
                ['', AVAILABLE_TOPPINGS[4]]]
    top_header = ['PRICE', 'TOPPING']
    print(tabulate(toppings, headers=top_header, tablefmt="grd") + '\n')
def PrintReceipt(order, delivery_fee, order_sum):
    standard_tabulation = 9*'\t'
    
    
    for item in order:
        item_tabulation = '\t'
        match len(item.toppings):
            case 4:
                if 'extra cheese' in item.toppings:
                    item_tabulation *= 2
                else:
                    item_tabulation *= 3
            case 3: 
                if 'extra cheese' in item.toppings:
                    item_tabulation *= 3
                else:
                    item_tabulation *= 4
            case 2:
                if 'extra cheese' in item.toppings:
                    item_tabulation *= 5
                else:
                    item_tabulation *= 6
            case 1:
                if 'extra cheese' in item.toppings:
                    item_tabulation *= 6
                else:
                    if item.toppings[0] == '':
                        item_tabulation *= 8
                    else:
                        item_tabulation *= 7
            case _:
                if 'extra cheese' in item.toppings:
                    item_tabulation = 0
                
        print(f"{item.size}\t{item.toppings}{item_tabulation}${item.price}")
    if delivery_fee != 0:
        print('-'*75)
        print(f'SubTotal{standard_tabulation[:-1]}${order_sum}\nDelivery{standard_tabulation[:-1]}${DELIVERY_FEE}\n{'-'*75}\nTotal{standard_tabulation}${order_sum + delivery_fee}')
    else:
        print('-'*75)
        print(f'SubTotal{standard_tabulation[:-1]}${order_sum}\nPick Up{standard_tabulation}$0\n{'-'*75}\nTotal{standard_tabulation}${order_sum}')
        
        
os.system('cls')    
total_order = []
order_sum = 0
order_more = ''

while(order_more.casefold() != 'q'):
    PrintSizes()
    pizza1 = Pizza('', '', 0)
    sleep(IDEAL_SLEEP_TIME)
    pizza1.ChoosePizzaSize(PIZZA_PRICING_NAME, PIZZA_PRICING_PRICES)
    os.system('cls')
    
    if pizza1.size != 'q':
        sleep(IDEAL_SLEEP_TIME)
        PrintToppings()
        sleep(IDEAL_SLEEP_TIME)
        pizza1.ChooseToppings(AVAILABLE_TOPPINGS)
        
        if pizza1.toppings[0] != '':
            pizza1.price = pizza1.price + 2 * len(pizza1.toppings)
            
        os.system('cls')
        
        if pizza1.toppings[0]=='':
            print(f"{pizza1.size} ${pizza1.price} pizza.")
            
        else:
            print(f"{pizza1.size} ${pizza1.price} pizza with {' and '.join(pizza1.toppings)}")
            
        x = input('\nPress any button to continue...')    
        total_order.append(pizza1)
        os.system('cls')
        
    else:
        break
 

for i in range(0, len(total_order)):
    order_sum += total_order[i].price
delivered = pizza1.DeliveryChoice()

PrintReceipt(total_order, delivered, order_sum)
