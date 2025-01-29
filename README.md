# Online Sales Analysis

This project is an implementation of a basic product and cart management system. It allows you to manage a list of products, add and remove items from a cart, and calculate the total value of the products in the cart.

## Classes and Functionalities

### `Product` class
The `Product` class represents a product in the inventory. It contains the following attributes and methods:
- **Attributes**: `name`, `price`, `quantity`
- **Methods**: 
  - `display_info()`: Displays information about the product.
  - `update_quantity(amount)`: Updates the quantity of the product.

### `ProductManager` class
The `ProductManager` class manages a list of products. It allows adding products, displaying products, and removing them from the inventory. It also provides a method to calculate the total value of the inventory. Methods include:
- `add_product(name, price, quantity)`: Adds a product to the list.
- `display_all_products()`: Displays all products in the inventory.
- `total_inventory_value()`: Calculates and displays the total value of the inventory.
- `remove_product(name)`: Removes a product by its name.
- `only_name_of_products()`: Displays only the names of the products in the inventory.

### `Cart` class
The `Cart` class represents a shopping cart. It allows you to add products to the cart and calculate the total value of the items in the cart. It includes:
- **Attributes**: `cart_items` (list of products in the cart).
- **Methods**: 
  - `add_to_cart(product)`: Adds a product to the cart.
  - `display_cart_contents()`: Displays all the products currently in the cart.
  - `total_cart_value()`: Calculates and displays the total value of the cart.

## Features Implemented
- Add products to inventory.
- Display products and inventory value.
- Remove products from inventory.
- Add products to a shopping cart.
- Display cart contents and total value.
- Randomly select products to add to the cart.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/online_sales_analysis.git
