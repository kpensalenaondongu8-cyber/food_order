import sqlite3
from datetime import datetime

def save_order(user_id, cart):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    total = 0
    for food, details in cart.items():
        total += details["quantity"] * details["price_per_unit"]

    created_at = datetime.now().isoformat()
    cursor.execute(
        "INSERT INTO orders (user_id, total, created_at) VALUES (?, ?, ?)",
        (user_id, total, created_at)
    )
    order_id = cursor.lastrowid

    for food_name, details in cart.items():
       quantity = details["quantity"]
       price_bought = details["price_per_unit"]
       
       cursor.execute(
        "INSERT INTO order_items (order_id, food_name, quantity, price_bought) VALUES (?, ?, ?, ?)",
        (order_id, food_name, quantity, price_bought)
    )
    conn.commit()
    conn.close()
  