DELIVERY_FEE = 5
DELIVERY_CHOICES = ('yes', 'no')

class Item:
    def __init__(self, price):
        self.price = price
        
    def DeliveryChoice(self):
        users_choice = ''
        while users_choice not in DELIVERY_CHOICES:
            users_choice = input("Would you like delivery?\n>>>").strip().casefold()
        if users_choice == DELIVERY_CHOICES[0]:
            return DELIVERY_FEE
        else:
            return 0