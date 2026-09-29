import psycopg
import os
from dotenv import load_dotenv



load_dotenv()

VALID_TRANSITIONS = {
    "pending": "accepted",
    "accepted": "preparing",
    "preparing": "ready",
    "ready": "completed"
}

DATABASE_URL = os.getenv("DATABASE_URL")
def restaurant_status(order_id, new_status):
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT status FROM orders WHERE id = %s",
        (order_id,)
    )

    order = cursor.fetchone()

    if order is None:
        conn.close()
        return False

    current_status = order[0]

    if VALID_TRANSITIONS.get(current_status) != new_status:
        conn.close()
        return False

    cursor.execute("""
        UPDATE orders
        SET status = %s
        WHERE id = %s
    """, (new_status, order_id))

    conn.commit()
    conn.close()

    return True