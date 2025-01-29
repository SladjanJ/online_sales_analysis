import random
from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreiranje instance klase ProductManager
pr_manager = ProductManager()

# Dodavanje proizvoda sa promenjenim imenima i količinama
pr_manager.add_product("Kajsija", 6, 15)
pr_manager.add_product("Ananas", 10, 12)
pr_manager.add_product("Badem", 8, 25)
pr_manager.add_product("Nar", 5, 18)
pr_manager.add_product("Borovnica", 7, 22)

# Kreiranje instance Cart
cart = Cart()

# Nasumično biramo 3 proizvoda iz liste dostupnih proizvoda
random_products = random.sample(pr_manager.products, 3)

# Dodajemo ih u korpu
for product in random_products:
    cart.add_to_cart(product)

# Prikaz sadržaja korpe
cart.display_cart_contents()

# Računanje ukupne vrednosti korpe
cart.total_cart_value()
