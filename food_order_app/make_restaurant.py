import psycopg
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


conn = psycopg.connect(DATABASE_URL)
cursor = conn.cursor()

cursor.execute("""
    UPDATE users
    SET role = 'restaurant'
    WHERE id = 2;
""")

conn.commit()

cursor.close()
conn.close()

print("User 2 is now a restaurant account")