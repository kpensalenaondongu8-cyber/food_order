import sqlite3
from werkzeug.security import generate_password_hash

def create_acct(first_name, middle_name, last_name, number, password):
    print("Starting create_acct for", number)
    password_hash = generate_password_hash(password)
    print("Password hashed")

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    print("Connected, cursor ready")

    try:
        cursor.execute(
            "INSERT INTO users (first_name, middle_name, last_name, number, password_hash) VALUES (?, ?, ?, ?, ?)",
            (first_name, middle_name, last_name, number, password_hash)
        )
        print("Insert executed")
    except sqlite3.IntegrityError:
        print("The number:", number, "is already registered")

    conn.commit()
    print("Committed")
    conn.close()
    print("Closed")

if __name__ == "__main__":
    create_acct("Thomas", "", "Doe", "08012345678", "mypassword123")