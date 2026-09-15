import sqlite3

def restaurant_status(order_id, new_status):
   conn = sqlite3.connect("app.db")
   cursor = conn.cursor()

   cursor.execute("""
          UPDATE orders
         SET status = ?
          WHERE id = ?""",
           (new_status, order_id))
   conn.commit()
   conn.close()