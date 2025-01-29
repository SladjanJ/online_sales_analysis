import random
from product import Product
import random
from product import Product
from product_manager import ProductManager
from cart import Cart


# Kreirana instanca klase ProductManager
pr_manager = ProductManager()

# Kreirana instanca za dodavanje informacija o proizvodima
pr_manager.add_product("Banana", 3, 15)
pr_manager.add_product("Kiwi", 7, 10)
pr_manager.add_product("Chocolate", 9, 20)
pr_manager.add_product("Jabuka", 5, 12)
pr_manager.add_product("Breskva", 8, 18)

# Poziv funkcije za ispis proizvoda sa svim podacima
pr_manager.display_all_products()

print("-" * 50)
# Poziv funkcije za ispis ukupne vrednosti inventara
pr_manager.total_inventory_value()

print("-" * 50)
# Poziv funkcije za brisanje proizvoda iz liste po imenu
pr_manager.remove_product("Banana")

# Poziv funkcije za ispis samo imena proizvoda
pr_manager.only_name_of_products()

print("-" * 50)

# Kreiranje instance Cart
cart = Cart()

# Nasumično biramo 3 proizvoda iz liste dostupnih proizvoda
random_products = random.sample(pr_manager.products, 3)

# Dodajemo ih u korpu
for product in random_products:
    cart.add_to_cart(product)

# Prikaz sadržaja korpe
cart.display_cart_contents()

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
