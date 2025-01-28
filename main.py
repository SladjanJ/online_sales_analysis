from product_manager import ProductManager

pr_manager = ProductManager()

pr_manager.add_product("Banana", 3, 15)
pr_manager.add_product("Kiwi", 7, 10)
pr_manager.add_product("Chocolate", 9, 20)

pr_manager.display_all_products()
pr_manager.total_inventory_value()
