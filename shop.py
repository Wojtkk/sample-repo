"""Shop class that sells products to customers and orders from magazines."""

from product import Product
from customer import Customer


class Shop:
    """Represents a shop that sells products to customers and orders from magazines."""
    
    def __init__(self, shop_id, name):
        """
        Initialize a Shop.
        
        Args:
            shop_id (int): Unique identifier for the shop
            name (str): Name of the shop
        """
        self.shop_id = shop_id
        self.name = name
        self.inventory = {}  # product_id -> quantity
        self.products = {}   # product_id -> Product
        self.sales_history = []  # List of sales made
        self.revenue = 0.0
    
    def __str__(self):
        """String representation of the shop."""
        return f"Shop(id={self.shop_id}, name='{self.name}', revenue=${self.revenue:.2f})"
    
    def __repr__(self):
        """Detailed representation of the shop."""
        return f"Shop({self.shop_id}, '{self.name}')"
    
    def add_product(self, product, quantity):
        """
        Add a product to shop inventory (used when receiving orders).
        
        Args:
            product (Product): The product to add
            quantity (int): Quantity to add
        """
        if product.product_id in self.products:
            self.inventory[product.product_id] += quantity
        else:
            self.products[product.product_id] = product
            self.inventory[product.product_id] = quantity
        
        print(f"[Shop {self.name}] Added {quantity}x {product.name} to inventory")
    
    def get_stock_level(self, product_id):
        """
        Get current stock level for a product.
        
        Args:
            product_id (int): ID of the product
            
        Returns:
            int: Current stock quantity, or 0 if not in inventory
        """
        return self.inventory.get(product_id, 0)
    
    def order_from_magazine(self, magazine, product_id, quantity):
        """
        Order products from a magazine (warehouse).
        
        Args:
            magazine: The Magazine instance to order from
            product_id (int): ID of the product to order
            quantity (int): Quantity to order
            
        Returns:
            bool: True if order was successful, False otherwise
        """
        print(f"[Shop {self.name}] Ordering {quantity}x product {product_id} from {magazine.name}")
        
        # Magazine fulfills the order
        if magazine.fulfill_order(self, product_id, quantity):
            # Add products to shop inventory
            product = magazine.catalog[product_id]
            self.add_product(product, quantity)
            return True
        else:
            print(f"[Shop {self.name}] Order failed")
            return False
    
    def sell_product(self, customer, product_id, quantity=1):
        """
        Sell a product to a customer.
        
        Args:
            customer (Customer): The customer buying the product
            product_id (int): ID of the product to sell
            quantity (int): Quantity to sell
            
        Returns:
            bool: True if sale was successful, False otherwise
        """
        # Check if product is available
        if product_id not in self.products:
            print(f"[Shop {self.name}] Product {product_id} not available")
            return False
        
        # Check if sufficient stock
        if self.inventory[product_id] < quantity:
            print(f"[Shop {self.name}] Insufficient stock for product {product_id}. Available: {self.inventory[product_id]}, Requested: {quantity}")
            return False
        
        product = self.products[product_id]
        total_cost = product.price * quantity
        
        # Check if customer has enough balance
        if customer.balance < total_cost:
            print(f"[Shop {self.name}] Customer {customer.name} has insufficient balance. Required: ${total_cost:.2f}, Available: ${customer.balance:.2f}")
            return False
        
        # Complete the transaction
        self.inventory[product_id] -= quantity
        self.revenue += total_cost
        
        # Update customer's purchase history
        customer.add_purchase(product, quantity, total_cost)
        
        # Record sale
        self.sales_history.append({
            'customer': customer,
            'product': product,
            'quantity': quantity,
            'revenue': total_cost
        })
        
        print(f"[Shop {self.name}] Sold {quantity}x {product.name} to {customer.name} for ${total_cost:.2f}")
        return True
    
    def get_inventory_summary(self):
        """Get a summary of all products and their stock levels."""
        summary = []
        for product_id, quantity in self.inventory.items():
            product = self.products[product_id]
            summary.append({
                'product': product,
                'quantity': quantity
            })
        return summary
    
    def get_revenue_report(self):
        """Get total revenue from sales."""
        return {
            'total_revenue': self.revenue,
            'total_sales': len(self.sales_history)
        }
