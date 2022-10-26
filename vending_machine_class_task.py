class VendingMachine:
    # attributes for each vending machine
    def __init__(self, id, balance):
        self.id = id
        self.products = []
        self.balance = balance
    
        def add_initial_stock(self):
            # this fills the self.products with products when the vending machine 
            # is first created
            for i in range(10):
                self.products.append(Product("JUICE01", "Juice Box", 3.50))

        add_initial_stock(self)

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.product_name = name
        self.price = price

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.account_balance = 0
    
    def add_funds(self, deposit_amount):
        self.account_balance += deposit_amount

    def __str__(self):
        return self.name + "Balance: " + str(self.account_balance)

brimson_vend = VendingMachine("BRIM01", 100)
magnus = Person("542", "Leuchars, Magnus")
print(magnus)
