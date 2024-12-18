import sqlite3
from datetime import datetime

def place_order(customer_id, items):
    connection = sqlite3.connect('./database/restaurant.db')
    cursor = connection.cursor()

    total_price = sum(item['price'] * item['quantity'] for item in items)
    order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("INSERT INTO Orders (customer_id, total_price, order_date) VALUES (?, ?, ?)", 
                   (customer_id, total_price, order_date))
    order_id = cursor.lastrowid

    for item in items:
        cursor.execute("INSERT INTO OrderDetails (order_id, item_id, quantity) VALUES (?, ?, ?)", 
                       (order_id, item['item_id'], item['quantity']))

    connection.commit()
    connection.close()
    print(f"Order placed! Order ID: {order_id}")
