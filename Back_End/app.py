from flask import Flask, jsonify, request, render_template
from read_write_menu import load_menu
from read_write_cart import load_cart
from increase_cart import increase_quantity
from decrease_cart import decrease_quantity
from checkout import checkout

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')


# 1. Route to get the whole menu data for the frontend
@app.route('/api/menu', methods=['GET'])
def get_menu():
    return jsonify(load_menu())

# 2. Route to get the current cart state
@app.route('/api/cart', methods=['GET'])
def get_cart():
    return jsonify(load_cart())

# 3. Route to change quantities when buttons are clicked
@app.route('/api/cart/modify', methods=['POST'])
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
def run_checkout():
    total = checkout()
    return jsonify({"status": "success", "total_charged": total})

if __name__ == '__main__':
    # Starts a real web server on your local machine
    app.run(debug=True, port=5000)
