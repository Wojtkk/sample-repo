"""Customer class representing buyers who can purchase products from shops."""

from product import Product


class Customer:
    """Represents a customer who can buy products from a shop."""
    
    def __init__(self, customer_id, name, balance):
        """
        Initialize a Customer.
        
        Args:
            customer_id (int): Unique identifier for the customer
            name (str): Name of the customer
            balance (float): Available money the customer has
        """
        self.customer_id = customer_id
        self.name = name
        self.balance = balance
        self.purchases = []  # List of purchased products
    
    def __str__(self):
        """String representation of the customer."""
        return f"Customer(id={self.customer_id}, name='{self.name}', balance=${self.balance:.2f})"
    
    def __repr__(self):
        """Detailed representation of the customer."""
        return f"Customer({self.customer_id}, '{self.name}', {self.balance})"
    
    def buy_product(self, shop, product_id, quantity=1):
        """
        Buy a product from a shop.
        
        Args:
            shop: The Shop instance to buy from
            product_id (int): ID of the product to buy
            quantity (int): Number of items to buy
            
        Returns:
            bool: True if purchase was successful, False otherwise
        """
        # Shop will handle the transaction
        return shop.sell_product(self, product_id, quantity)
    
    def add_purchase(self, product, quantity, total_cost):
        """
        Record a purchase.
        
        Args:
            product (Product): The product that was purchased
            quantity (int): Number of items purchased
            total_cost (float): Total cost of the purchase
        """
        self.purchases.append({
            'product': product,
            'quantity': quantity,
            'cost': total_cost
        })
        self.balance -= total_cost
    
    def get_purchase_history(self):
        """Get the customer's purchase history."""
        return self.purchases
    
    def get_total_spent(self):
        """Calculate total amount spent by customer."""
        return sum(purchase['cost'] for purchase in self.purchases)
