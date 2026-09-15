import sqlite3


VALID_TRANSITIONS = {
    "pending": "accepted",
    "accepted": "preparing",
    "preparing": "ready",
    "ready": "completed"
}


def restaurant_status(order_id, new_status):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT status FROM orders WHERE id = ?",
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
        SET status = ?
        WHERE id = ?
    """, (new_status, order_id))

    conn.commit()
    conn.close()

    return True