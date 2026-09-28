import os
import psycopg
from dotenv import load_dotenv
from werkzeug.security import check_password_hash


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def login(number, password):
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, password_hash FROM users WHERE number = %s",
        (number,)
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        print("No account with that number")
        return False

    stored_id = row[0]
    stored_hash = row[1]

    if check_password_hash(stored_hash, password):
        print("Login successful")
        return stored_id
    else:
        print("Wrong password")
        return False