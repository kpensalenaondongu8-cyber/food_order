import sqlite3

def get_order_history(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, total, created_at FROM orders WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,)
    )
    orders = cursor.fetchall()

    full_history = []
    for order_id, total, created_at in orders:
        cursor.execute(
            "SELECT food_name, quantity, price_bought FROM order_items WHERE order_id = ?",
            (order_id,)
        )
        items = cursor.fetchall()
        full_history.append({
            "order_id": order_id,
            "total": total,
            "created_at": created_at,
            "items": items
        })

    conn.close()
    return full_history

if __name__ == "__main__":
    import json
    history = get_order_history(2)
    print(json.dumps(history, indent=2))