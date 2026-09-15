import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute("""
    UPDATE users
    SET role = 'restaurant'
    WHERE id = 2;
""", )

conn.commit()
conn.close()

print("User 2 is now a restaurant account")