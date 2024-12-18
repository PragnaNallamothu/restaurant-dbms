import sqlite3

# Database connection
DB_PATH = "database/restaurant.db"

def display_menu():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM menu")
        rows = cursor.fetchall()
        print("\n--- Menu ---")
        for row in rows:
            print(f"{row[0]}. {row[1]} (${row[2]:.2f}) - {row[3]}")
        print()

def add_menu_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    category = input("Enter item category: ")
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO menu (name, price, category) VALUES (?, ?, ?)", (name, price, category))
        conn.commit()
        print("Menu item added successfully.")

def place_order():
    customer_name = input("Enter customer name: ")
    display_menu()
    item_ids = input("Enter item IDs (comma-separated): ").split(",")
    item_ids = [int(id.strip()) for id in item_ids]
    
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, price FROM menu WHERE id IN ({seq})".format(seq=','.join(['?']*len(item_ids))), item_ids)
        items = cursor.fetchall()
        
        ordered_items = ", ".join([item[0] for item in items])
        total_price = sum([item[1] for item in items])
        
        cursor.execute("INSERT INTO orders (customer_name, ordered_items, total_price) VALUES (?, ?, ?)",
                       (customer_name, ordered_items, total_price))
        conn.commit()
        print(f"Order placed successfully for {customer_name}. Total: ${total_price:.2f}")

def main():
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. View Menu")
        print("2. Add Menu Item")
        print("3. Place Order")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_menu()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            place_order()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
