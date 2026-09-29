import psycopg
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


def get_order_history(user_id):
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, total, created_at FROM orders WHERE user_id = %s ORDER BY created_at DESC",
        (user_id,)
    )
    orders = cursor.fetchall()

    full_history = []
    for order_id, total, created_at in orders:
        cursor.execute(
            "SELECT food_name, quantity, price_bought FROM order_items WHERE order_id = %s",
            (order_id,)
        )
        items = cursor.fetchall()
        full_history.append({
            "order_id": order_id,
            "total": total,
            "created_at": created_at,
            "items": items
        })

    cursor.close()
    conn.close()
    return full_history

if __name__ == "__main__":
    import json
    history = get_order_history(2)
    print(json.dumps(history, indent=2))