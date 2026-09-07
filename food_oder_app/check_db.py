import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Rows:", rows)

cursor.execute("PRAGMA table_info(users)")
schema = cursor.fetchall()
print("Schema:", schema)

conn.close()