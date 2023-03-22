class SodaStore:

    def __init__(self, brand, sold, redeemed, deposit, total):
        self.brand = brand
        self.sold = sold
        self.redeemed = redeemed
        self.deposit = deposit
        self.total = total
        self.cart = {}
        

    def add_item(self, brand, quantity, deposit=0.05):
        self.total += quantity * deposit
        if brand in self.cart:
            self.cart[brand]['quantity'] += quantity
            self.cart[brand]['deposit'] += quantity * 0.05
        else:
            self.cart[brand] = {
                'quantity': quantity,
                'deposit': deposit
            }
        

    def redeem_item(self, brand, quantity, deposit=0.05):
        self.total -= quantity * deposit
        if brand in self.cart:
            self.cart[brand]['quantity'] -= quantity
            self.cart[brand]['deposit'] -= quantity * 0.05
        else:
            self.cart[brand] = {
                'quantity': - quantity,
                'deposit': - quantity * 0.05,
            }
        self.show_list()

    def show_list(self):
        print('\n','='*10)
        print(self.cart)

    def driver():
        shop = SodaStore("", 0, 0, 0.05, 0)
        shopping = True
        while shopping:
            user_choice = input('What are you here for today? (buy/redeem/show/quit) ').lower()
            if user_choice == 'buy':
                item = input('Which brand would you like to buy?: CocaCola or Pepsi: ').lower()
                if item == 'cocacola':
                    try:
                        quantity = int(input('How many do you want to buy?: '))
                    except:
                        print('Please Try again with a quantity in digits')
                        continue
                    deposit = 0.05 * quantity
                    shop.add_item(item, quantity, deposit)
                elif item == 'pepsi':
                    try:
                        quantity = int(input('How many do you want to buy?: '))
                    except:
                        print('Please Try again with a quantity in digits')
                        continue
                    deposit = 0.05 * quantity
                    shop.add_item(item, quantity, deposit)
            elif user_choice == 'redeem':
                item = input('which brand will you redeem? (CocaCola/Pepsi):  ').lower()
                try:
                    quantity = (input('How many containers do you want to redeem?: '))
                    if quantity.isdigit():
                        quantity=float(quantity)
                except:
                    print("Please enter quantity in digits")
                    continue
                deposit = 0.05
                shop.redeem_item(item, quantity, deposit)
            elif user_choice == 'show':
                shop.show_list()
            elif user_choice == 'quit':
                shopping = False
                shop.show_list()
                break
            else:
                print('Please Enter Valid Choice')
SodaStore.driver()