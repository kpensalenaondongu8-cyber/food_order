import sqlite3

def get_restaurant_orders():
   conn = sqlite3.connect("app.db")
   cursor = conn.cursor()


   cursor.execute("""
      SELECT id, user_id, total, created_at, status
      FROM orders
      ORDER BY id DESC
      """)
   orders = cursor.fetchall()
   result = []

   for order in orders:
    order_id = order[0]
    cursor.execute("""
        SELECT food_name, quantity, price_bought
        FROM order_items
        WHERE order_id = ?
        """, (order_id,))
    items = cursor.fetchall()  


    order_data = {
        "id": order[0],
        "user_id": order[1],
        "total": order[2],
        "created_at": order[3],
        "status": order[4],
        "items": items
    }
    result.append(order_data)

    conn.close
    return result