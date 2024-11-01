import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("sales_database.db")
cursor = conn.cursor()

# Create SALES table
cursor.execute("""
CREATE TABLE IF NOT EXISTS SALES (
    Date TEXT,
    Order_id INTEGER PRIMARY KEY,
    Item_id INTEGER,
    Customer_id INTEGER,
    Quantity INTEGER,
    Revenue REAL
);
""")

# Create ITEMS table
cursor.execute("""
CREATE TABLE IF NOT EXISTS ITEMS (
    Item_id INTEGER PRIMARY KEY,
    Item_name TEXT,
    Price REAL,
    Department TEXT
);
""")

# Create CUSTOMERS table
cursor.execute("""
CREATE TABLE IF NOT EXISTS CUSTOMERS (
    Customer_id INTEGER PRIMARY KEY,
    First_name TEXT,
    Last_name TEXT,
    Address TEXT
);
""")

# Sample data insertion
# Insert data into SALES table
sales_data = [
    ('2023-03-18', 1, 1, 1, 2, 50.0),
    ('2023-03-18', 2, 2, 2, 1, 30.0),
    ('2023-01-15', 3, 3, 1, 3, 75.0),
    ('2022-12-10', 4, 4, 3, 1, 45.0)
]
cursor.executemany("INSERT INTO SALES (Date, Order_id, Item_id, Customer_id, Quantity, Revenue) VALUES (?, ?, ?, ?, ?, ?);", sales_data)

# Insert data into ITEMS table
items_data = [
    (1, 'Laptop', 500.0, 'Electronics'),
    (2, 'Phone', 300.0, 'Electronics'),
    (3, 'Desk', 150.0, 'Furniture'),
    (4, 'Chair', 75.0, 'Furniture')
]
cursor.executemany("INSERT INTO ITEMS (Item_id, Item_name, Price, Department) VALUES (?, ?, ?, ?);", items_data)

# Insert data into CUSTOMERS table
customers_data = [
    (1, 'John', 'Doe', '123 Main St'),
    (2, 'Jane', 'Smith', '456 Elm St'),
    (3, 'Bob', 'Brown', '789 Oak St')
]
cursor.executemany("INSERT INTO CUSTOMERS (Customer_id, First_name, Last_name, Address) VALUES (?, ?, ?, ?);", customers_data)

# Commit and close
conn.commit()
conn.close()

print("Database and tables created with sample data.")
