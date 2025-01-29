import random
from product import Product
import random
from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreirana instanca na klasi ProductManager
pr_manager = ProductManager()

# Kreirana instanca za dodavanje informacija proizvoda
pr_manager.add_product("Banana", 3, 15)
pr_manager.add_product("Kiwi", 7, 10)
pr_manager.add_product("Chocolate", 9, 20)

# Poziv funkcije za ispis proizvoda sa svim 
pr_manager.display_all_products()

# Poziv funkcije za ispis ukupne vrijednosti inventara
pr_manager.total_inventory_value()

# Poziv funkcije za brisanje proizvoda iz liste po imenu
pr_manager.remove_product("Banana")

# Poziv funkcije za ispis samo imena proizvoda preko instance
pr_manager.only_name_of_products()


