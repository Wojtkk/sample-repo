# Shop System - Class Structure and Dependencies

This repository contains a simple shop system implemented in Python to demonstrate class dependencies and call graphs. The system models a retail environment where customers buy products from shops, and shops order inventory from warehouses (magazines).

## Class Structure

### 1. Product (`product.py`)
**Purpose**: Represents items that can be bought and ordered.

**Attributes**:
- `product_id`: Unique identifier
- `name`: Product name
- `price`: Product price
- `description`: Product description

**Methods**:
- `get_info()`: Returns product details

**Dependencies**: None (base class)

---

### 2. Customer (`customer.py`)
**Purpose**: Represents buyers who purchase products from shops.

**Attributes**:
- `customer_id`: Unique identifier
- `name`: Customer name
- `balance`: Available money
- `purchases`: List of purchase history

**Methods**:
- `buy_product(shop, product_id, quantity)`: Purchase from a shop
- `add_purchase(product, quantity, total_cost)`: Record a purchase
- `get_purchase_history()`: View purchase history
- `get_total_spent()`: Calculate total spending

**Dependencies**:
- Imports: `Product`
- Interacts with: `Shop` (calls `shop.sell_product()`)

---

### 3. Magazine (`magazine.py`)
**Purpose**: Represents a warehouse/supplier that fulfills shop orders.

**Attributes**:
- `magazine_id`: Unique identifier
- `name`: Magazine name
- `inventory`: Product quantities (product_id → quantity)
- `catalog`: Available products (product_id → Product)
- `order_history`: List of fulfilled orders

**Methods**:
- `add_product_to_catalog(product, initial_quantity)`: Add products to catalog
- `get_stock_level(product_id)`: Check inventory levels
- `fulfill_order(shop, product_id, quantity)`: Process shop orders
- `restock_product(product_id, quantity)`: Replenish inventory
- `get_inventory_summary()`: View all inventory

**Dependencies**:
- Imports: `Product`
- Interacts with: `Shop` (receives orders from shops)

---

### 4. Shop (`shop.py`)
**Purpose**: Represents a retail shop that sells to customers and orders from magazines.

**Attributes**:
- `shop_id`: Unique identifier
- `name`: Shop name
- `inventory`: Product quantities
- `products`: Available products
- `sales_history`: List of sales transactions
- `revenue`: Total revenue earned

**Methods**:
- `add_product(product, quantity)`: Add to inventory
- `get_stock_level(product_id)`: Check inventory
- `order_from_magazine(magazine, product_id, quantity)`: Order from warehouse
- `sell_product(customer, product_id, quantity)`: Sell to customer
- `get_inventory_summary()`: View inventory
- `get_revenue_report()`: View sales statistics

**Dependencies**:
- Imports: `Product`, `Customer`
- Interacts with: `Magazine` (calls `magazine.fulfill_order()`)
- Interacts with: `Customer` (receives purchase requests, calls `customer.add_purchase()`)

---

## Dependency Graph

```
┌─────────────────┐
│    Product      │ (Base - no dependencies)
└────────┬────────┘
         │
         ├─────────────────────┐
         │                     │
         ▼                     ▼
┌─────────────────┐   ┌─────────────────┐
│    Magazine     │   │    Customer     │
│   (Warehouse)   │   │                 │
└────────┬────────┘   └────────┬────────┘
         │                     │
         │        ┌────────────┘
         │        │
         ▼        ▼
    ┌─────────────────┐
    │      Shop       │
    │   (Retailer)    │
    └─────────────────┘
```

## Call Graph / Interaction Flow

### Flow 1: Shop orders from Magazine
```
Shop.order_from_magazine()
  └──> Magazine.fulfill_order()
         └──> Shop.add_product()
```

### Flow 2: Customer buys from Shop
```
Customer.buy_product()
  └──> Shop.sell_product()
         └──> Customer.add_purchase()
```

## Key Interactions

1. **Magazine → Shop**: Magazine supplies products to shop via `fulfill_order()`
2. **Shop → Customer**: Shop sells products to customers via `sell_product()`
3. **Customer → Shop**: Customer initiates purchases via `buy_product()`
4. **Shop → Magazine**: Shop places orders via `order_from_magazine()`

## Running the Demo

Execute the main demo script:

```bash
python3 main.py
```

This will demonstrate:
- Creating products, shops, warehouses, and customers
- Shops ordering inventory from warehouses
- Customers purchasing from shops
- Inventory management
- Revenue tracking
- Transaction history

## Design Features

### For Dependency Analysis:
- **Clear separation of concerns**: Each class has a distinct responsibility
- **Bidirectional relationships**: Shop↔Magazine, Shop↔Customer
- **Transitive dependencies**: Customer depends on Shop, which depends on Magazine
- **Data flow tracking**: Purchase history, order history, sales history

### For Call Graph Analysis:
- **Method chaining**: Customer.buy_product() → Shop.sell_product() → Customer.add_purchase()
- **Cross-class method calls**: Multiple classes calling methods on other classes
- **State modifications**: Methods that update state in multiple objects
- **Validation logic**: Checks before executing transactions (balance, inventory)

## Complexity Features

The system includes enough complexity for meaningful analysis:
- **4 interconnected classes** with clear dependencies
- **Multiple interaction patterns** (orders, sales, restocking)
- **State management** across multiple objects
- **Transaction validation** and error handling
- **History tracking** for auditing
- **Bidirectional communication** between classes
