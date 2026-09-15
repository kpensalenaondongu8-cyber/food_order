import sqlite3
from functools import wraps
from flask import session, jsonify


def restaurant_required(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return jsonify({
                "status": "error",
                "message": "Login required"
            }), 401

        conn = sqlite3.connect("app.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT role FROM users WHERE id = ?",
            (session["user_id"],)
        )

        user = cursor.fetchone()

        conn.close()

        if user is None or user[0] != "restaurant":
            return jsonify({
                "status": "error",
                "message": "Restaurant access required"
            }), 403

        return function(*args, **kwargs)

    return wrapper