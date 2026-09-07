import sqlite3

from werkzeug.security import check_password_hash

def login(number, password):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE number = ?", (number,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        print("No account with that number")
        return False

    stored_hash = row[0]
    if check_password_hash(stored_hash, password):
        print("Login successful")
        return True
    else:
        print("Wrong password")
        return False
