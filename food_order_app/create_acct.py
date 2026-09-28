import os
import psycopg
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def create_acct(first_name, middle_name, last_name, number, password):
    password_hash = generate_password_hash(password)

    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users
            (first_name, middle_name, last_name, number, password_hash)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (first_name, middle_name, last_name, number, password_hash)
        )

        conn.commit()

        print("Account created successfully")
        return True

    except psycopg.errors.UniqueViolation:
        conn.rollback()
        print("The number:", number, "is already registered")
        return False

    finally:
        cursor.close()
        conn.close()
