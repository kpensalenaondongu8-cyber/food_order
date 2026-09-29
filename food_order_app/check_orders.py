import psycopg
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


conn = psycopg.connect(DATABASE_URL)

cursor = conn.cursor()

cursor.execute(
    "SELECT id, user_id, total, created_at, status FROM orders ORDER BY id DESC"
)

orders = cursor.fetchall()

for order in orders:
    print(order)

cursor.close()
conn.close()