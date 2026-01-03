"""Product class representing items that can be bought and ordered."""


class Product:
    """Represents a product that can be sold in a shop."""
    
    def __init__(self, product_id, name, price, description=""):
        """
        Initialize a Product.
        
        Args:
            product_id (int): Unique identifier for the product
            name (str): Name of the product
            price (float): Price of the product
            description (str): Optional description of the product
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
    
    def __str__(self):
        """String representation of the product."""
        return f"Product(id={self.product_id}, name='{self.name}', price=${self.price:.2f})"
    
    def __repr__(self):
        """Detailed representation of the product."""
        return f"Product({self.product_id}, '{self.name}', {self.price}, '{self.description}')"
    
    def get_info(self):
        """Get detailed information about the product."""
        return {
            'id': self.product_id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }
