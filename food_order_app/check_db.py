import psycopg
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
 
conn = psycopg.connect(DATABASE_URL)

cursor =  conn.cursor()
for table in ["users", "orders", "order_items"]: 
    print(f"\n--- {table} ---") 

    cursor.execute(""" SELECT column_name, data_type 
                   FROM information_schema.columns WHERE table_name = %s 
                   ORDER BY ordinal_position 
    """,
                    (table,)) 
    schema = cursor.fetchall() 

    for column in schema: 
        print(column) 

print("\n--- USERS ---") 

cursor.execute(""" SELECT id, first_name, last_name, number, role 
                   FROM users ORDER BY id 
                   """) 
users = cursor.fetchall() 

for user in users: 
        print(user) 

cursor.close() 
conn.close()