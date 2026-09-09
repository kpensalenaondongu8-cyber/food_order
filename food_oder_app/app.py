from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from read_write_menu import load_menu
from read_write_cart import load_cart
from increase_cart import increase_quantity
from decrease_cart import decrease_quantity
from remove_from_cart import Rem_Fro_Cart
from checkout import checkout
from login import login
from create_acct import create_acct
import os
from dotenv import load_dotenv
from wrap import login_required

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")


@app.route('/')
def home():
    if "user_id" in session:
        return redirect(url_for('logged_in_home'))
    return render_template('guest.html')


@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/home')
def logged_in_home():
    return render_template('home.html')

@app.route('/cart')
def cart_page():
    return render_template('cart.html')


@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    number = data.get("number")
    password = data.get("password")

    user_id = login(number, password)
    if user_id is not False:
        session["user_id"] = user_id
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Invalid number or password"}), 401


@app.route('/api/signup', methods=['POST'])
def api_signup():
    data = request.json
    create_acct(
        data.get("first_name"),
        data.get("middle_name", ""),
        data.get("last_name"),
        data.get("number"),
        data.get("password")
    )
    return jsonify({"status": "success"})


@app.route('/api/logout', methods=['POST'])
def api_logout():
    session.pop("user_id", None)
    return jsonify({"status": "success"})


# 1. Route to get the whole menu data for the frontend
@app.route('/api/menu', methods=['GET'])
def get_menu():
    return jsonify(load_menu())

# 2. Route to get the current cart state
@app.route('/api/cart', methods=['GET'])
@login_required
def get_cart():
    return jsonify(load_cart())

# 3. Route to change quantities when buttons are clicked
@app.route('/api/cart/modify', methods=['POST'])
@login_required
def modify():
    data = request.json
    item = data.get("item")
    action = data.get("action")
    amount = data.get("amount", 1)
    
    if action == "increase":
        increase_quantity(item, amount)
    elif action == "decrease":
        decrease_quantity(item, amount)
        
    return jsonify({"status": "success", "cart": load_cart()})

# 4. Route to trigger checkout
@app.route('/api/checkout', methods=['POST'])
@login_required
def run_checkout():
    total = checkout()
    return jsonify({"status": "success", "total_charged": total})


# 5. Route to remove an item from the cart entirely
@app.route('/api/cart/remove', methods=['POST'])
@login_required
def remove():
    data = request.json
    item = data.get("item")
    Rem_Fro_Cart(item)
    return jsonify({"status": "success", "cart": load_cart()})
if __name__ == '__main__':
    # Starts a real web server on your local machine
    app.run(debug=True, port=5000)
