from functools import wraps
from flask import session, jsonify

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"status": "error", "message": "Please log in first"}), 401
        return f(*args, **kwargs)
    return wrapper