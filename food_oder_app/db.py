import sqlite3

DB_NAME = "app.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print("Creating users table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            number TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    print("users done")

    print("Creating orders table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            total REAL NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    print("orders done")

    print("Creating order_items table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            food_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price_bought REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id)
        )
    """)
    print("order_items done")

    conn.commit()
    print("Committed")

    # Check immediately, same connection, before closing anything
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print("Tables that exist right now:", cursor.fetchall())

    conn.close()
    print("Closed")

if __name__ == "__main__":
    init_db()