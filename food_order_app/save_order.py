import os 
import psycopg 
from dotenv import load_dotenv 
from datetime import datetime 

load_dotenv() 
DATABASE_URL = os.getenv("DATABASE_URL") 

def save_order(user_id, cart): 
    conn = psycopg.connect(DATABASE_URL) 
    cursor = conn.cursor() 
    total = 0 

    for food, details in cart.items(): 
        total += details["quantity"] * details["price_per_unit"] 

    created_at = datetime.now().isoformat()

    cursor.execute( """ INSERT INTO orders (user_id, total, created_at) VALUES (%s, %s, %s) RETURNING id """, (user_id, total, created_at) ) 
        
    order_id = cursor.fetchone()[0] 
    for food_name, details in cart.items():
        quantity = details["quantity"] 
        price_bought = details["price_per_unit"] 
        cursor.execute( """ INSERT INTO order_items (order_id, food_name, quantity, price_bought) 
                       VALUES 
                       (%s, %s, %s, %s) """, 
                       (order_id, food_name, quantity, price_bought) )
        conn.commit()
        
    cursor.close()
    conn.close()