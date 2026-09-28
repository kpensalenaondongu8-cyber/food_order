import sqlite3
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

sqlite_conn = sqlite3.connect("app.db")
postgres_conn = psycopg.connect(DATABASE_URL)

sqlite_cursor = sqlite_conn.cursor()
postgres_cursor = postgres_conn.cursor()

sqlite_cursor.execute("SELECT * FROM users")
users = sqlite_cursor.fetchall()

for user in users:
    postgres_cursor.execute("""
    INSERT INTO users
    (id, first_name, middle_name, last_name, number, password_hash, role)
    OVERRIDING SYSTEM VALUE
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", user)

postgres_conn.commit()