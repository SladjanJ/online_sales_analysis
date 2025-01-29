from product_manager import ProductManager

class Cart(ProductManager):
    def __init__(self):
        self.cart_items = []
    
    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Product {product.name} added to cart")

    def total_cart_value(self):
        total_value = sum(product.price * product.quantity for product in self.cart_items)
        print(f"Total cart value: {total_value}$")
    
    def display_cart_contents(self):
        for items in self.cart_items:
            print(f"Products in cart: {items.name}")
