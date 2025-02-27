class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product name: {self.name}; Product price: {self.price}; Product quantity: {self.quantity}")
    
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"Updated product quantity: {self.quantity}")
