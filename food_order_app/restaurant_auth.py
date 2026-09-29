import os
import psycopg
from dotenv import load_dotenv
from functools import wraps
from flask import session, jsonify


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def restaurant_required(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return jsonify({
                "status": "error",
                "message": "Login required"
            }), 401

        conn = psycopg.connect(DATABASE_URL)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT role FROM users WHERE id = %s",
            (session["user_id"],)
        )

        user = cursor.fetchone()
        
        cursor.close()
        conn.close()

        if user is None or user[0] != "restaurant":
            return jsonify({
                "status": "error",
                "message": "Restaurant access required"
            }), 403

        return function(*args, **kwargs)

    return wrapper