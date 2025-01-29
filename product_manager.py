from product import Product

class ProductManager(Product):
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
    
    def display_all_products(self):
        for p in self.products:
                print(f"Product: {p.name}; Price: {p.price}; Quantity: {p.quantity}")

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total value of all products: {total_value}$")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Product '{product_name}' is deleted.")
                return
        print(f"Product '{product_name}' not found.")
    
    def only_name_of_products(self):
        for product in self.products:
            print(f"Product: {product.name}")
