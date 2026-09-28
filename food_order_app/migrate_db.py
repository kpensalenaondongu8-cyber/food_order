import sqlite3
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


sqlite_conn = sqlite3.connect("app.db")
sqlite_cursor = sqlite_conn.cursor()


postgres_conn = psycopg.connect(DATABASE_URL)
postgres_cursor = postgres_conn.cursor()


try:


    sqlite_cursor.execute("SELECT * FROM users")
    users = sqlite_cursor.fetchall()

    for user in users:
        postgres_cursor.execute("""
            INSERT INTO users
            (id, first_name, middle_name, last_name, number, password_hash, role)
            OVERRIDING SYSTEM VALUE
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, user)


    sqlite_cursor.execute("SELECT * FROM orders")
    orders = sqlite_cursor.fetchall()


    for order in orders:
        postgres_cursor.execute("""
            INSERT INTO orders
            (id, user_id, total, created_at, status)
            OVERRIDING SYSTEM VALUE
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, order)


  

    sqlite_cursor.execute("SELECT * FROM order_items")
    order_items = sqlite_cursor.fetchall()

    for item in order_items:
        postgres_cursor.execute("""
            INSERT INTO order_items
            (id, order_id, food_name, quantity, price_bought)
            OVERRIDING SYSTEM VALUE
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, item)


    postgres_conn.commit()

    print("Migration completed successfully!")


except Exception as e:

    postgres_conn.rollback()

    print("Migration failed:")
    print(e)


finally:

    sqlite_cursor.close()
    sqlite_conn.close()

    postgres_cursor.close()
    postgres_conn.close()