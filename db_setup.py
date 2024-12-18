import sqlite3

# Connect to SQLite database (will create if it doesn't exist)
connection = sqlite3.connect("database/restaurant.db")
cursor = connection.cursor()

# Drop existing tables to reset the schema
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS menu")


# Create Menu table
cursor.execute("""
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT NOT NULL
)
""")

# Create Orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    ordered_items TEXT NOT NULL,
    total_price REAL NOT NULL,
    order_date TEXT DEFAULT (datetime('now', 'localtime'))
)
""")

# Insert sample menu items
sample_menu = [
    ("Margherita Pizza", 8.99, "Main Course"),
    ("Chicken Burger", 5.99, "Main Course"),
    ("Caesar Salad", 4.99, "Appetizer"),
    ("Chocolate Cake", 3.99, "Dessert"),
    ("Coffee", 2.49, "Beverage")
]

cursor.executemany("INSERT INTO menu (name, price, category) VALUES (?, ?, ?)", sample_menu)

# Insert sample orders
sample_orders = [
    ("Alice", "Margherita Pizza, Coffee", 11.48),
    ("Bob", "Chicken Burger, Chocolate Cake", 9.98),
]

cursor.executemany("INSERT INTO orders (customer_name, ordered_items, total_price) VALUES (?, ?, ?)", sample_orders)

# Commit changes and close connection
connection.commit()
connection.close()

print("Database setup completed with sample data.")
