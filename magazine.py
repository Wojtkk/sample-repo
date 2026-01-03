"""Magazine (warehouse) class that supplies products to shops."""

from product import Product


class Magazine:
    """Represents a warehouse/supplier that fulfills shop orders."""
    
    def __init__(self, magazine_id, name):
        """
        Initialize a Magazine (warehouse).
        
        Args:
            magazine_id (int): Unique identifier for the magazine
            name (str): Name of the magazine/warehouse
        """
        self.magazine_id = magazine_id
        self.name = name
        self.inventory = {}  # product_id -> quantity
        self.catalog = {}    # product_id -> Product
        self.order_history = []  # List of orders fulfilled
    
    def __str__(self):
        """String representation of the magazine."""
        return f"Magazine(id={self.magazine_id}, name='{self.name}')"
    
    def __repr__(self):
        """Detailed representation of the magazine."""
        return f"Magazine({self.magazine_id}, '{self.name}')"
    
    def add_product_to_catalog(self, product, initial_quantity=100):
        """
        Add a product to the magazine's catalog.
        
        Args:
            product (Product): The product to add
            initial_quantity (int): Initial stock quantity
        """
        self.catalog[product.product_id] = product
        self.inventory[product.product_id] = initial_quantity
    
    def get_stock_level(self, product_id):
        """
        Get current stock level for a product.
        
        Args:
            product_id (int): ID of the product
            
        Returns:
            int: Current stock quantity, or 0 if not in inventory
        """
        return self.inventory.get(product_id, 0)
    
    def fulfill_order(self, shop, product_id, quantity):
        """
        Fulfill an order from a shop.
        
        Args:
            shop: The Shop instance placing the order
            product_id (int): ID of the product to order
            quantity (int): Quantity to fulfill
            
        Returns:
            bool: True if order was fulfilled, False otherwise
        """
        # Check if product exists in catalog
        if product_id not in self.catalog:
            print(f"[Magazine] Product {product_id} not in catalog")
            return False
        
        # Check if sufficient stock available
        if self.inventory[product_id] < quantity:
            print(f"[Magazine] Insufficient stock for product {product_id}. Available: {self.inventory[product_id]}, Requested: {quantity}")
            return False
        
        # Fulfill order
        product = self.catalog[product_id]
        self.inventory[product_id] -= quantity
        
        # Record order
        self.order_history.append({
            'shop': shop,
            'product': product,
            'quantity': quantity
        })
        
        print(f"[Magazine] Fulfilled order: {quantity}x {product.name} to {shop.name}")
        return True
    
    def restock_product(self, product_id, quantity):
        """
        Restock a product in the magazine.
        
        Args:
            product_id (int): ID of the product to restock
            quantity (int): Quantity to add
        """
        if product_id in self.inventory:
            self.inventory[product_id] += quantity
            print(f"[Magazine] Restocked {quantity}x {self.catalog[product_id].name}")
        else:
            print(f"[Magazine] Product {product_id} not in catalog")
    
    def get_inventory_summary(self):
        """Get a summary of all products and their stock levels."""
        summary = []
        for product_id, quantity in self.inventory.items():
            product = self.catalog[product_id]
            summary.append({
                'product': product,
                'quantity': quantity
            })
        return summary
