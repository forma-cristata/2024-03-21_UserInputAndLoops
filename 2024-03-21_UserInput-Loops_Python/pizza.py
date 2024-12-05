from item import Item

PIZZA_PRICING_NAME = ("small", "medium", "large")
PIZZA_PRICING_PRICES = (10, 12, 14)


class Pizza(Item):
    def __init__(self, price, size, toppings):
        super().__init__(price)
        self.size = size
        self.toppings = toppings
        
    def ChoosePizzaSize(self, pizza_sizes, pizza_prices):
        #TODO, print table of pizza sizes and prices
        choice = input("What size pizza would you like? (or enter q to quit):\n>>>")
        choice = choice.strip().casefold()
        
        while choice not in pizza_sizes and choice != 'q':
            print("Please choose a valid pizza size.") 
            choice = input("What size pizza would you like?\n>>>")
            choice = choice.strip().casefold()
         
        iteration = 0   
        for i in range(0, len(pizza_sizes)):
            if choice == pizza_sizes[i]:
                iteration = i
                break
        if choice != 'q':
            self.size = pizza_sizes[iteration]
            self.price = pizza_prices[iteration]
        else:
            self.size = 'q' 
        
        
    
            
            
                
    def ChooseToppings(self, toppings_available) -> list:
        topping_chosen = ''
        available_toppings = list(toppings_available[:])
        chosen_toppings = []
        
        topping_chosen = input("What toppings would you like? \nPlease enter separated by a comma and space, or enter nothing to quit:\n>>>")
    
        topping_chosen = topping_chosen.strip().casefold()
        
        tops = topping_chosen.split(', ')
                
        for i in range (0, len(tops)):
            if tops[i] not in available_toppings and len(tops) != 0:
                if tops[i] in toppings_available:
                    print(f'You already chose {tops[i]}!. Choose something else')
                    tops[i] = input('>>>').strip().casefold()
                elif topping_chosen == '':
                    break   
                else:
                    print(f"We do not have {tops[i]}.  Please choose something else")
                    tops[i] = input('>>>')
                

                
                
                while tops[i] not in available_toppings:
                    tops[i] = input('Please choose a valid topping!\n>>>').strip().casefold()
            elif (len(tops) != 0):
                available_toppings.remove(tops[i])
            else: break
            
            
        
        self.toppings = tops    
            
                
