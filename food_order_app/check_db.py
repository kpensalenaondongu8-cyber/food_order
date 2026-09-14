import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

for table in ["users", "orders", "order_items"]:
    print(f"\n--- {table} ---")
    cursor.execute(f"PRAGMA table_info({table})")
    schema = cursor.fetchall()
    for column in schema:
        print(column)

conn.close()