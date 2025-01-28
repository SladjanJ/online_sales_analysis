from product import Product

class ProductManager(Product):
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
    
    def display_all_products(self):
        for p in self.products:
                print(f"Proizvod: {p.name}, Cena: {p.price}, Količina: {p.quantity}")

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total value of all products: {total_value}$")
