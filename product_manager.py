from product import Product

class ProductManager(Product):
    def init(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def display_all_products(self):
        for p in self.products:
            print(f"Products: {p.display_info()}")

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total value of all products: {total_value}")
