"""
Main demo script showing the shop system in action.

This demonstrates the interactions between:
- Product: Items that can be bought/ordered
- Customer: Buyers who purchase from shops
- Shop: Retailers that sell to customers and order from magazines
- Magazine: Warehouses that supply products to shops
"""

from product import Product
from customer import Customer
from shop import Shop
from magazine import Magazine


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def main():
    """Run the shop system demo."""
    
    print_section("SHOP SYSTEM DEMO")
    
    # 1. Create products
    print_section("1. Creating Products")
    products = [
        Product(1, "Laptop", 999.99, "High-performance laptop"),
        Product(2, "Mouse", 29.99, "Wireless mouse"),
        Product(3, "Keyboard", 79.99, "Mechanical keyboard"),
        Product(4, "Monitor", 299.99, "27-inch 4K monitor"),
        Product(5, "Headphones", 149.99, "Noise-canceling headphones")
    ]
    
    for product in products:
        print(f"Created: {product}")
    
    # 2. Create a magazine (warehouse)
    print_section("2. Creating Magazine (Warehouse)")
    warehouse = Magazine(1, "TechSupply Warehouse")
    print(f"Created: {warehouse}")
    
    # Add products to magazine catalog
    print("\nAdding products to warehouse catalog:")
    for product in products:
        warehouse.add_product_to_catalog(product, initial_quantity=50)
        print(f"  - {product.name}: {warehouse.get_stock_level(product.product_id)} units")
    
    # 3. Create a shop
    print_section("3. Creating Shop")
    tech_shop = Shop(1, "TechMart")
    print(f"Created: {tech_shop}")
    
    # Shop orders products from magazine
    print("\nShop ordering products from warehouse:")
    tech_shop.order_from_magazine(warehouse, 1, 10)  # 10 laptops
    tech_shop.order_from_magazine(warehouse, 2, 20)  # 20 mice
    tech_shop.order_from_magazine(warehouse, 3, 15)  # 15 keyboards
    tech_shop.order_from_magazine(warehouse, 4, 8)   # 8 monitors
    tech_shop.order_from_magazine(warehouse, 5, 12)  # 12 headphones
    
    # 4. Create customers
    print_section("4. Creating Customers")
    customers = [
        Customer(1, "Alice Johnson", 2000.00),
        Customer(2, "Bob Smith", 500.00),
        Customer(3, "Carol Williams", 1500.00)
    ]
    
    for customer in customers:
        print(f"Created: {customer}")
    
    # 5. Customers make purchases
    print_section("5. Customers Making Purchases")
    
    print("\nAlice buys a laptop and mouse:")
    customers[0].buy_product(tech_shop, 1, 1)  # 1 laptop
    customers[0].buy_product(tech_shop, 2, 1)  # 1 mouse
    
    print("\nBob tries to buy a laptop (insufficient funds):")
    customers[1].buy_product(tech_shop, 1, 1)  # Will fail - not enough money
    
    print("\nBob buys a keyboard:")
    customers[1].buy_product(tech_shop, 3, 1)  # 1 keyboard
    
    print("\nCarol buys a monitor and headphones:")
    customers[2].buy_product(tech_shop, 4, 1)  # 1 monitor
    customers[2].buy_product(tech_shop, 5, 1)  # 1 headphones
    
    # 6. Display current state
    print_section("6. Current System State")
    
    print("Shop Inventory:")
    for item in tech_shop.get_inventory_summary():
        print(f"  - {item['product'].name}: {item['quantity']} units")
    
    print(f"\nShop Revenue Report:")
    report = tech_shop.get_revenue_report()
    print(f"  Total Sales: {report['total_sales']}")
    print(f"  Total Revenue: ${report['total_revenue']:.2f}")
    
    print("\nWarehouse Inventory:")
    for item in warehouse.get_inventory_summary():
        print(f"  - {item['product'].name}: {item['quantity']} units")
    
    print("\nCustomer Purchase History:")
    for customer in customers:
        print(f"\n  {customer.name}:")
        print(f"    Current Balance: ${customer.balance:.2f}")
        print(f"    Total Spent: ${customer.get_total_spent():.2f}")
        print(f"    Purchases:")
        for purchase in customer.get_purchase_history():
            print(f"      - {purchase['quantity']}x {purchase['product'].name} (${purchase['cost']:.2f})")
    
    # 7. Shop reorders stock
    print_section("7. Shop Reordering Stock")
    print("Shop needs more laptops:")
    tech_shop.order_from_magazine(warehouse, 1, 5)  # 5 more laptops
    
    # 8. More customer purchases
    print_section("8. Additional Customer Purchases")
    print("\nAlice buys another mouse:")
    customers[0].buy_product(tech_shop, 2, 1)
    
    # 9. Final summary
    print_section("9. Final Summary")
    final_report = tech_shop.get_revenue_report()
    print(f"Shop: {tech_shop}")
    print(f"  Inventory items: {len(tech_shop.inventory)}")
    print(f"  Total sales: {final_report['total_sales']}")
    print(f"  Revenue: ${tech_shop.revenue:.2f}")
    
    print(f"\nWarehouse: {warehouse}")
    print(f"  Catalog items: {len(warehouse.catalog)}")
    print(f"  Orders fulfilled: {len(warehouse.order_history)}")
    
    print("\nCustomers:")
    for customer in customers:
        print(f"  {customer.name}: ${customer.balance:.2f} remaining, {len(customer.purchases)} purchases")
    
    print_section("DEMO COMPLETE")


if __name__ == "__main__":
    main()
