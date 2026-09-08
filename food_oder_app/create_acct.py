import sqlite3
from werkzeug.security import generate_password_hash

def create_acct(first_name, middle_name, last_name, number, password):
    password_hash = generate_password_hash(password)

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (first_name, middle_name, last_name, number, password_hash) VALUES (?, ?, ?, ?, ?)",
            (first_name, middle_name, last_name, number, password_hash)
        )
    except sqlite3.IntegrityError:
        print("The number:", number, "is already registered")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_acct("Thomas", "", "Doe", "08012345678", "mypassword123")