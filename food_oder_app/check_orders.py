import sqlite3

conn = sqlite3.connect("app.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT id, user_id, total, created_at, status FROM orders ORDER BY id DESC"
)

orders = cursor.fetchall()

for order in orders:
    print(order)

conn.close()